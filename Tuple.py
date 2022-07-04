# #  Tuple 
# # indexed
# # ordered 
# # mulpiple data
# # Imutable


# a = ("apple","ball","cat")
# b = (1,2,3,4,5,6,7,8,9)
# print(a)
# print(type(a))
# print(b)
# print(type(b))


# a = ("apple","ball","cat")
# print(a[2])



# a = ("apple","ball","cat")
# b = (1,2,3,4,5,6,7,8,9)
# c = a+b
# print(c)


# b = (1,2,3,4,5,6,7,8,9)
# print(max(b))
# print(min(b))
# print(sum(b))
#  in tuple no apped() , insert(), extend sort()
# no update
# no del pop() remove()


# a = ()
# b = a+(1,)
# c = b+(2,)
# d = c+(3,)
# print(d)

# t = tuple()
# n = int (input("enter n = "))
# for i in range(n):
#     x = input("enter x= ")
#     t = t+(x,)
#     print(t)


#  we can  change tuple to list and reverse
# a = ("apple","ball","cat")
# b = list(a)
# print(b)
# del b[1]
# a = tuple(b)
# print(a) 

# a = "hello world" #we can also change 
# print(list(a))
#print(tuple(a))


## tuple inside tuple
# a = (("Ram",34,"kathmandu"),
#     ("shyam",24,"lalitpur"),
#     ("Hary",65,"bhaktapur"))
# print(a)

# t = ()
# n = int(input("enter n = "))
# for i in range(n):
#     name = input("enter name")
#     age = int(input("enter the age"))
#     add = input("enter the adderess")
#     info = ((name,age,add),)
#     t = t+info
# print(t)

# # tuple inside list
# a = (('k', 25, 'kk'),("pp",25,"pk"))
# b = list(a)
# print(b)

# #  we can also insert tuple inside of list
# b.append(("ram",25,"ktm"))
# print(b)


# #  from tuple inside tuple to list inside list

# c = []
# a = (('k', 25, 'kk'),("pp",25,"pk"))
# for i in a:
#     x = list(i)
#     c.append(x)
# print(c)