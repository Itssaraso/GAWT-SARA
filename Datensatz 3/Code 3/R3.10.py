import csv
import numpy as np
from collections import Counter


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




with open('rangliste_spalte_3.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]

array = np.array(array, dtype=object)
spalte3 = make_numbers(array, 0)
spalte3 = spalte3[1:]
spalte3 = [item for sublist in spalte3 for item in sublist]
print(spalte3)
spannweite = spalte3[len(spalte3) - 1] - spalte3[0]
print(spannweite)


with open('rangliste_spalte_4.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]

array = np.array(array, dtype=object)
spalte4 = make_numbers(array, 0)
spalte4 = spalte4[1:]
spalte4 = [item for sublist in spalte4 for item in sublist]
print(spalte4)
spannweite = spalte4[len(spalte3) - 1] - spalte4[0]
print(spannweite)