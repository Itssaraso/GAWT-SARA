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

def IQR(array):
    first = quartile(array)[0]
    third = quartile(array)[2]
    return third - first

def quartile(array):
    lenght = len(array)
    if lenght%2 == 0:
        first = calculate_median(array[:lenght/2])
        second = calculate_median(array)
        third = calculate_median(array[lenght/2:])
    else:
        first = calculate_median(array[:(lenght // 2 - 1)])
        second = calculate_median(array)
        third = calculate_median(array[(lenght // 2 - 1):])

    return first, second, third

def dezile(array):
    lenght = len(array)
    first = array[int(lenght*0.1)]
    second = array[int(lenght*0.2)]
    third = array[int(lenght*0.3)]
    forth = array[int(lenght*0.4)]
    fifth = array[int(lenght*0.5)]
    sixth = array[int(lenght*0.6)]
    seventh = array[int(lenght*0.7)]
    eighth = array[int(lenght*0.8)]
    ninth = array[int(lenght*0.9)]

    return first, second, third, forth, fifth, sixth, seventh, eighth, ninth




with open('urliste_spalte_2.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]


array = make_ints(array[0:], 0)
array = array[1:]
array = [item for sublist in array for item in sublist]
array = sorted(array, key = lambda x:float(x))
print(quartile(array))
print(dezile(array))
print(IQR(array))