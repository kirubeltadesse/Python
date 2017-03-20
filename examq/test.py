import pandas as pd
import numpy as np

path = '/home/aniekan/Downloads/numbers.csv'
k = pd.read_csv(path, header = None)
print(k)
k.info()
#print(len(k))
#for i, row in k.iterrows():
#    print(i)

#for i in k:
#s = pd.Series(k, index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
#print(s)
#for i in k:
df = pd.DataFrame.idxmax(k)
df2 = pd.DataFrame.tail(1)
#df
