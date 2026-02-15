import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage


# ------------------------ Helpers ------------------------

def bytes_to_mb(value: int) -> float:
    return value / (1024 * 1024)


def get_env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


# ------------------------ Email Feature ------------------------

def SendEmailWithLog(receiver_email: str, log_file_path: str, summary: dict) -> bool:
    """
    Sends an email with the log file attached.
    Sender credentials must be provided via env variables:

    PSS_SENDER_EMAIL  = sender gmail (example: yourmail@gmail.com)
    PSS_SENDER_PASS   = gmail app password (NOT normal password)
    Optional:
    PSS_SMTP_SERVER   = smtp.gmail.com
    PSS_SMTP_PORT     = 465
    """
    sender_email = get_env("PSS_SENDER_EMAIL")
    sender_pass = get_env("PSS_SENDER_PASS")
    smtp_server = get_env("PSS_SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(get_env("PSS_SMTP_PORT", "465"))

    if not sender_email or not sender_pass:
        # As per rule, avoid console spam; but still inform user minimally
        print("Email not sent: set PSS_SENDER_EMAIL and PSS_SENDER_PASS environment variables.")
        return False

    try:
        msg = EmailMessage()
        msg["Subject"] = f"Platform Surveillance Report - {time.strftime('%Y-%m-%d %H:%M:%S')}"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        body_lines = [
            "Platform Surveillance System - Summary",
            "-" * 50,
            f"Total processes: {summary.get('total_processes', 'NA')}",
            "",
            "Top CPU usage processes:",
        ]
        for item in summary.get("top_cpu", []):
            body_lines.append(f"- {item['name']} (PID {item['pid']}): {item['cpu_percent']:.2f}%")

        body_lines.append("")
        body_lines.append("Top Memory (RSS) usage processes:")
        for item in summary.get("top_mem", []):
            body_lines.append(
                f"- {item['name']} (PID {item['pid']}): {bytes_to_mb(item['rss_bytes']):.2f} MB"
            )

        body_lines.append("")
        body_lines.append("Top Thread count processes:")
        for item in summary.get("top_threads", []):
            body_lines.append(f"- {item['name']} (PID {item['pid']}): {item['threads_count']} threads")

        body_lines.append("")
        body_lines.append("Top Open files count processes:")
        for item in summary.get("top_open_files", []):
            open_files_val = item["open_files_count"]
            body_lines.append(f"- {item['name']} (PID {item['pid']}): {open_files_val}")

        msg.set_content("\n".join(body_lines))

        # Attach log file
        with open(log_file_path, "rb") as f:
            data = f.read()
        filename = os.path.basename(log_file_path)
        msg.add_attachment(data, maintype="application", subtype="octet-stream", filename=filename)

        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_pass)
            server.send_message(msg)

        return True

    except Exception as e:
        print("Email sending failed:", e)
        return False


# ------------------------ Core Scanning ------------------------

