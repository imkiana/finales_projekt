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
#import numpy as np
import itertools as it


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
        
    def check_and_adjust_values(self, value1, value2): #100% chatgpt
        difference_percentage = abs(value1 - value2) / value1 * 100
        if difference_percentage <= 5:
            return True
        else:
            return False
        
    def plotDevelopment(self): #1-30
        anfang=self.X
        ende=self.N
        städte = df[df["Year"]==2020].iloc[anfang-1:ende,0] #anzahl städte + alle infos #bereinigt nur städte
        
        plt.figure()
        y_ticks = []
        y_labels = []
        for i in range(len(städte)):
            aktuelleStadt = df[df["City"]==städte.iloc[i]] #alle infos der stadt
            aktuelleStadt = aktuelleStadt.iloc[:,self.plotNummer+1].reset_index(drop=True) #nur die infos fürs gewollte plot auswählen
            plt.plot(aktuelleStadt, label=städte.iloc[i])
            y_ticks.append(aktuelleStadt.iloc[-1]) #pos für ticks holen
            y_labels.append(städte.iloc[i]) #label für ticks holen
        titel = pd.DataFrame(aktuelleStadt).columns.tolist() #pandas series warum auch immer
        plt.xticks(ticks=range(6),labels=[2019,2020,2021,2022,2023,2024])
        ax = plt.gca()
    
        for tick_position in range(6):
            ax.axvline(x=tick_position, color='gray', linestyle='--', linewidth=0.7)
            
        ax_right = ax.twinx() #2te achse rechts hinzufügen
        ax_right.set_ylim(ax.get_ylim())
        for i in list(it.combinations(range(len(y_ticks)), 2)):
            überlagerung = self.check_and_adjust_values(y_ticks[i[0]],y_ticks[i[1]])
            if überlagerung == True:
                idkhowtoname = (0, 1) if y_ticks[i[0]] > y_ticks[i[1]] else (1, 0)
                y_ticks[i[idkhowtoname[0]]] = y_ticks[i[idkhowtoname[0]]] * 1.01  # Erhöhe um 1%
                y_ticks[i[idkhowtoname[1]]] = y_ticks[i[idkhowtoname[1]]] * 0.99  # Verringere um 1%
        ax_right.set_yticks(y_ticks)
        ax_right.set_yticklabels(y_labels)
        
        prop_cycle = plt.rcParams['axes.prop_cycle'] #farben der aktuellen plt farbliste holen
        colors = prop_cycle.by_key()['color']
        
        for tick_label, color in zip(ax_right.get_yticklabels(), colors[anfang - 1:ende]): #tick label färben
            tick_label.set_color(color)
        plt.title(str(titel).replace('[', '').replace(']', '').replace("'", '')) #titel anbringen
        plt.show()                  
        
test = Datenanalyse(N=5,plotNummer=7) #num 1-7
test.plotSectors()
test.plotDevelopment()
