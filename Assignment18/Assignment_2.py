# filter (70 to 90) -> map(+10) -> reduce(product)
#   Input list: [4,34,36,76,68,24,89,23,86,90,45,70]
#   Filter: [76,89,86,90,70]
#   Map: [86,99,96,100,80]

from functools import reduce
def ProcessList(Data):
   FData = list(filter(lambda No : 70<= No or 90<=No,Data ))
   MData = list(map(lambda No : No + 10, FData))
   RData = reduce(lambda A,B: A*B,MData)
   return FData,MData,RData
def main():
    Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    print("Input list :",Data)

    FData, MData, RData = ProcessList(Data)

    print("List after filter:", FData)
    print("List after map:", MData)
    print("Output of reduce:", RData)

if __name__ =="__main__":
    main()