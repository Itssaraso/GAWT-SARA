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

def calculate_median(list):
    list.sort()
    n = len(list)

    if n % 2 == 1:
        return list[n // 2]
    else:
        mid1 = list[n // 2 - 1]
        mid2 = list[n // 2]
        return (mid1 + mid2) / 2

def abweichung_median(array, median):
    sum = 0
    for i in array:
        sum = sum + abs(i - median)
    sum = sum/len(array)
    return sum


with open('rangliste_spalte_3.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]

array = np.array(array, dtype=object)
spalte3 = make_numbers(array, 0)
spalte3 = spalte3[1:]
spalte3 = [item for sublist in spalte3 for item in sublist]

print(spalte3)
abweichung= abweichung_median(spalte3, calculate_median(spalte3))

print(abweichung)


with open('rangliste_spalte_4.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]

array = np.array(array, dtype=object)
spalte4 = make_numbers(array, 0)
spalte4 = spalte4[1:]
spalte4 = [item for sublist in spalte4 for item in sublist]

print(spalte4)
abweichung= abweichung_median(spalte4, calculate_median(spalte4))

print(abweichung)