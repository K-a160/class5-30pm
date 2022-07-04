# ##function
#  print()
# type()
# str() int() float()
# list()
# tuple()
# dict()



# def<function_name>():  #defining
#     <operator>
# <function_name>() #calling

# def hello():
#     print("hello world")
# hello()
# hello()

# def area():
#     l = int(input("enter the length"))   ##local variable
#     b = int(input("enter the bredth"))     ##local variable
#     a = l*b                                ##local variable
#     print(a)
# area()


# def area(): 
#     a = l*b                                ##localvariable
#     print(a)

# l = int(input("enter the length"))   ##global variable
# b = int(input("enter the bredth"))   ##global variable 
# area()


# argument and return type

# def hello(x):          #parameter
#     print(x)
# hello("hello world")   #argument

# def area(l,b):       #parameter
#     a = l*b                                ##localvariable
#     print(a)

# l = int(input("enter the length"))   ##global variable
# b = int(input("enter the bredth"))   ##global variable 
# area(l,b)                            #argument

# def area(x,y):                           #parameter
#     a = x*y                                ##localvariable
#     print(a)

# l = int(input("enter the length"))   ##global variable
# b = int(input("enter the bredth"))   ##global variable 
# area(l,b)                            #argument

# def area(x,y):       #parameter
#     a = x*y                             ##localvariable
#     print(a)
# def volume(x,y,z):
#      v =x*y*z
#      print(v) 
# l = int(input("enter the length"))   ##global variable
# b = int(input("enter the bredth"))   ##global variable
# h = int(input("enter the height")) 
# volume(l,b,h)                    #argument
# area(l,b)                            #argument


# def info(l):
#     info = f"Hello world I am {l[0]}.  I am from {l[2]}. i am {l[1]}"
#     print(info)

# name = (input("enter the name = "))
# age = int(input("enter the age = "))
# add  = input("enter the address = ")

# l = [name,age,add]
# info(l)

# def info(d):
#     infos = f"Hello world I am {d['name']}. I am from {d['add']}. i am {d['age']}"
#     print(infos)

# name = (input("enter the name = "))
# age = int(input("enter the age = "))
# add  = input("enter the address = ")

# d = {"name":name,"age":age,"add":add}
# info(d)




# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def div(a,b):
#     print(a/b)
# def cal(a,b,o):


#     if o == "+":
#         add(a,b)
#     elif o == "-":
#         sub(a,b)
#     elif o == "*":
#         mul(a,b)
#     elif o == "/" :
#         if(b!=0):
#          div(a,b)
#         else:
#          print("The value of b cannot be Zero")
#     else:
#         print("invalid opreter")
# a = int(input("Enter a = "))
# b = int(input("Enter b = "))
# o = input("Enter +  or - or * or /")

# cal(a,b,o)

