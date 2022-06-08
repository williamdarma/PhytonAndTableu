# -*- coding: utf-8 -*-
"""
Created on Mon May 23 10:22:58 2022

@author: Zendrax
"""

import pandas as pd

#bring the file

#file_name = pd.read_csv('file.csv') <--- format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')

#summary of data
data.info()

#playing around with variables
var = ('apple','pear','banana')
var = range(2,9);
var = {'name':'Dee','location':'south africa'}
var = {'apple','pear','banana'}

#working with calculation
#Defining variable

costPerItem = 11.73
sellingPricePerItem = 21.11
numberOfItemPurchase = 6

#mathematical operation
profitPerItem = sellingPricePerItem-costPerItem

profitPerTransaction = numberOfItemPurchase*profitPerItem
sellingPricePerTransaction = numberOfItemPurchase*sellingPricePerItem

#Cost per transaction column calculation

#costPerTransaction = costPerItem*NumberofItemPurchase
#variable = dataframe['column_name']

costPerItem = data['CostPerItem']
numberofItemPurchase= data['NumberOfItemsPurchased']
costPerTransaction = costPerItem * numberofItemPurchase


#adding new colum into dataframe
data['CostPerTransaction'] = costPerTransaction

#sales per transaction
data ['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit Calculation = sales - cost
data['ProfitperTransaction'] = data ['SalesPerTransaction']- data['CostPerTransaction']

#markup = (sales-cost)/cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

data['Markup'] = data['ProfitperTransaction']/data['CostPerTransaction']

#Rounding Marking

roundMarkUp =  round(data['Markup'],2)
data['Markup'] = roundMarkUp

#Combining DataField

my_name = 'william' + 'terserah'
my_date = 'day'+'-'+'month'+'-'+'year'
#my_date = data['Day'] +

#checking colums data type
print(data['Day'].dtype)


#change colums type

day = data['Day'].astype(str)
print(day.dtype)

year = data['Year'].astype(str)

my_date = day+'-'+ data['Month']+ '-' + year
data['date'] = my_date


#using iloc to view specific colums/rows
data.iloc[0] #views the row with index 0
data.iloc[0:3]  #views the row with index 0-3
data.iloc[-5]  #views the row with index last 5

data.head(5) #bring in 5 rows

data.iloc[:,2] #bring all row on the 2nd column

data.iloc[4,2] #bring 4 row on the 2nd column

#using split to split the client keywoird field
#neww_var = column.str.split('sep',expand = true)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#creating new colomn for split colomn in client keyword

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthContract'] = split_col[2]


#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','');
data['LengthContract'] = data['LengthContract'].str.replace(']','');

#using the lower functino to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()



#how to merge files
#bringing in a new dataset

seasons = pd.read_csv('E:/Data Annalytics/Data/value_inc_seasons.csv',sep=';')

#merge files : merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data,seasons)

#dropping collumns
#dataaframe = df,drop('columnname), axis =1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop(['Month', 'Year'],axis = 1)

#export to csv

data.to_csv('ValueInc_Cleaned.csv', index= False)


































































































































