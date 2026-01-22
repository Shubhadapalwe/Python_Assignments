# reduce() :
from functools import reduce

Data = [10,45,32,67,55]
Result = reduce(lambda No1 ,No2 : No2 if No1 >  No2 else No1,Data)

print("minimum from data is :",Result) 