import csv
import numpy as np
import math
import matplotlib.pyplot as plt


def make_numbers(data, column):
    for row in data[1:]:
        try:
            row[column] = int(row[column])
        except ValueError:
            try:
                row[column] = float(row[column])
            except ValueError:
                pass

    return data

with open('data-3-combined.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    array = list(reader)

array = np.array(array, dtype=object)
array = make_numbers(array, 3)

x = [item for item in array[1:, 1]]
y = [item for item in array[1:, 3]]

x_numeric = range(len(x))
plt.figure(figsize=(20, 20))
plt.scatter(x_numeric, y, alpha=0.5)
plt.xticks(ticks=x_numeric, labels=x, rotation=90)
plt.xlabel('Unternehmensdemografie')
plt.ylabel('Überlebensrate der Unternehmen')
plt.title('Scatterplot von Datensatz 3')
plt.tight_layout()
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
plt.show()