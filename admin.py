# -*- coding: utf-8 -*-

import pandas as pd



df=pd.read_csv('sharks.csv')
df_1=df.fillna(0)
df_2=df_1.loc[df_1['Event']!=0]
df_2.to_csv('SharksEvents.csv',index=False)
