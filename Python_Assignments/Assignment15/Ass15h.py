# filter() : numbers divisible by both 3 and 5
data = [ 15,10,40,45,30,35]
Result = list(filter(lambda No : (No % 3 == 0) and(No % 5 == 0),data))
print("output",Result)