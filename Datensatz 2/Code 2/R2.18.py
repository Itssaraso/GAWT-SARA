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

def calculate_median(list):
    list.sort()
    n = len(list)

    if n % 2 == 1:
        return list[n // 2]
    else:
        mid1 = list[n // 2 - 1]
        mid2 = list[n // 2]
        return (mid1 + mid2) / 2


def quartile(array):
    length = len(array)
    if length%2 == 0:
        new_l = int(length/2)
        first = calculate_median(array[:int(length/2)])
        second = calculate_median(array)
        third = calculate_median(array[int(length/2):])
    else:
        first = calculate_median(array[:(length // 2 - 1)])
        second = calculate_median(array)
        third = calculate_median(array[(length // 2 - 1):])

    return first, second, third

def IQR(array):
    first = quartile(array)[0]
    third = quartile(array)[2]
    return third - first


with open('rangliste_spalte_2.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]


array = make_ints(array[0:], 0)
array = array[1:]
array = [item for sublist in array for item in sublist]
array = sorted(array, key = lambda x:float(x))

print(IQR(array))