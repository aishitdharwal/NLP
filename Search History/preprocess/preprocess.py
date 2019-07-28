#!/usr/bin/env python
# coding: utf-8

# In[195]:


import json

everything = json.loads(open('data.json').read())


# In[196]:


everything[0]['content'][0]


# C:/Users/DELL.india/Desktop/activity/data2.json

# In[197]:


print(everything[0])
print(everything[1])


# In[198]:


everything[0]['time']


# In[199]:


len(everything)


# In[200]:


j=0
empty_indices=[]
for i in range(len(everything)):
    if everything[i]['content']==[]:
#         empty_indices=empty_indices+(str(i))
        empty_indices.append(i)
#         print(list(str(i)))
        j=j+1

print(j,empty_indices)
print(len(empty_indices))
# print(j)


# In[201]:


def minus1():
    for i in range(len(empty_indices)):
        empty_indices[i]=empty_indices[i]-1


# In[202]:


for i in empty_indices:
    del everything[i]
    minus1()


# In[203]:


len(everything)


# In[204]:


content=[]
for i in range(len(everything)):
    content=content+list(everything[i]['content'])


# In[205]:


len(content)


# In[206]:


content


# In[207]:


for i in range(len(everything)):
    del everything[i]['time'][0]


# In[208]:


time=[]
for i in range(len(everything)):
    time=time+list(everything[i]['time'])


# In[209]:


len(time)


# In[210]:


time[0]


# In[211]:


from datetime import datetime
t1=datetime.strptime('May 17, 2019, 3:50:43 PM UTC', '%b %d, %Y, %I:%M:%S %p %Z')
t2=datetime.strptime('May 17, 2019, 3:40:43 PM UTC', '%b %d, %Y, %I:%M:%S %p %Z')
print(t2.minute-t1.minute)


# In[212]:


def diffunder60mins(t1,t2):
    y2=t2.year
    M2=t2.month
    d2=t2.day
    h2=t2.hour
    m2=t2.minute
    y1=t1.year
    M1=t1.month
    d1=t1.day
    h1=t1.hour
    m1=t1.minute
    if(y1==y2 and M1==M2 and d1==d2):
        if(abs(m2-m1+60*(h2-h1))>=60):
            return False
        else:
            return True
    else:
        return False


# In[213]:


diffunder60mins(t1,t2)


# In[214]:


time_objects=[]
for i in range(len(time)):
    time_objects.append(datetime.strptime(time[i], '%b %d, %Y, %I:%M:%S %p %Z'))


# In[215]:


time_objects[0].hour


# In[216]:


session_number=[0]
l=len(time_objects)
j=0
for i in range(1,l):
    if(diffunder60mins(time_objects[i-1],time_objects[i])==True):
        session_number.append(j)
    else:
        j=j+1
        session_number.append(j)


# In[217]:


len(session_number)


# In[218]:


session_number


# In[219]:


session_number[-1]


# In[220]:


sessions=[]
session=[[content[0],time[0]]]
print(session)
k=session_number[0]
# print(k)
for i in range(1,len(content)):
    if(session_number[i]!=k):
        k=session_number[i]
        sessions.append(session)
        session=[]
    if(session_number[i]==k):
        session.append([content[i],time[i]])
if(session!=[]):
    sessions.append(session)


# In[221]:


print(sessions)


# In[222]:


len(sessions)


# In[223]:


sessions[0]


# In[230]:


sessions[10]


# In[ ]:




