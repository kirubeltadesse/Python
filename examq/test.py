import pandas as pd
import numpy as np

path = '/home/aniekan/Downloads/numbers2.csv'
k = pd.read_csv(path, index_col = 0,  header = None)
print(k.index.tolist())
print(k.idxmax())
k.info()
#print(len(k))
#for i, row in k.iterrows():
#    print(i)

#for i in k:
#s = pd.Series(k, index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
#print(s)
#for i in k:
df = pd.DataFrame.idxmax(k)
print ("Here is ")
print (df)
df.head()
df.tail(1)
#df
