# for i in range(0,5):
#     for j in range(0,i+1):
#         print("👉",end=" ")
    
#     print("\r")
    
######################Multiplcation table################################################################


# n=int(input("Value of n"))
# for i in range(0,11):
#     print(n,"*",i,"=",n*i)
    
# s=[]
# c=int(input("Value of c: "))
# for i in range(c):
#     n=input("Value of n: ")   
#     s.append(n)
# print(s)
#




#Factorial
# s=1
# n=int(input("Value"))
# for i in range(1,n+1):
#     s=s*i
# print(s)

#Wap to calculate the sum of the numbers from n1 to n2

# n1=int(input("Value of n1: "))
# n2=int(input("Value of n2: "))

# s=0
# m=1

# for i in range(n1,n2+1):
#     s=s+i
#     m=m*i
# print(s)
# print(m)

text= input("Enter plain text")
s=int(input("Value of s: "))
res=""

def encrypt(text,s):
    res=""
   # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        
        if (char.isupper()):
            res += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            res += chr((ord(char) + s - 97) % 26 + 97)
        return res
#check the above function
# text = "CEASER CIPHER DEMO"
# s = 4

print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher: " + encrypt(text,s))