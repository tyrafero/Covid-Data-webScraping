# file= open("< File name>","<mode>")
# file.close()
# here file is an object
# object holds operations


# Modes:
#     r= read
#     w= write
#     a= append
#     x= create
    
# with open("< File name>","<mode")as file:
#     <operations>

# with open("data.txt","r") as file:

file= open("data.csv","x")
print(file.read())
file.close()