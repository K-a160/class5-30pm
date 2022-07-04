# import pandas as pd
# data = {
#          'name':['ram','shyam','hari'],
#         'age':[35,25,45],
#         'add':['kathmandu','bhaktapur','lalitpur']}
# df = pd.DataFrame(data)
# print(df)
# df.to_csv('datas.csv')
# print(df)

# import pandas as pd
# df = pd.read_csv('datas.csv',index_col='sn')
# print(df)


# import csv
# data = ['sn','sabin','kathmandu']
# file = open('datas1.csv','w')
# x = csv.writer(file)
# x.writerow(data)
# file.close()

# import csv
# data = [[1,'sabin','kathmandu'],
#         [2,'Rabin',67,'lalitpur'],
#         [3,'sita',65,'bhaktapur']]
# file = open('datas1.csv','w')
# x = csv.writer(file)
# for i in data:
#     x.writerow(i)
# file.close()

# ###Dict writer

# import csv

# from nbformat import write
# csv_columes = ['Name','Age','Adds']
# dict = [
#         {'Name':'Ayush','Age':23,'Adds':'Kathmandu'},
#         {'Name':'Ram','Age':33,'Adds':'patan'}
# ]
# csvfile = open('datas3.csv','w')
# writer = csv.DictWriter(csvfile, fieldnames=csv_columes)
# writer.writeheader()
# for data in dict:
#     writer.writerow(data)
# csvfile.close()
#

# import csv
# # with open('datas3.csv') as csvfile:   
# csvfile = open('datas3.csv')
# reader = csv.DictReader(csvfile)
# for row in reader:
#   print(row)  #print(dict(row))



        
# import pandas as pd
# df = pd.read_csv('datas3.csv',index_col='sn')
# print(df.drop['Ram'],axis = 0)
# df = pd.read_csv('datas3.csv',index_col='sn')
# print(df.drop['Ram'],axis = 1)