def ProcessScan() -> list[dict]:
    """
    Returns a list of dicts for each process with:
    Process Name, PID, CPU %, RSS, VMS, Memory %, Threads Count, Open Files Count, Timestamp
    Handles AccessDenied safely.
    """
    processes = []

    # Warm-up CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(None)
        except Exception:
            pass

    time.sleep(0.2)

    now_ts = time.strftime("%Y-%m-%d %H:%M:%S")

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name"])
            pid = info.get("pid")
            name = info.get("name") or "NA"

            cpu_p = proc.cpu_percent(None)

            # memory
            rss_bytes = 0
            vms_bytes = 0
            mem_percent = 0.0
            try:
                memi = proc.memory_info()
                rss_bytes = int(memi.rss)
                vms_bytes = int(memi.vms)
                mem_percent = float(proc.memory_percent())
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

            # threads
            threads_count = 0
            try:
                threads_count = proc.num_threads()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                threads_count = -1  # indicate access denied / not available

            # open files
            # If AccessDenied -> record as "Access Denied"
            open_files_count = 0
            open_files_note = ""
            try:
                of = proc.open_files()
                open_files_count = len(of)
            except psutil.AccessDenied:
                open_files_note = "Access Denied"
                open_files_count = -1
            except (psutil.NoSuchProcess, psutil.ZombieProcess):
                open_files_count = 0

            processes.append({
                "timestamp": now_ts,
                "pid": pid,
                "name": name,
                "cpu_percent": float(cpu_p),
                "rss_bytes": rss_bytes,
                "vms_bytes": vms_bytes,
                "memory_percent": float(mem_percent),
                "threads_count": int(threads_count),
                "open_files_count": open_files_count,
                "open_files_note": open_files_note,
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return processes


def BuildSummary(processes: list[dict]) -> dict:
    """
    Create summary for email:
    - total processes
    - top 5 cpu
    - top 5 memory (rss)
    - top 5 threads
    - top 5 open files (excluding AccessDenied where possible)
    """
    summary = {"total_processes": len(processes)}

    top_cpu = sorted(processes, key=lambda x: x.get("cpu_percent", 0.0), reverse=True)[:5]
    top_mem = sorted(processes, key=lambda x: x.get("rss_bytes", 0), reverse=True)[:5]

    # threads: treat -1 as very small
    top_threads = sorted(processes, key=lambda x: (x.get("threads_count", -1) if x.get("threads_count", -1) >= 0 else -1),
                         reverse=True)[:5]

    # open files: treat -1 as very small
    top_open = sorted(processes, key=lambda x: (x.get("open_files_count", -1) if x.get("open_files_count", -1) >= 0 else -1),
                      reverse=True)[:5]

    summary["top_cpu"] = top_cpu
    summary["top_mem"] = top_mem
    summary["top_threads"] = top_threads
    summary["top_open_files"] = top_open

    return summary


# ------------------------ Logging ------------------------

def CreateLog(folder_name: str) -> tuple[str, dict]:
    """
    Creates log file inside folder_name.
    Returns: (log_file_path, summary_dict)
    """
    border = "-" * 60

    if os.path.exists(folder_name):
        if not os.path.isdir(folder_name):
            raise RuntimeError("Unable to create folder: file exists with same name.")
    else:
        os.mkdir(folder_name)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_file_path = os.path.join(folder_name, f"Marvellous_{timestamp}.log")

    # System report
    cpu_total = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    net = psutil.net_io_counters()

    processes = ProcessScan()
    summary = BuildSummary(processes)

    # Top 10 memory consuming processes (Requirement)
    top10_mem = sorted(processes, key=lambda x: x.get("rss_bytes", 0), reverse=True)[:10]

    with open(log_file_path, "w") as fobj:
        fobj.write(border + "\n")
        fobj.write("---- Marvellous Platform Surveillance System -----\n")
        fobj.write(f"Log created at: {time.ctime()}\n")
        fobj.write(border + "\n\n")

        fobj.write("----------------- System Report ------------------\n")
        fobj.write(f"CPU Usage: {cpu_total:.2f} %\n")
        fobj.write(f"RAM Usage: {mem.percent:.2f} %\n")
        fobj.write(border + "\n")

        fobj.write("\nDisk Usage Report\n")
        fobj.write(border + "\n")
        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                fobj.write(f"{part.mountpoint} -> {usage.percent:.2f} % used\n")
            except Exception:
                pass
        fobj.write(border + "\n")

        fobj.write("\nNetwork Usage Report\n")
        fobj.write(f"Sent: {bytes_to_mb(net.bytes_sent):.2f} MB\n")
        fobj.write(f"Recv: {bytes_to_mb(net.bytes_recv):.2f} MB\n")
        fobj.write(border + "\n\n")

        # Requirement: show Top 10 memory consuming processes
        fobj.write("Top 10 Memory Consuming Processes (by RSS)\n")
        fobj.write(border + "\n")
        for p in top10_mem:
            fobj.write(
                f"{p['name']} (PID {p['pid']}) -> RSS: {bytes_to_mb(p['rss_bytes']):.2f} MB | "
                f"VMS: {bytes_to_mb(p['vms_bytes']):.2f} MB | Mem%: {p['memory_percent']:.2f}%\n"
            )
        fobj.write(border + "\n\n")

        # Per-process detailed entries (Expected Output Format)
        fobj.write("Expected Output in Log File (Per Process Entry)\n")
        fobj.write(border + "\n")

        for info in processes:
            fobj.write(f"Timestamp: {info['timestamp']}\n")
            fobj.write(f"Process Name: {info['name']}\n")
            fobj.write(f"PID: {info['pid']}\n")
            fobj.write(f"CPU %: {info['cpu_percent']:.2f}\n")
            fobj.write(f"Memory (RSS): {bytes_to_mb(info['rss_bytes']):.2f} MB\n")
            fobj.write(f"Memory (VMS): {bytes_to_mb(info['vms_bytes']):.2f} MB\n")
            fobj.write(f"Memory %: {info['memory_percent']:.2f}\n")

            tc = info["threads_count"]
            fobj.write(f"Threads Count: {tc if tc >= 0 else 'Access Denied'}\n")

            ofc = info["open_files_count"]
            if ofc >= 0:
                fobj.write(f"Open Files Count: {ofc}\n")
            else:
                fobj.write("Open Files Count: Access Denied\n")

            fobj.write(border + "\n")

        fobj.write(border + "\n")
        fobj.write("----------------- End of Log File ----------------\n")
        fobj.write(border + "\n")

    return log_file_path, summary


# ------------------------ Scheduler Job ------------------------

def Job(folder_name: str, receiver_email: str | None):
    log_file_path, summary = CreateLog(folder_name)

    # If receiver is provided, send email
    if receiver_email:
        ok = SendEmailWithLog(receiver_email, log_file_path, summary)
        if ok:
            print(f"Email sent to {receiver_email} with log: {os.path.basename(log_file_path)}")
        else:
            print("Email not sent (check env vars / permissions).")


# ------------------------ Main ------------------------

def main():
    border = "-" * 60
    print(border)
    print("---- Marvellous Platform Surveillance System -----")
    print(border)

    # Support BOTH formats:
    # Old:  python Script.py 5 LogsFolder
    # New:  python Script.py LogsFolder receiver@gmail.com 10

    if len(sys.argv) == 2 and sys.argv[1].lower() in ("--h", "--help"):
        print("This script provides:")
        print("1) Thread Monitoring (PID, Name, Threads count)")
        print("2) Open Files Monitoring (Open files count + Access Denied handling)")
        print("3) Actual Memory Allocation (RSS, VMS, Memory % + Top 10 by RSS)")
        print("4) Periodic Email Reporting (log attachment + summary)")
        print("\nUsage:")
        print("A) python PlatformSurveillance.py <interval_minutes> <log_folder>")
        print("B) python PlatformSurveillance.py <log_folder> <receiver_email> <interval_minutes>")
        print("\nEmail setup (env vars):")
        print("PSS_SENDER_EMAIL=yourmail@gmail.com")
        print("PSS_SENDER_PASS=your_app_password")
        return

    if len(sys.argv) == 3:
        # Old format: interval, folder
        try:
            interval = int(sys.argv[1])
            folder = sys.argv[2]
        except ValueError:
            print("Invalid arguments. Use --h for help.")
            return

        receiver = None

    elif len(sys.argv) == 4:
        # New format: folder, receiver, interval
        folder = sys.argv[1]
        receiver = sys.argv[2]
        try:
            interval = int(sys.argv[3])
        except ValueError:
            print("Invalid interval minutes. Use --h for help.")
            return

    else:
        print("Invalid number of command line arguments.")
        print("Use: python PlatformSurveillance.py --h")
        return

    # Schedule the job
    schedule.every(interval).minutes.do(Job, folder, receiver)

    print("Platform Surveillance System started successfully")
    print("Log folder:", folder)
    if receiver:
        print("Receiver email:", receiver)
    print("Interval (minutes):", interval)
    print("Press Ctrl + C to stop")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()