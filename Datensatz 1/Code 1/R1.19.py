import csv
import numpy as np
import math
import matplotlib.pyplot as plt

def make_ints(data, column):
    for row in data[1:]:
        try:
            row[column] = int(row[column])
        except ValueError:
            pass

    return data

with open('urliste_spalte_2.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]


array = make_ints(array[0:], 0)
array = array[1:]
array = [item for sublist in array for item in sublist]

#nach Bodennutzungsarten klassifiziert
v1 = ['Kleine Betriebe', 'Mittlere Betriebe', 'Große Betriebe']
v2 = [(1040 + 920 + 210 + 410 + 500 + 15410), (155080+117750+115570+100470+90160+47060+47110), (255010+251130+187300)]
plt.bar(v1, v2)
plt.xlabel('Klassen')
plt.ylabel('Anzahl Landwirtschaftliche Betriebe')
plt.title('Histogramm Anzahl Landwirtschaftliche Betriebe')
plt.tight_layout()
plt.show()

#nach Anzahl Betriebsfläche klassifiziert
v1 = ['Flächennutzung', 'Getreide', 'Hackfrüchte', 'Hülsenfrüchte', 'Handelsgewächse', 'Gemüse und Gartengewächse']
v2 = [np.sum(array[0:3]), np.sum(array[3:24]), np.sum(array[24:28]), np.sum(array[28:34]), np.sum(array[34:48]), np.sum(array[48:])]
v2 = [int(item) for item in v2]
plt.bar(v1, v2)
plt.xlabel('Bodennutzungsarten')
plt.ylabel('Landwirtschaftliche Betriebe (Anzahl)')
plt.title('Histogramm Bodennutzungsarten')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()