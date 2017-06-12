import pandas as pd
from datetime import datetime
start=datetime.now()
excep = []
df = pd.read_csv('sample_input.csv',encoding='ISO-8859-1')

def score(w,a):
    w = w.lower()
    a = a.lower()

for idx,each in df.iterrows():
    print idx
    try:
        score(each['walmart'],each['amazon'])
    except Exception,e:
        print e
        continue
        print each_url['s.no']
pd.DataFrame(excep,columns=['exception']).to_csv('exception1.csv',encoding='utf8',header=False)

print "Scraped pages:",(len(df)-len(excep))
print "Error pages:",len(excep)
print datetime.now()-start