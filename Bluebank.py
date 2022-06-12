# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:02:50 2022

@author: Zendrax
"""

import pandas as pd
import json 
import numpy as np
import matplotlib.pyplot as pit

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

  
#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

#transform to dataframe
loadData = pd.DataFrame(data)

loadData.info()
#finding unique value for the purpose column
loadData['purpose'].unique()

#describe the data
loadData.describe()
                 

#describe the data for the specific column
loadData['int.rate'].describe()
loadData['fico'].describe()
loadData['dti'].describe()

#using exp() to get annual income
income = np.exp(loadData['log.annual.inc'])                
loadData['annualIncome'] = income


#Working with array
#0D array
arr = np.array(43)

#1D array
arr = np.array([1,2,3,4])

#2D array
arr = np.array([[1,2,3],[4,5,6]])


#working with if statement

a = 40
b = 500
c = 1000

if b>a:
    print('b lebih besar dari a')
else:
    print('a lebih besar dari b')


if b>a and b<c:
    print('b lebih besar dari a tapi lebih kecil dari c')
else:
    print('tidak ada kondisi terpenuhi')
    
#fico score
# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'
fico = 100
if fico >= 300 and fico<400:
    ficocat = 'very poor'
elif fico >= 400 and fico<600:
    ficocat = 'poor'
elif fico >= 600 and fico<660:
    ficocat = 'fair'
elif fico >= 660 and fico<780:
    ficocat = 'good'
elif fico >= 780 :
     ficocat = 'excellent'
else:
     ficocat = 'unknown'
        
#for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

for x in range(0,3):
    y = fruits[x]
    print(y)
    
    
#applying for loop to loadData
#using first 10
ficocat = []

totalFico = len(loadData)
print(totalFico)
for x in range(0,totalFico):
    category = loadData['fico'][x]
    if category >=300 and category<400:
        cat = 'very poor'
    elif category >= 400 and category<600:
        cat = 'poor'
    elif category >= 600 and category<660:
        cat = 'fair'
    elif category >= 660 and category<700:
        cat = 'good'
    elif category >= 700 :
         cat = 'excellent'
    else:
         cat = 'unknown'            

    ficocat.append(cat)

ficocat = pd.Series(ficocat)

loadData['fico_Category'] = ficocat


#while loops

i = 1;
while i<10:
    print(i)
    i+=1

#testing error
# =============================================================================
# totalFico = len(loadData['fico'])
# for x in range(0,totalFico):
#     category = loadData['fico'][x]
#     if category >=300 and category<400:
#             cat = 'very poor'
#     elif category >= 400 and category<600:
#             cat = 'poor'
#     elif category >= 600 and category<660:
#             cat = 'fair'
#     elif category >= 660 and category<700:
#             cat = 'good'
#     elif category >= 700 :
#              cat = 'excellent'
#     else:
#              cat = 'unknown'            
#    # except:
#      #   cat = 'unknown'
# ficocat.append(cat)
# 
# ficocat = pd.Series(ficocat)
# 
# loadData['fico_Category'] = ficocat
# =============================================================================


#df.loc as conditional statement
#df.loc[df[columnname] condition, new columnname] = 'value id the condition is met

#for interest rates , a new column is wanted, rate>.12 teh high, else low

loadData.loc[loadData['int.rate']>0.12,'int.rate.type']='High'
loadData.loc[loadData['int.rate']<=0.12,'int.rate.type']='Low'

#number of loan/row by fico.category
catplot = loadData.groupby(['fico_Category']).size()

catplot.plot.bar()

catplot.plot.bar(color = 'red',width = .1)
pit.show()

purposeCount = loadData.groupby(['purpose']).size()
purposeCount.plot.bar(color = 'Green',width = .2)
pit.show()

ypoint = loadData['annualIncome']
xpoint = loadData['dti']
pit.scatter(xpoint, ypoint, color = 'red')
pit.show()

#export to csv

loadData.to_csv('loan_Cleaned.csv', index = True)

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 

                 














































