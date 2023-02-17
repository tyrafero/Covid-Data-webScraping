# class Hello:
#     @staticmethod
#     def hello(): #can add any  thing
        
#         print("Hello World") 
        
# obj= Hello()
# obj.hello()


# class Cal:
#     def calv(self,l,b,h):
#         v= l*b*h
#         print(v)
#     def cala(self,l,b):
#         a=l*b
#         print(a)
# l=10
# b=5
# h=2
# obj=Cal()
# obj.calv(l,b,h)
# obj.cala(l,b)


# class Cal:
#     def __init__(self,l,b,h):
#         self.l=l
#         self.b=b
#         self.h=h
        
#     def calv(self):
#         v= self.l*self.b*self.h
#         print(v)
#     def cala(self):
#         a=self.l*self.b
#         print(a)
# l=10
# b=5
# h=2
# obj=Cal(l,b,h)
# obj.calv()
# obj.cala()

class Information:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(name, age, address)
    def __str__(self):
        return self.name
        
    def info(this):
        print(f"Hello I am {this.name} and {this.age} years old. I live in {this.address}")
    
obj= Information("Ram","45","Kathmandu")
obj.info()