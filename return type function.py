# return type function


#  function with no argument with return type
# def hello():
#     x = "hello world"
#     return x 
# print(hello())

# def cal():
#     l = 2
#     b = 3
#     a = l*b
#     return a 
# print(cal()) # or print(a)


# def cal():
#     l = 2
#     b = 3
#     a = l*b
#     return a 
# x = cal()
# h = 6
# v = x*h
# print("the volume = ", v)


# def cal():
#     l = int(input("enter the length = "))
#     b = int(input("enter the bredth = "))
#     a = l*b
#     return a 

# x = cal()
# h = int(input("enter the height = "))
# v = x*h
# print("the volume = ", v)




# def cal():
#     l = int(input("enter the length = "))
#     b = int(input("enter the bredth = "))
#     a = l*b
#     return a 
# print("area = ", cal())
# x = cal()
# h = int(input("enter the height = "))
# v = x*h
# print("the volume = ", v)



# def cal(l,b):

#     a = l*b
#     return a 

# l = int(input("enter the length = "))
# b = int(input("enter the bredth = "))
# h = int(input("enter the height = "))
# x = cal(l,b)

# v = x*h
# print("the volume = ", v)

#  function with  argument with return type
# def cal(l,b,h):

#     a = l*b
#     v = a*h
#     return a,v

# l = int(input("enter the length = "))
# b = int(input("enter the bredth = "))
# h = int(input("enter the height = "))
# x = cal(l,b,h)

# area , volume = x
# print( "the area is ", area)
# print("the volume is ",volume)


# def add(a,b):
#     return(a+b)
# def sub(a,b):
#     return(a-b)
# def mul(a,b):
#     return(a*b)
# def div(a,b):
#     return(a/b)
# def cal(a,b,o):

#     if o == "+":
#        print(add(a,b))
#     elif o == "-":
#         print(sub(a,b))
#     elif o == "*":
#         print(mul(a,b))
#     elif o == "/" :
#         if(b!=0):
#          print(div(a,b))
#         else:
#          print("The value of b cannot be Zero")
#     else:
#         print("invalid opreter")
# a = int(input("Enter a = "))
# b = int(input("Enter b = "))
# o = input("Enter +  or - or * or /")

# cal(a,b,o)

# def area(l,b):

#     a = l*b
#     return a 
# def volume(l,b,h):
#     v = area(l,b)*h
#     print("the volume = ", v)
# l = int(input("enter the length = "))
# b = int(input("enter the bredth = "))
# h = int(input("enter the height = "))
# volume(l,b,h)


# def area(l,b):

#     a = l*b
#     return a 
# def volume(l,b,h):
#     v = area(l,b)*h
#     return v
# l = int(input("enter the length = "))
# b = int(input("enter the bredth = "))
# h = int(input("enter the height = "))
# volume(l,b,h)
# print("the volume = ", volume(l,b,h))
# print("the area is ",area(l,b))

# ## recursive function

# def hello():
#     print("hello world")
    
# print(hello())



# def hello():
#     print("hello world")
#     hello()      ##recursion
# print(hello())


# def hello():
#     print("hello world")
#     x = input( "enter y for more print = ")
#     if x == 'y':
#        hello()      ##recursion
# print(hello())


# def hello():
#     p = int(input("enter the p = "))
#     t = int(input("enter the t = "))
#     r = int(input("enter the r = "))

#     i = p*t*r/100
#     print(i)
#     x = input( "enter y for more print = ")
#     if x == 'y':
#        hello()      ##recursion
# print(hello())