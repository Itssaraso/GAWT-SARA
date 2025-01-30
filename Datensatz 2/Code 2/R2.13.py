import matplotlib.pyplot as plt
import csv
import numpy as np

def make_ints(data, column):
    for row in data[1:]:
        try:
            row[column] = int(row[column])
        except ValueError:
            pass

    return data

with open('rangliste_spalte_2.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]


array = make_ints(array[0:], 0)
array = array[1:]
array = [item for sublist in array for item in sublist]
array = sorted(array, key = lambda x:float(x))

plt.boxplot(array)
plt.title('Box-Whisker-Plot - Datensatz 2')
plt.ylabel('Anzahl Landwirtschaftliche Betriebe mit ökologischem Landbau')
plt.savefig('box-whisker-plot.png', dpi=300, bbox_inches='tight')
plt.show()