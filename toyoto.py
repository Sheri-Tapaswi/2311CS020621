# -*- coding: utf-8 -*-
"""toyoto.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U4Yk6kEVJN978VcX-J-nWPU3A8OTtA-O
"""

import pandas as pd
from google.colab import files
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name)

import pandas as pd
import statsmodels.formula.api as smf
df = pd.read_csv("Toyoto_Corrola.csv")
model = smf.ols('Price ~ Model + KM + Age_08_04 + HP', data=df).fit()
print(model.params)

model = smf.ols('Price ~ Model + KM + Weight + HP', data=df).fit()
print(model.params)

print(model.pvalues,model.tvalues)

(model.rsquared,model.rsquared_adj)

formula = 'Price ~ ' + ' + '.join(df.columns.difference(['Price']))
ml_v = smf.ols(formula, data=df).fit()
print(ml_v.tvalues)
print(ml_v.pvalues)

import pandas as pd
from google.colab import files
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name)

df_new = df.drop(["Model","Fuel_Type"],axis=1,inplace=True)

df.shape

df.corr

df.info()

df

df.drop(columns=["Color"], axis=1, inplace=True)

df.head()

print(df)

df.corr()

import statsmodels.formula.api as smf
model = smf.ols('Price~Mfg_Year+Central_Lock' ,data=df).fit()

(model.rsquared,model.rsquared_adj)

print(model.pvalues,model.tvalues)

import statsmodels.formula.api as smf
model = smf.ols('Mfg_Year~Price+CD_Player	' ,data=df).fit()

(model.rsquared,model.rsquared_adj)