# class Data:                                                        #Parent
#     def __init__(self):
#         self.name = input("Enter name:  ") 
#         self.age = input(f"Enter {self.name}'s age: ") 
        
# class Info(Data):                                                  #Child
#     def info(self):
#         print(self.name, self.age) 
        
# obj=Info()
# obj.info() 

# 
# Privat Protected Public

# Public

# class Info:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# obj=Info("Rma", 45)
# print(obj.name, obj.age)


# Protected
# class Info:
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age

# obj=Info("Rma", 45)
# print(obj._name, obj._age)


# Private Doesn't run
# class Info:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age

# obj=Info("Rma", 45)
# print(obj.__name, obj.__age)



#Private 

# class Data:                                                        #Parent
#     def __init__(self):
#         self.name = input("Enter name:  ") 
#         self.__age = input(f"Enter {self.name}'s age: ") 
        
# class Info(Data):                                                  #Child
#     def info(self):
#         print(self.name) 
        
# obj=Info()
# obj.info() 



# Protected
# class Data:                                                        #Parent
#     def __init__(self):
#         self.name = input("Enter name:  ") 
#         self.__age = input(f"Enter {self.name}'s age: ") 
        
# class Info(Data):                                                  #Child
#     def info(self):
#         print(self.name) 
        
# obj=Info()
# obj.info()


# Using Private members

# class Age:
#     def __init__(self, age):
#         self.__age= age
#     def Age(self):
#         print(self.__age)

# class Data:
#     def __init__(self, name):
#         self.name= name
#     def data(self):
#         print(self.name)
# class Info(Age,Data):
#     def __init__(self, name,age,add):
#         self.__add= add
#         Data.__init__(self.name)
#         Age.__init__(self.age)
        
#     def info(self):
#         print(self.name, self.__add)
        
# name=input("Name: ")
# age=int(input("Age: "))
# phone=input("Phone: ")

# obj= Info(name,age,phone)
# obj.info()        


# Name membling: Accessing private attributes outside the class. The process is as follows:
# __name => _Class__name
# We can use private attributes by changing it into public attribute by add class before it for checking purposes.