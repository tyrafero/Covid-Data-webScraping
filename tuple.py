a=(1,2,3,4)
# if a=(1) then its int If a=(1,) then its tuple
# Tuple is a light weight data type
# Concatenation is possible 
# max min sum and sorted can be used
# Sorted turns tuple into list
b=list(a)
print(b)
del b[0]
b=tuple(a)
print(b)
reversed(b)
print(b)