# a="mr. "
# b="bean"
# c=a+b
# print(c)



# for i in c:
#     print(i)
    
# # String Slicing


# a="Hello World"
# print(a[1])
# print(a[0:5])
# print(a[0:12:2])
# # String Reversing
# print(a[-1::-1])
# print(a[::-1])
    
#Palindrome 

# a=input("Enter the value a:")

# if a==a[::-1]:
#     print("Word is palindrome: ",a)
# else:
#     print("Word is not palindrome")


# name=input("Enter the name: ")
# age=int(input("Enter the age: "))
# add= input("Enter the address: ")

# print(f"My name is {name} and {age} years old. I live in {add}")


# Billing System
# a=int(input("Enter number of particulars"))
# bill=""
# for i in range(a):
#     name= input("Enter the name of product: ")
#     price= int(input(f"Enter price of {name}: "))
#     quantity= int(input(f"Enter quantity of {name}: "))
#     total= price*quantity
  
#     bill= bill+ f"{name}\t {price}\t {quantity}\t {total}\t\n"
    
    
# print("Name\t", "Price\t", "Quantity\t", "Total\t")  
# print(bill)
# Immutable Datatype

# Search
# a= "Ram Shyam Hari Geeta Ravi Mami Dami Sami Gami Lami"
# a= a.lower()
# name= input("Enter a name to check in list: ")
# print(a.count(name))
# if name in a:
#     print("Yes, there is ", name)
# else:
#     print("No, there is no ", name)



# Replace
a= "Ram Shyam Hari Geeta Ravi Mami Dami Sami Gami Lami".split()
# a=a.replace("Ram","Rama")
print(a)
