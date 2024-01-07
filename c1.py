c=0
c1=0
c2=0
"""initialising the variables"""
import re
"""importing the regular expressions module"""
import pandas as pd
"""importing the pandas module"""
log=pd.read_csv('logfile.txt',sep=' ',header=None)
"""given text file is read using pandas"""
a=log[1]
"""the 2nd columnn of the log file is considered to identify which is in waiting state,scheduled state and running state"""
for i in range(0,20):
    b=a.iloc[i]
    pattern='^\d'
    result=re.match(pattern,str(b))
    """regular expressions is used to determine the scheduled states because it contains different numbers for each line"""
    if result:
        c2+=1
    elif b=='waiting':
        c1+=1
    else:
        c+=1
print('Waiting state:',c1)
print('Scheduled state:',c2)
print('Running state:',c)

