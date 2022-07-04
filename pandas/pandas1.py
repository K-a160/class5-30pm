# try:
#     file = open('pandas1.csv','x')
#     file.close()
# except:
#     print('the file is already there.')

# import pandas as pd
# df = pd.read_csv('pandas1.csv')
# print(df)

# import pandas as pd
# df = pd.read_csv('pandas1.csv')
# print(df.head(4))


# import pandas as pd
# df = pd.read_csv('pandas1.csv')
# print(df.tail(3))


# import pandas as pd
# df = pd.read_csv('pandas1.csv',index_col='sn',usecols=['sn','name','age'])
# print(df)



# import pandas as pd
# df = pd.read_csv('pandas1.csv',index_col='sn',usecols=['sn','name','phone','add'])
# print(df)

# import pandas as pd
# df = pd.read_csv('pandas1.csv',index_col='sn')
# print(df.iloc[0:3,0:3])


# import pandas as pd
# df = pd.read_csv('pandas1.csv',index_col='name')
# print(df.loc['Shyam':'Nabin'])


# import pandas as pd
# df = pd.read_csv('pandas1.csv',index_col='sn')
# print(df['add']== 'Kathmandu')



# import pandas as pd
# df = pd.read_csv('pandas1.csv',index_col='sn')
# print(df[df['add']== 'Kathmandu'])

# import pandas as pd
# df = pd.read_csv('pandas1.csv',index_col='sn')
# print(df[(df['add'] == 'Kathmandu') | (df['phone'] == 98025145184)])

# import pandas as pd
# data = {'name':['ram','shyam','hari'],
#         'age':[35,25,45],
#         'add':['kathmandu','bhaktapur','lalitpur']}
# df = pd.DataFrame(data)
# print(df)
# df.to_csv('datas.csv')
# print(df)
