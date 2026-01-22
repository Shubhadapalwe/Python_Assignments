#reduce() : maximum element
from functools import reduce

Data = [10,45,32,67,55]
Result = reduce(lambda No1 ,No2 : No1 if No1 > No2 else No2,Data)

print("maximum from data is :",Result)