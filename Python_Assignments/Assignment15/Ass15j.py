# filter() : count of even numbers
Data = [12,5,44,33,32,56,76,78,88,11]
Result = list(filter(lambda No : No % 2 == 0,Data))
print("the count of Even numbers :",len(Result))
