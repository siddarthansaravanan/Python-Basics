import pandas as pd
import re
abc = pd.read_csv("input.csv")
l1=[]
for i in abc.Header:
    i=i.lower()
    lr = re.compile(r'pattern') 
    lx = lr.findall(i)
    l1.append(lx)
    print lx
    
pd.DataFrame(l1).to_csv('Output.csv')