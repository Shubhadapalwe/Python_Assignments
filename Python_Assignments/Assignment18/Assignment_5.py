from functools import reduce

def IsPrime(No):
    if No <= 1:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def PrimeDoubleMax(Data):
    FData = list(filter(IsPrime, Data))                      # primes
    MData = list(map(lambda No: No * 2, FData))              # double
    RData = reduce(lambda A, B: A if A > B else B, MData)    # max
    return FData, MData, RData

def main():
    Data = [2, 70, 11, 10, 17, 23, 31, 77]
    FData, MData, RData = PrimeDoubleMax(Data)

    print("Input List:", Data)
    print("List after filter:", FData)
    print("List after map:", MData)
    print("Output of reduce:", RData)

if __name__ == "__main__":
    main()