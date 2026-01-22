from functools import reduce

Data = [1, 2, 3, 4, 5]

Result = reduce(lambda A, B: A + B, Data)

print("Output:", Result)