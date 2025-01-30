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

with open('data-1-edited.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    array = list(reader)

array = np.array(array, dtype=object)
array = make_ints(array, 1)

x = [item for item in array[1:, 0]]
y = [item for item in array[1:, 1]]

x_numeric = range(len(x))
plt.figure(figsize=(25, 40))
plt.scatter(x_numeric, y, alpha=0.5)
plt.xticks(ticks=x_numeric, labels=x, rotation=90)
plt.xlabel('Bodennutzungsarten')
plt.ylabel('Landwirtschaftliche Betriebe Anzahl')
plt.title('Scatterplot von Datensatz 1')
plt.tight_layout()
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
plt.show()