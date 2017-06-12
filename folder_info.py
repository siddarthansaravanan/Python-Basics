import os
import time
import pandas
from os.path import join, getsize
y = [x[0] for x in os.walk('folder')]
modified_time = []
file_size = []
for xy in y:
    modified_time.append(time.ctime(max(os.path.getmtime(root) for root,_,_ in os.walk(xy))))
    file_size.append(getsize(xy))
data = pd.concat((pd.DataFrame(y,columns=['Dictionary']),pd.DataFrame(modified_time,columns=['Modified Time']),pd.DataFrame(file_size,columns=['File Size'])),axis=1)