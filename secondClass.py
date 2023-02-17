# Compare length of given string #

name1=input("enter 1st name\t")
name2=input("enter 2nd name\t")


if len(name1)==len(name2):
    print(name1,name2+""+": Lenght of alphabets are identical")
elif len(name1)>len(name2):
    print(name1+">"+name2)
elif len(name1)<len(name2):
    print(name1+"<"+name2)
else:
    print(name1+"!="+name2)
    
    
#####################################################################    
num1= int(input("Enter 1st number to compare"))
num2= int(input("Enter 2nd number to compare"))

######### Comparing Number with num1 and num2 #######
if num1>0:
    if num1==num2:
        print("Numbers are positive and identical")
    if num1>num2:
        print("Number 1 is positive and greater than Number 2")
    if num1<num2:
        print("Number 2 is positive and greater than Number 1")
if num1<0:
    if num1==num2:
        print("Numbers are negative and identical")
    if num1>num2:
        print("Number 1 is negtive and greater than Number 2")
    if num1<num2:
        print("Number 2 is negative and greater than Number 1")

else:
    print("Invalid Inputs")

# Area OF Circle
r= float(input("enter the radius:  "))
pi= 3.14

area= pi*(r**2)

print("The area of circle with radius  "+ str(r) +"cm is "+ str(area)+"cm2")