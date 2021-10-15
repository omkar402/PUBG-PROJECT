#!/usr/bin/env python
# coding: utf-8

# # 1.Read the dataset.

# In[5]:


import pandas as pd
data = pd.read_csv("pubg - Dr. Darshan Ingle.csv")
print(data)


# # 2. Check the datatype of all the columns.

# In[8]:


data.columns
data.dtypes


# # 3.Find the summary of all the numerical columns and write your findings about it.

# In[41]:


data.describe()


# # In this dataset there are 20 columns with different data having differnt values
# 1. The dataset consists of total 20 columns of numerical datatype 
# 2. mean gives the average value of that column 
# 3. std gives the standard deviation of that column 
# 4. min gives the minmum value present in that column 
# 5. max gives the maximum value present in that column 
# 6. 25% gives the 25% of that data 
# 7. 50% gives the 50% of that data 
# 8. 75% gives the 75% of that data
# 
# 

# # 4.The average person kills how many players?

# In[44]:


a=data['kills'].mean()
print('The average person kills',a,'players')


# # 5.99% of people have how many kills?

# In[7]:


import numpy as np
np.percentile(data.kills,99)


# # 6.The most kills ever recorded are how much?

# In[9]:


b=data.kills.max()
print("most kills ever recorded are ",b)
print("helooooo oooo")


# # 7. Print all the columns of the dataframe.

# In[11]:


data.columns


# # 8.Comment on distribution of the match's duration. Use seaborn.

# In[23]:


import seaborn as sb
sb.distplot(data.matchDuration);


# # 1.mean value of match's duration is 1575.398
# 
# 
# 
# 2.std of match's duration is 258.9635152028575
# 
# 
# 
# 3.min match's duration is 464
# 
# 
# 
# 4.max match's duration is 2202

# # 9.Comment on distribution of the walk distance. Use seaborn.

# In[27]:


sb.distplot(data.walkDistance)


# # data['walkDistance'].std()
# 
# max of walkDistance is=10490.0
# 
# min  of walkDistance is=0.0
# 
# mean of  walkDistance is 1130.0084103600002
# 
# std of walkDistance is =1168.5979830618528
# 
# 

# # 10.Plot distribution of the match's duration vs walk distance one below the other.

# In[33]:


import matplotlib.pyplot as plt
fig,axs=plt.subplots(2,1)
sb.distplot(data.matchDuration,ax=axs[0]);
sb.distplot(data.walkDistance,ax=axs[1]);


# # 11.Plot distribution of the match's duration vs walk distance side by side.

# In[37]:


import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2)
sb.distplot(data.matchDuration,ax=axs[0]);
sb.distplot(data.walkDistance,ax=axs[1]);


# # 12.Pairplot the dataframe. Comment on kills vs damage dealt, Comment on maxPlace vs numGroups.

# In[ ]:


import seaborn as sb
import pandas as pd
data = pd.read_csv("pubg - Dr. Darshan Ingle.csv")
data.describe()
sb.pairplot(data.head(500))


# # 13.How many unique values are there in 'matchType' and what are their counts?

# In[8]:


print(data['matchType'].unique().tolist())
print()
print(data['matchType'].value_counts().tolist())


# # 14.Plot a barplot of ‘matchType’ vs 'killPoints'. Write your inferences. 

# In[16]:


import seaborn as sb
import matplotlib.pyplot as plt
sb.barplot(x='matchType', y='killPoints', data=data);
plt.xticks(rotation=90);


# # 15.Plot a barplot of ‘matchType’ vs ‘weaponsAcquired’. Write your inferences.

# In[15]:


import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
sb.barplot(x='matchType', y='weaponsAcquired', data=data);
plt.xticks(rotation=90);


# # 16. Find the Categorical columns.

# In[1]:


import pandas as pd
data = pd.read_csv("pubg - Dr. Darshan Ingle.csv")
data.describe()
data.select_dtypes(exclude=['number'])


# # 17.Plot a boxplot of ‘matchType’ vs ‘winPlacePerc’. Write your inferences.

# In[5]:


import seaborn as sb
import matplotlib.pyplot as plt

sb.boxplot(data.matchType,data.winPlacePerc);

plt.xticks(rotation=90);


# # 18.Plot a boxplot of ‘matchType’ vs ‘matchDuration’. Write your inferences.

# In[4]:


import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("pubg - Dr. Darshan Ingle.csv")
data.describe()
sb.boxplot(data.matchType,data.matchDuration);
plt.xticks(rotation=90);


# # 19.Change the orientation of the above plot to horizontal.

# In[6]:


sb.boxplot(data.matchDuration,data.matchType);
plt.xticks(rotation=90);


# # 20.Add a new column called ‘KILL’ which contains the sum of following columns viz. headshotKills,teamKills, roadKills.
# 

# In[15]:


data['kill']=data['headshotKills']+data['teamKills']+data['roadKills']
data


# # 21.Round off column ‘winPlacePerc’ to 2 decimals.

# In[19]:


data['winPlacePerc']=round(data['winPlacePerc'],2)
data['winPlacePerc']


# # 22.Take a sample of size 50 from the column damageDealt for 100 times and calculate its mean. Plot it on a histogram and comment on its distribution.
# 

# In[10]:


import numpy as np
import seaborn as sb
import pandas as pd
data = pd.read_csv("pubg - Dr. Darshan Ingle.csv")
data.describe()
x = []
for i in range(100):
  x.append(data['damageDealt'].sample(50).mean())
means = np.array(x)
sb.distplot(means);

#std()=167.1939453412012
#mean()=129.2112641000002
#min()=0
#max()=3469.0


# 
# 1.maximum damageDealt in histrogram is=3469.0
# 
# 2.min damageDealt in histrogram is=0
# 
# 3.std damageDealt in histrogram is=167.1939453412012
# 
# 4.mean damageDealt in histrogram is=129.2112641000002
# 

# In[ ]:




