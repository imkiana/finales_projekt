# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:21:13 2024

@author: Kiana Heuser
"""
#Datenanalyse https://www.kaggle.com/datasets/sudhanvahg/gdp-and-productivity-of-indian-cities-2019-2024

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"D:\github_repos\finales_projekt\Data\Economy_Productivity_SD_India.csv")
df2 = pd.read_csv(r"D:\github_repos\finales_projekt\Data\GDP_Sector_Income_2019_2023_30Cities.csv")

plt.hist(df2)