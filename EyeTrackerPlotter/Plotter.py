#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


print("Please type the TimeSeries data file name")
dataFile = input(str(""))


# In[3]:


# Provide the image format
formatImage = input(str("Does your image is in the PNG or JPG, please type your answer ")).lower()
if formatImage ==('jpg'):
    imageJpg = input(str("provide your JPG file name "))
    img = plt.imread(imageJpg + ".jpg")
    
elif formatImage == ("png"):
    imagePng = input(str("provide your PNG file name "))
    img = plt.imread(imagePng + ".png")
else:
    print("ops, something is wrong, please try again ")


# Provide the size of the picture
print("What is the height of the picture?")
hImage = input(int())
print("What is the width of the picture?")
wImage = input(int())
# In[4]:


# Load the data and encode the utf8
data = pd.read_csv(dataFile + '.csv',sep='\t',encoding='utf8')


# In[5]:


# Prepare data
# data = pd.concat([data, data['values'].str.split(',', expand=True)], axis=1)
# data = data.drop('values', axis=1)

## G and H represent the columns with corr
# Prepare data
data = pd.concat([data, data['values'].str.split(',', expand=True)], axis=1)
data = data.drop('values', axis=1)
data = data.rename(columns={"variable_name":"variable",0:"G", 1: "H"})


# In[6]:


#Show first 5 rows
data.head()


# ### Specyfic setup, depens of the different variables or data types etc.

# In[7]:


output = {}
current_answer = None
for _,row in data.iterrows():
    if 'answer' in row['variable']:
        current_answer = row['H']
    else:
        output.setdefault('y',[]).append(row['H'])
        output.setdefault('x',[]).append(row['G'])
        output.setdefault('answer',[]).append(current_answer)
data = pd.DataFrame.from_dict(output)

# decimals = pd.Series([0,1], index=['x','y'])
# data = data.round(decimals)
# data = data.x.astype(float);

# data = data.to_csv("ConvertedX_Y.csv")
data.x = data.x.str.extract('(\d+)', expand=False)
data.y = data.y.str.extract('(\d+)', expand=False)
data.x
data.head()
# data.x.astype(int);
# data.y.astype(int);
data = data.astype(float)

data = data.drop('answer', axis=1)
data = data.dropna(how='all')
data.head(1000)


# ### Plotting Scatters and Heatmaps

# In[8]:


# Plotting on the scatter with picture on the back ground.
# img = plt.imread('bath.jpg')

# load the coordinates file
x = data['x']
y = data['y']

plt.scatter(x, y, cmap='summer', edgecolor='red', linewidth=1, alpha=0.75)
# plt.hist2d(x,y, bins=[np.arange(0,800,5),np.arange(0,450,5)])

plt.title('Eye Tracker corrdianates')
plt.xlabel('X corrinates')
plt.ylabel('Y corridnates')
plt.imshow(img)
plt.style.use('seaborn')

plt.xlim(0,800)
plt.ylim(450,0)
plt.tight_layout()


# In[11]:


# import the required packages
from scipy import stats, integrate
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# load the coordinates file
# x = data['x']
# y = data['y']

# call the kernel density estimator function
ax = sns.kdeplot(x, y, cmap="Reds", shade=True, shade_lowest=False, alpha=0.5)
# the function has additional parameters you can play around with to fine-tune your heatmap, e.g.:
#ax = sns.kdeplot(x, y, kernel="gau", bw = 25, cmap="Reds", n_levels = 50, shade=True, shade_lowest=False, gridsize=100)

# plot your KDE
ax.set_frame_on(False)
plt.xlim(0, int(wImage))
plt.ylim(int(hImage), 0)
plt.axis('on')
plt.imshow(img)

print("Your heatmap is saved in the current directory")
plt.savefig("heatmap" + dataFile + ".jpg")

plt.show()

# save your KDE to disk
fig = ax.get_figure()
fig.savefig('kde.png', transparent=True, bbox_inches='tight', pad_inches=0)


# In[8]:




