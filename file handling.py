# # file
# from ast import operator


# file = open'<file_name>','<mode>'
# # file.close()

# with open('<file_name>','mode')as file:
#     <operator>


# mode

# read -> r 
# write -> w 
# append -> a 
# creat -> x

# creat a file 
# file = open('data.txt','x')
# file.close()

# try:
#     file = open('data.txt','x')
#     file.close()
# except:
#     print('the file is aleady there')


# # # read a file 
# file = open('data.txt','r')
# x = file.read()
# print(x)
# file.close()
# # split the data 
# y = x.split('\n')
# print(y)
# print(y[1])

# write a,w
#  use w for write 

# file = open('data1.txt','w')
# file.write('Hello world I am keshav')

# file.close()




# s = str()
# grand_total = 0
# n = int(input("Enter n = "))
# for i in range(n):
#     name = input("Enter name = ")
#     price = int(input("Enter price = "))
#     quantity = int(input("Enter quantity = "))
#     total = price*quantity
#     info = f"{name} {price} {quantity} {total}\n"
#     s = s+info
   
# print(s)
# # print("Grand total = ",grand_total)
# file = open('data1.txt','w')
# file.write(s)
# file.close()


# s = str()
# grand_total = 0
# n = int(input("Enter n = "))
# for i in range(n):
#     name = input("Enter name = ")
#     price = int(input("Enter price = "))
#     quantity = int(input("Enter quantity = "))
#     total = price*quantity
#     info = f"{name},{price},{quantity},{total}\n"
#     s = s+info
# print(s)

# file = open('data2.csv','w')
# file.write('name,price,Quality,total\n')
# file.write(s)
# file.close()

#  a mean append {add more in that file }
# file = open('data2.csv','a')
# file.write('coke,120,5,600\n')
# file.close()

# file = open('data2.csv','a')
# file.write('name,price,Quality,total\n')
# n = int(input("Enter n = "))
# for i in range(n):
#     name = input("Enter name = ")
#     price = int(input("Enter price = "))
#     quantity = int(input("Enter quantity = "))
#     total = price*quantity
#     info = f"{name},{price},{quantity},{total}\n"

# file.write(info)
# file.close()

