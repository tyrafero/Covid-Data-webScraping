# a="python"
# for i in range(len(a)-1,-1,-1):
#     print(a[i],end="-")
    
    
# Removing spaces in string

# a="Hello I am python"

# for i in a:
#     if (i!=" ") or (i!="."):
#         print(i,end="")
        


# Control Statements:
# break
# continue
# pass

# for i in range(10):
#     if i==5:
#         continue
    
#     if i==8:
#         continue
#     print(i,end="*")
# a="hey you there. Can you think about me?"
# for i in a:
#     if i==".":
#         print(i,end="")
#         break
#     print(i,end="")
    

# WAP to check if given number is prime

# n= int(input("Enter a number"))
# is_prime= True
# for i in range(2,n):
#     if n%i==0:
#         is_prime= False
# if is_prime==True:
#     print("Its prime")
# else:
#     print("Its not prime")


#Using for else loop to find prime number:

# for i in range(2,n):
#     if n%i==0:
#         print(f"Its composite: {str(n)}")
#         break
# else:
#     print(f"Its prime: {str(n)}")


# a=1
# while a<5:
#     print("Hello, World")
#     a=a+1
# n=int(input("Please enter any number to genrate its multiplcation table: "))
# b=1
# while b<=10:
#     print(n,"*",b,"=",n*b)
#     b=b+1


# c=int(input("Please enter numbers to add"))

# s=0
# i=1

# while i<c:
#     n=int(input("Please enter any number to add: "))
#     s=s+n
#     i=i+1

# print("Total sum: ",s)

# c=int(input("Please enter number"))
# i=1
# s=0
# m=1
# while i<=c:
#     s=s+i
#     m=m*i
#     i=i+1

# print(s,m)

# n1=int(input("Please enter number: "))
# n2=int(input("Please enter another number: "))
# s=0
# m=1
# while n1<=n2:
#     s=s+n1
#     m=m*n1
#     n1=n1+1
# print(s,m)


# n=int(input("Please enter a number to check: "))
# i=2
# is_prime=True
# while i<n:
#     if n%i == 0:
#         is_prime=False
#     i=i+1
# if is_prime==False:
#     print("Not prime")
# else:
#     print("Prime")


# a=0
# while a<5:
#     if  a==4:
#         break
#     print(a)
#     a=a+1

n=int(input("Please enter a number: "))
i=2
while i<n:
    if n%i==0:
        print(f"Its composite: {str(n)}")
        break
    i=i+1
else:
    print(f"Its prime: {str(n)}")
    
