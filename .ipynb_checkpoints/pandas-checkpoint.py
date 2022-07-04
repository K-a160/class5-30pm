try:
    file = open('pandas.csv','x')
    file.close()
except:
    print('the file is already there.')

import pandas as pd
df = pd.read_csv('pandas.csv',index_col='sn')
print(df)

df.head(4)

df.tail()
