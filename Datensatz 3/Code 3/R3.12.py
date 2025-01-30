import csv
import numpy as np
from collections import Counter
import math

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

def calculate_mean(list):
    if len(list) == 0:
        return 0

    total_sum = sum(list)
    count = len(list)
    mean = total_sum / count

    return mean

def stichprobenvarianz(array, mean):
    sum = 0
    for i in array:
        sum = sum + abs(i - mean)**2
    sum = sum / (len(array) - 1)
    return math.sqrt(sum)


with open('rangliste_spalte_3.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]

array = np.array(array, dtype=object)
spalte3 = make_numbers(array, 0)
spalte3 = spalte3[1:]
spalte3 = [item for sublist in spalte3 for item in sublist]

print(spalte3)
s= stichprobenvarianz(spalte3, calculate_mean(spalte3))

print(s)


with open('rangliste_spalte_4.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]

array = np.array(array, dtype=object)
spalte4 = make_numbers(array, 0)
spalte4 = spalte4[1:]
spalte4 = [item for sublist in spalte4 for item in sublist]

print(spalte4)
s= stichprobenvarianz(spalte4, calculate_mean(spalte4))

print(s)