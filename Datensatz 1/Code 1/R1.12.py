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

plt.boxplot(array)
plt.title('Box-Whisker-Plot - Datensatz 1')
plt.ylabel('Landwirtschaftliche Betriebe')
plt.savefig('box-whisker-plot.png', dpi=300, bbox_inches='tight')
plt.show()