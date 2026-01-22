# # filter() : list of odd numbers
Data = [ 2,3,4,5,6,7,8,9,12,13]
Result = (list(filter(lambda No :  No % 2 != 0 ,Data )))
print("odd numbers from list are:",Result)