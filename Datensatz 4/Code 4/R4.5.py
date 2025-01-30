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


def calculate_mean(list):
    if len(list) == 0:
        return 0

    total_sum = sum(list)
    count = len(list)
    mean = total_sum / count

    return mean

def calculate_mode(list):
    counter = Counter(list)
    max_freq = max(counter.values())

    modes = [key for key, freq in counter.items() if freq == max_freq]
    print(modes)
    return modes



with open('data-3-b-edited.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]

array = np.array(array, dtype=object)
spalte4 = make_numbers(array, 0)
spalte4 = spalte4[1:]
spalte4 = [item for sublist in spalte4 for item in sublist]

print(spalte4)
mean = calculate_mean(spalte4)
median = calculate_median(spalte4)
mode = calculate_mode(spalte4)

print('mean', mean, 'median', median,'mode', mode)