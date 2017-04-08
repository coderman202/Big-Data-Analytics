
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[4]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[5]:

s


# In[6]:

s.index


# In[7]:

pd.Series(np.random.randn(15))


# In[8]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[10]:

pd.Series(d)


# In[11]:

d2 = {'a' : 0.5, 'b' : 3.4, 'c' : 2.7}


# In[12]:

pd.Series(d)


# In[13]:

pd.Series(d, d2)


# In[14]:

d2


# In[15]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[16]:

pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])


# In[17]:

pd.Series(5., index=[10])


# In[18]:

pd.Series(5, index=['a', 'b', 'c', 'd', 'e'])


# In[19]:

pd.Series(5.235698755986587455884569, index=['a', 'b', 'c', 'd', 'e'])


# In[20]:

s[0]


# In[21]:

s


# In[22]:

s[4-3]


# In[23]:

s[a]


# In[24]:

s['a']


# In[25]:

s[:3]


# In[26]:

s[3:]


# In[27]:

s[s > s.median()]


# In[28]:

s[[4, 3, 1]]


# In[29]:

s[[4, 3, 1, 4, 1, 3]]


# In[30]:

np.exp(s)


# In[31]:

s['e'] = 12


# In[32]:

s


# In[33]:

'e' in s


# In[34]:

'f' in s


# In[35]:

12 in s


# In[36]:

1 in s


# In[37]:

s.get('f')


# In[38]:

s.get('f', np.nan)


# In[39]:

if 'e' in s: print(s['e'])


# In[41]:

s.get('e')


# In[43]:

s.get('e', 'c')


# In[44]:

s + s


# In[45]:

s * s


# In[47]:

s + s + 4


# In[48]:

np.exp(s)


# In[49]:

s[1:] + s[:-1]


# In[50]:

s[:-1]


# In[51]:

s = pd.Series(np.random.randn(5), name='something')


# In[52]:

s


# In[53]:

'something'


# In[54]:

s.name


# In[55]:

s2 = s.rename("different")


# In[56]:

s2


# In[57]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[58]:

d


# In[59]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[60]:

d


# In[62]:

df = pd.DataFrame(d)


# In[63]:

df


# In[64]:

pd.DataFrame(d, index=['d', 'b', 'a'])


# In[65]:

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['farm', 'three'])


# In[66]:

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])


# In[67]:

'one' in df


# In[68]:

df.index


# In[69]:

df.columns


# In[70]:

d = {'one' : [1., 2., 3., 4.],
'two' : [4., 3., 2., 1.]}


# In[71]:

pd.DataFrame(d, index=['a', 'b', 'c', 'd'])


# In[72]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[73]:

data


# In[74]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[75]:

data


# In[76]:

data[:] = [(1,2.,'Hello'), (2,3.,"World famous the best ever yes this is a test")]


# In[77]:

data


# In[78]:

data[:] = [(1,2.,'Hello'), (2,3546545465.7596631188772535874654687654654743543787689676556456484624544,"World")]


# In[79]:

data


# In[80]:

pd.DataFrame(data)


# In[81]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[82]:

pd.DataFrame(data)


# In[83]:

pd.DataFrame(data, index=['first', 'second'])


# In[84]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[85]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
data2


# In[86]:

pd.DataFrame(data2)


# In[87]:

pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
                 ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
             ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
                ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
               ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})


# In[88]:

df


# In[89]:

df['one']


# In[92]:

df['three'] = df['one'] * df['two']
df


# In[93]:

df['flag'] = df['one'] > 2


# In[94]:

df


# In[95]:

del df['two']


# In[96]:

three = df.pop('three')


# In[100]:

three


# In[101]:

df


# In[102]:

three
df


# In[103]:

df
df


# In[104]:

df1 = df * df


# In[105]:

df['foo'] = 'bar'
df


# In[106]:

df['one_trunc'] = df['one'][:2]
df


# In[107]:

df.insert(1, 'bar', df['one'])


# In[108]:

df


# In[ ]:



