# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:21:13 2024

@author: Kiana Heuser
"""
#Datenanalyse https://www.kaggle.com/datasets/sudhanvahg/gdp-and-productivity-of-indian-cities-2019-2024

import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic
import numpy as np


df = pd.read_csv(r"D:\github_repos\finales_projekt\meinPaket\Data\Economy_Productivity_SD_India.csv")
df2 = pd.read_csv(r"D:\github_repos\finales_projekt\meinPaket\Data\GDP_Sector_Income_2019_2023_30Cities.csv")
df = pd.DataFrame(df)
df2 = pd.DataFrame(df2)

class Datenanalyse():
    def __init__(self,X=1,N=4,plotNummer=1):
        self.X = X
        self.N = N
        self.plotNummer = plotNummer
    
    def mosaic_plot(self,dataframe):
        #plt.figure(figsize=(12, 8))
        
        props = {}
        for index, row in dataframe.iterrows():
            city = row['City']
            gdp_width = row['Rel_GDP']
            props[(city, 'Industry')] = row['Industry'] * gdp_width / 100
            props[(city, 'Agriculture')] = row['Agriculture'] * gdp_width / 100
            props[(city, 'Services')] = row['Services'] * gdp_width / 100
            props[(city, 'Technology')] = row['Technology'] * gdp_width / 100
    
        color_dict = {
            'Industry': 'gray',
            'Agriculture': 'green',
            'Services': 'turquoise',
            'Technology': 'orange'
        }
    
        mosaic(props, gap=0.015, properties=lambda key: {'color': color_dict[key[1]]}, labelizer=lambda key: '')
    
        plt.title('Mosaikplot der Wirtschaftssektoren nach Stadt und GDP')
        plt.xlabel('Stadt (Breite proportional zu GDP)')
        plt.ylabel('Wirtschaftssektoren (Höhe proportional zu Prozent)')
         

    
    def plotSectors(self):
        X = self.X - 1
        N = self.N
        
        
        dfsummen = df2.groupby("City").agg({
            "GDP (in billion $)": "sum",
            "Industry (%)": "mean",
            "Agriculture (%)": "mean",
            "Services (%)": "mean",
            "Technology (%)": "mean"
        }).reset_index()
        
        dfsummen.columns = [
            "City",
            "GDP",
            "Industry",      
            "Agriculture", 
            "Services",     
            "Technology"     
        ]
        
        dfsummen = dfsummen.iloc[X:N, :]
        
        dfplot = pd.DataFrame(dfsummen)
        
        dfplot['Total'] = dfplot[['Industry', 'Agriculture', 'Services', 'Technology']].sum(axis=1)
        dfplot['Industry'] = (dfplot['Industry'] / dfplot['Total'] * 100).round(2)
        dfplot['Agriculture'] = (dfplot['Agriculture'] / dfplot['Total'] * 100).round(2)
        dfplot['Services'] = (dfplot['Services'] / dfplot['Total'] * 100).round(2)
        dfplot['Technology'] = (dfplot['Technology'] / dfplot['Total'] * 100).round(2)
        
        total_gdp = dfplot['GDP'].sum()
        dfplot['Rel_GDP'] = dfplot['GDP'] / total_gdp
        self.mosaic_plot(dfplot)
        

    def plotDevelopment(self,anfang=1,ende=5): #1-30
        städte = df[df["Year"]==2020].iloc[anfang-1:ende,0] #anzahl städte + alle infos #bereinigt nur städte
        
        plt.figure()
        y_ticks = []
        y_labels = []
        for i in range(len(städte)):
            aktuelleStadt = df[df["City"]==städte.iloc[i]] #alle infos der stadt
            aktuelleStadt = aktuelleStadt.iloc[:,self.plotNummer+1].reset_index(drop=True) #nur die infos fürs gewollte plot auswählen
            #titel = pd.DataFrame(aktuelleStadt).columns.tolist() #pandas series warum auch immer
            plt.plot(aktuelleStadt, label=städte.iloc[i])
            y_ticks.append(aktuelleStadt.iloc[0])
            y_labels.append(städte.iloc[i])
        print(y_ticks)
        titel = pd.DataFrame(aktuelleStadt).columns.tolist()
        plt.xticks(ticks=range(6),labels=[2019,2020,2021,2022,2023,2024])
        ax = plt.gca()
        
        for tick_position in range(6):
            ax.axvline(x=tick_position, color='gray', linestyle='--', linewidth=0.7)
        prop_cycle = plt.rcParams['axes.prop_cycle']
        colors = prop_cycle.by_key()['color']
        plt.yticks(ticks=y_ticks, labels=y_labels)
                       
        ax = plt.gca()
        
        for tick_label, color in zip(ax.get_yticklabels(), colors[anfang-1:ende]):
            tick_label.set_color(color)
        plt.title(str(titel).replace('[', '').replace(']', '').replace("'", ''))
        plt.show()

test = Datenanalyse(plotNummer=4) #1-7
test.plotSectors()
test.plotDevelopment()