import csv
import numpy as np
from sorting import *
import math
import matplotlib.pyplot as plt

with open('data-2-edited.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    array = list(reader)

array = np.array(array, dtype=object)
array = make_ints(array, 1)

x = [item for item in array[1:, 0]]
y = [item for item in array[1:, 1]]

x_numeric = range(len(x))
plt.figure(figsize=(20, 20))
plt.scatter(x_numeric, y, alpha=0.5)
plt.xticks(ticks=x_numeric, labels=x, rotation=90)
plt.xlabel('Bodennutzungsarten')
plt.ylabel('Landwirtschaftliche Betriebe Anzahl')
plt.title('Scatterplot von Datensatz 1')
plt.tight_layout()
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
plt.show()