# class A:
#     pass
# class B(A):
#     pass
# obj = b()


# class A:
#     def __init__(self) -> None:
#         self.name = input("enter name = ")
#         self.age = int(input("Enter the age = "))
#         self.add = input("Enter the address = ")

# class B(A):
#     def info(self):
#         d = f"Hello World I am {self.name}.I am from {self.add}. I am {self.age}. "
#         print(d)
# obj = B()
# obj.info()




# class A:
#     def __init__(self,name,age,add) -> None:
#         self.name = name
#         self.age = age
#         self.add = add

# class B(A):
#     def info(self):
#         d = f"Hello World I am {self.name}.I am from {self.add}. I am {self.age}. "
#         print(d)


# name = input("enter name = ")
# age = int(input("Enter the age = "))
# add = input("Enter the address = ")
# obj = B(name,age,add)
# obj.info()


# class A:
#     def __init__(self,add) -> None:
#        self.add = add

# class B(A):
#     def __init__(self, name, age, add) -> None:
#         self.name = name
#         self.age = age
#         A.__init__(self,add)
        
#     def info(self):
#         d = f"Hello World I am {self.name}.I am from {self.add}. I am {self.age}. "
#         print(d)


# name = input("Enter name = ")
# age = int(input("Enter the age = "))
# add = input("Enter the address = ")
# obj = B(name,age,add)
# obj.info()



# multi level


# class A:
#     pass
# class B:
#     pass
# class C:
#     pass
# obj = c()

# Multiple

# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass
# obj = c()


# # multi-level
# class A:
#     def __init__(self,add) -> None:
#         self.add = add

# class B(A):
#     def __init__(self,age, add) -> None:
#         self.age = age
#         A.__init__(self,add)
# class C(B):
#     def __init__(self, name, age, add) -> None:
#         self.name = name
#         B.__init__(self,add,age)

#     def info(self):
#         d = f"Hello World I am {self.name}.I am from {self.add}. I am {self.age}. "
#         print(d)


# name = input("Enter name = ")
# age = int(input("Enter the age = "))
# add = input("Enter the address = ")
# obj = C(name,age,add)
# obj.info()



# class A:
#     def __init__(self,add) -> None:
#         self.add = add

# class B():
#     def __init__(self,age,) -> None:
#         self.age = age
        
# class C():
#     def __init__(self, name) -> None:
#         self.name = name

# class D(A,B,C):
#     def __init__(self, name, age, add) -> None:
#         A.__init__(self,add)
#         B.__init__(self,age)
#         C.__init__(self,name)


#     def info(self):
#         d = f"Hello World I am {self.name}.I am from {self.add}. I am {self.age}. "
#         print(d)


# name = input("Enter name = ")
# age = int(input("Enter the age = "))
# add = input("Enter the address = ")
# obj = D(name,age,add)
# obj.info()


