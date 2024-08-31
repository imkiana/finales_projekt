# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:00:49 2024

@author: Kiana Heuser
"""

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

# Neue Daten als Dictionary
data = {
    'City': ['Ahmedabad', 'Aizawl', 'Amaravati', 'Amritsar', 'Bengaluru', 'Bhopal', 'Brajrajnagar', 'Chandigarh',
             'Chennai', 'Coimbatore', 'Delhi', 'Ernakulam', 'Gandhinagar', 'Gurugram', 'Guwahati', 'Hyderabad',
             'Indore', 'Jaipur', 'Jorapokhar', 'Kochi', 'Kolkata', 'Lucknow', 'Mumbai', 'Patna', 'Pune', 'Shillong',
             'Talcher', 'Thiruvananthapuram', 'Vadodara', 'Visakhapatnam'],
    'GDP': [1013.1, 861.4, 701.0, 619.2, 888.1, 987.1, 976.8, 745.8, 1018.1, 856.2, 531.0, 716.2, 974.4, 860.7, 1085.6,
            955.7, 646.5, 939.1, 898.3, 694.7, 1103.9, 972.9, 808.8, 918.1, 722.9, 743.0, 383.1, 774.6, 797.3, 715.6],
    'Industry': [33.44, 30.12, 32.76, 26.5, 31.38, 30.74, 31.5, 34.32, 28.04, 24.32, 21.72, 30.02, 27.02, 29.16, 31.72,
                 34.16, 25.92, 28.64, 26.74, 25.72, 29.78, 27.6, 31.88, 29.04, 30.14, 33.24, 34.6, 23.3, 30.4, 27.56],
    'Agriculture': [12.5, 11.36, 11.8, 15.34, 11.56, 13.54, 13.24, 14.02, 11.58, 9.82, 12.4, 16.52, 10.9, 13.24, 8.1,
                    14.28, 12.22, 13.36, 11.2, 14.06, 9.46, 10.88, 12.48, 11.82, 10.8, 12.26, 13.38, 13.42, 14.6, 12.34],
    'Services': [45.98, 35.96, 37.7, 43.16, 39.64, 40.12, 40.82, 39.22, 40.54, 38.22, 42.42, 42.68, 40.92, 44.66, 42.94,
                 42.02, 37.4, 39.48, 42.28, 36.72, 42.86, 36.1, 38.6, 41.6, 40.72, 42.14, 38.56, 38.36, 39.12, 38.78],
    'Technology': [19.36, 28.98, 25.24, 26.22, 20.74, 20.14, 20.7, 26.68, 20.66, 20.42, 19.54, 21.78, 19.92, 22.9, 30.02,
                   25.64, 22.0, 19.78, 21.46, 28.54, 25.5, 23.66, 17.42, 26.54, 22.28, 20.94, 24.28, 21.9, 20.7, 25.96]
}

# Erstellen eines DataFrames
df = pd.DataFrame(data)

# Runden der Prozentwerte und Sicherstellen, dass sie insgesamt 100% ergeben
df['Total'] = df[['Industry', 'Agriculture', 'Services', 'Technology']].sum(axis=1)
df['Industry'] = (df['Industry'] / df['Total'] * 100).round(2)
df['Agriculture'] = (df['Agriculture'] / df['Total'] * 100).round(2)
df['Services'] = (df['Services'] / df['Total'] * 100).round(2)
df['Technology'] = (df['Technology'] / df['Total'] * 100).round(2)

# Gesamtes GDP berechnen, um die relative Breite zu bestimmen
total_gdp = df['GDP'].sum()

# Relative Häufigkeiten für die Breite der Städte
df['Rel_GDP'] = df['GDP'] / total_gdp

# Funktion zum Erstellen des Mosaikplots
# Funktion zum Erstellen des Mosaikplots
def mosaic_plot(dataframe):
    plt.figure(figsize=(12, 8))
    
    # Umwandlung der Daten in ein Dictionary für das Mosaikplot
    props = {}
    for index, row in dataframe.iterrows():
        city = row['City']
        gdp_width = row['Rel_GDP']
        props[(city, 'Industry')] = row['Industry'] * gdp_width / 100
        props[(city, 'Agriculture')] = row['Agriculture'] * gdp_width / 100
        props[(city, 'Services')] = row['Services'] * gdp_width / 100
        props[(city, 'Technology')] = row['Technology'] * gdp_width / 100

    # Erstellen des Mosaikplots ohne Beschriftungen innerhalb der Mosaike
    color_dict = {
        'Industry': 'red',
        'Agriculture': 'green',
        'Services': 'blue',
        'Technology': 'orange'
    }

    # Entfernen von Labels innerhalb der Mosaike
    mosaic(props, gap=0.015, properties=lambda key: {'color': color_dict[key[1]]}, labelizer=lambda key: '')

    plt.title('Mosaikplot der Wirtschaftssektoren nach Stadt und GDP')
    plt.xlabel('Stadt (Breite proportional zu GDP)')
    plt.ylabel('Wirtschaftssektoren (Höhe proportional zu Prozent)')

    # Manuelle Beschriftung der Städte-Namen auf der x-Achse
    ax = plt.gca()
    ax.set_xticks([i + 0.5 for i in range(len(dataframe))])
    ax.set_xticklabels(dataframe['City'], rotation='vertical', ha='center')
    plt.show()

# Aufruf der geänderten Plot-Funktion
mosaic_plot(df)


