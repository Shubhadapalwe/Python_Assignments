# filter() : strings length > 5
Data = ["India", "Python", "Marvellous", "AI", "Machine","Shubhada","Ganpati","Bappa"]
Result = list(filter( lambda s : len(s) > 5 , Data))
print("Output is :",Result)