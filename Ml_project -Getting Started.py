#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
print("Python: {}".format(sys.version))
import scipy
print("Scipy: {}".format(scipy.__version__))
import numpy
print("Numpy: {}".format(numpy.__version__))
import matplotlib
print("Matplotlib: {}".format(matplotlib.__version__))
import pandas
print("Pandas: {}".format(pandas.__version__))
import sklearn
print("Sklearn: {}".format(sklearn.__version__))


# In[13]:


import pandas
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.ensemble import VotingClassifier


# In[19]:


#loading the data
url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names= ['sepal-length','sepal-width','petal-lenth','petal-width','class']
dataset=read_csv(url,names=names)


# In[20]:


#dimensions of the dataset
print(dataset.shape)


# In[21]:


#take a peak at the data
print(dataset.head(21))


# In[22]:


#statistical summary
print(dataset.describe())


# In[23]:


#class distrubution
print(dataset.groupby('class').size())


# In[24]:


#univariate plots -box and whisker plots
dataset.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)
pyplot.show()


# In[25]:


#histogram of the variable
dataset.hist()
pyplot.show()


# In[27]:


#multivariate plots
scatter_matrix(dataset)
pyplot.show()


# In[28]:


#creating a validation dataset
#splitting dataset
array=dataset.values
X=array[:,0:4]
y=array[:,4]
X_train,X_validation,Y_train,Y_validation=train_test_split(X,y,test_size=0.2,random_state=1)


# In[33]:


#Logistic Regression
#Linear Discriminant Analysis
#K-Nearest Analysis
#Classification and Regression Trees
#Gaussian Naive Bayes
#Support Vector Machines

#building models
models=[]
models.append(('LR',LogisticRegression(solver='liblinear',multi_class='ovr')))
models.append(('LDA',LinearDiscriminantAnalysis()))
models.append(('KNA',KNeighborsClassifier()))
models.append(('NB',GaussianNB()))
models.append(('SVM',SVC(gamma='auto')))


# In[36]:


#evaluate the created models
results=[]
names=[]
for name,model in models:
    kfold=StratifiedKFold(n_splits=10,random_state=1)
    cv_results=cross_val_score(model,X_train,Y_train,cv=kfold,scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f(%f)' %(name,cv_results.mean(),cv_results.std()))


# In[38]:


#compare our models
pyplot.boxplot(results,labels=names)
pyplot.title("Algorithm Comparisiom")
pyplot.show()


# In[39]:


#make predicions on SVM
model=SVC(gamma='auto')
model.fit(X_train,Y_train)
predictions=model.predict(X_validation)


# In[40]:


#evaluate our predictions on SVM
print(accuracy_score(Y_validation,predictions))
print(confusion_matrix(Y_validation,predictions))
print(classification_report(Y_validation,predictions))

