# filter(even) -> map(square) -> reduce(addition)
from functools import reduce

def EvenSquareSum(Data):
    FData = list(filter(lambda No: No % 2 == 0, Data))      # even
    MData = list(map(lambda No: No * No, FData))            # square
    RData = reduce(lambda A, B: A + B, MData)               # sum
    return FData, MData, RData

def main():
    Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    FData, MData, RData = EvenSquareSum(Data)

    print("Input List:", Data)
    print("List after filter:", FData)
    print("List after map:", MData)
    print("Output of reduce:", RData)

if __name__ == "__main__":
    main()