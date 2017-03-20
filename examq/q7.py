import pandas as pd
import numpy as np

path = '/home/aniekan/Downloads/numbers.csv'
k = pd.read_csv(path, header = None)
#print(k)
#print(len(k))
#for i, row in k.iterrows():
#    print(i)

#for i in k:
#s = pd.Series(k, index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
#print(s)
df = pd.DatarFrame(k)
df
