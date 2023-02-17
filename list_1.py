

# n= int(input("Enter the number of inputs"))
# l=[]
# for i in range(n):
#     x=input("Enter any number: ")
#     l.append(x)

# print(l)
# print(max(l))
# print(min(l))
# l.sort()
# print(l)
# import math

# a=["5",6,7,8,9,"pop"]

# a.insert(math.floor((len(a)+1)/2), "Shishimaruuu")

# print(a)


# # Update

# a[5:7]=["Sinjo","Hattori"]
# print(a)

# # Delete Remove and Pop for deleting the values


# a=["Amt","baby","doll","me","soney", "di", "baby"]
# for i in range(len(a)):
#     if a[i]=="baby":
#         print(i)
        
# Multidimensional array (LIST inside LIST)

# a=[["Ram", 19, "pop"],["Shyam", 18, "push"]]

# a[0][0]= "Chuppa"
# # del a[1]
# b=a[0].pop(2)
# print(a)
# print(b)


a=[["Ram", 19, "pop"],["Shyam", 18, "push"],["Hari",15,"good"],["Hari"]]
name=input("Enter name to search: ")
for i in range(len(a)):
    for i in range(len(a)):
        if a[i][0]==name:
            print(i)