# reduce() : product of all elements
from functools import reduce
data = [ 1,4,5,3,7,10]
Result = (reduce(lambda No1 ,No2 : No1 * No2,data))
print("product of all numbers/elements ",Result)