import matplotlib.pyplot as plt
import csv
import numpy as np

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

with open('rangliste_spalte_4.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]


array = make_numbers(array[0:], 0)
array = array[1:]
array = [item for sublist in array for item in sublist]
array = sorted(array, key = lambda x:float(x))
print(array)
plt.boxplot(array)
plt.title('Box-Whisker-Plot - Datensatz 3')
plt.ylabel('Überlebensrate der Unternehmen')
plt.savefig('box-whisker-plot.png', dpi=300, bbox_inches='tight')
plt.show()