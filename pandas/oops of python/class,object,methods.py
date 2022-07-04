### class <class_name>:
# ##    <methods>
#   ##  <attributes>

# ##obj = <class_name>()


# class Hello:              #class
#     print("hello world")
# obj = Hello()             #object



# class Hello:  
#     def hello(self):           
#      print("hello world")
# obj = Hello()           
# obj.hello()

# class cal:
#     def area(self):
#         l= 10
#         b = 2
#         a = l*b
#         print(a)
#     def volume(self):
#         l = 20
#         b = 10
#         h = 2
#         v = l*b*h
#         print(v)
# obj = cal()
# obj.area()
# obj.volume()

# class cal:
#     def area(self):
#         l= int(input("enter the length"))
#         b = int(input("enter the bredth"))
#         a = l*b
#         print(a)
#     def volume(self):
#         l = int(input("enter the length"))
#         b = int(input("enter the bredth"))
#         h = int(input("enter the height"))
#         v = l*b*h
#         print(v)
# obj = cal()
# obj.area()
# obj.volume()

# class cal:
#     def area(self,l,b):
#         a = l*b
#         print(a)
#     def volume(self,l,b,h):
#         v = l*b*h
#         print(v)
# obj = cal()
# obj.area(10,5)
# obj.volume(10,5,2)

# class Cal:
#     def cal(self,l,b,h):
#         a = l*b
#         v = a*h
#         return a,v

# obj = Cal()
# obj.cal(10,5,2)

# class Cal:
#     def __init__(self,l,b,h):
#         self.l = l
#         self.b = b
#         self.h = h
#     def area(self):
#         a = self.l*self.b
#         print(a)
#     def volume(self):
#         v = self.l*self.b*self.h
#         print(v)


# obj = Cal(10,5,2)
# obj.area()
# obj.volume()

# class Area:
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b
#     def area(self):
#         a = self.l*self.b
#         print(a)

# class Volume:
#     def __init__(self,l,b,h):
#         self.l =l
#         self.b = b
#         self.h = h
#     def volume(self):
#         v = self.l*self.b*self.h
#         print(v)

# obj1 = Area(10,5)
# obj2 = Volume(10,5,2)
# obj1.area()
# obj2.volume()

# class Information:
#     def __init__(self):
#         self.name = input("enter name = ")
#         self.age =int(input("enter age = "))
#         self.add = input("enter address = ")
#     def info(self):
#         return self.name
#     def __str__(self) -> str:
#         return self.name
# obj = Information()
# print(obj.info(),type(obj.info))
# print(obj,type(obj))
