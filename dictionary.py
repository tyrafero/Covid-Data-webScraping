# University of Michigan ma sodheko question

# bill= {"sn":[], "product":[], "price":[], "quantity":[],"total":[] }

# c= int(input("Enter c="))
# for i in range(1,c+1):
#     name=input("Name: ")
#     quantity=int(input("Quantity: "))
#     price=int(input("Price: "))
#     total=price*quantity
    
#     bill["sn"].append(i)
#     bill["product"].append(name)
#     bill["price"].append(price)
#     bill["quantity"].append(quantity)
#     bill["total"].append(total)

# print(bill)

L=[]
c=int(input("Enter value of C: "))

for i in range(c):
    name=input("Name: ")
    quantity=int(input("Quantity: "))
    price=int(input("Price: "))
    total=price*quantity
    
    d={"sn":i, "product":name, "quantity":quantity, "price":price, "total":total}
    
    L.append(d)
print(L)