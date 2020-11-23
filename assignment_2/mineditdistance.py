#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np

def editDis(tar,src):
    
    
    target=[]
    for j in tar:   
        target.append(j)
        
        
   
    source=[]
    for j in src:   
        source.append(j)
   
    
    grid=np.zeros((len(source),len(target)))
    
    grid[0,:]=[i for i in range (len(target))]
    
    grid[:,0]=[k for k in range (len(source))]
   
           
    for i in range(1,len(target)):
        for j in range(1,len(source)):
            if target[i] != source[j]:
                grid[j,i]=min(grid[j-1,i],grid[j,i-1])+1
                
            else:
                    grid[j,i]=grid[j-1,i-1]
                    
                    
    return np.flip(grid, 0)
                
    



# In[36]:



inp=open("input.txt")
inptxt=inp.read()
i=inptxt.splitlines()
print(i[0])
print(i[1])

target=i[0]
source=i[1]
a=editDis(target,source)
print("minimum edit distance : {}".format(a[0][len(target)-1]))
print(a)


# In[ ]:




