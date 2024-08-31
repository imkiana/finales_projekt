# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:45:42 2024

@author: Kiana Heuser
"""
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

# Beispiel-Daten
data = {
    'Stadt': ['Berlin', 'Berlin', 'Berlin', 'Berlin', 
              'Hamburg', 'Hamburg', 'Hamburg', 'Hamburg',
              'München', 'München', 'München', 'München', 
              'Köln', 'Köln', 'Köln', 'Köln'],
    'Sektor': ['Landwirtschaft', 'Industrie', 'Dienstleistungen', 'Bau',
               'Landwirtschaft', 'Industrie', 'Dienstleistungen', 'Bau',
               'Landwirtschaft', 'Industrie', 'Dienstleistungen', 'Bau',
               'Landwirtschaft', 'Industrie', 'Dienstleistungen', 'Bau'],
    'Prozent': [5, 30, 50, 15, 8, 40, 40, 12, 3, 25, 60, 12, 7, 35, 45, 13],
    'GDP': [400, 400, 400, 400, 300, 300, 300, 300, 500, 500, 500, 500, 200, 200, 200, 200]
}

# Erstelle einen DataFrame
df = pd.DataFrame(data)

# Gesamtes GDP berechnen, um die relative Breite zu bestimmen
total_gdp = df.groupby('Stadt')['GDP'].max().sum()

# Relative Häufigkeiten für die Breite der Städte
df['Rel_GDP'] = df['GDP'] / total_gdp

# Erstellen des Mosaikplots
def mosaic_plot(dataframe):
    plt.figure(figsize=(10, 6))
    
    # Gruppieren nach Stadt und Sektor und Berechnen der Gesamtanzahl für die relative Fläche
    dataframe['Rel_Fläche'] = dataframe['Prozent'] * dataframe['Rel_GDP'] / 100
    
    # Umwandlung der Daten für das Mosaik-Plot in ein Dictionary
    props = {}
    for (idx, row) in dataframe.iterrows():
        props[(row['Stadt'], row['Sektor'])] = row['Rel_Fläche']
    
    # Erstellen des Mosaikplots basierend auf den berechneten relativen Flächen
    mosaic_dict = mosaic(props, labelizer=lambda k: f"{k[1]}\n{df[(df['Stadt'] == k[0]) & (df['Sektor'] == k[1])]['Prozent'].iloc[0]}%", gap=0.02)
    
    plt.title('Mosaikplot der Wirtschaftssektoren nach Stadt und GDP')
    plt.xlabel('Stadt (Breite proportional zu GDP)')
    plt.ylabel('Wirtschaftssektoren (Höhe proportional zu Prozent)')
    plt.show()

# Mosaikplot anzeigen
mosaic_plot(df)


