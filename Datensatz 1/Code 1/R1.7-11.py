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


def calculate_mean(list):
    if len(list) == 0:
        return 0

    total_sum = sum(list)
    count = len(list)
    mean = total_sum / count

    return mean

def abweichung_median(array, median):
    sum = 0
    for i in array:
        sum = sum + abs(i - median)
    sum = sum/len(array)
    return sum

def stichprobenvarianz(array, mean):
    sum = 0
    for i in array:
        sum = sum + abs(i - mean)**2
    sum = sum / (len(array) - 1)
    return math.sqrt(sum)

def erwartungswert(array):
    return sum(array)/len(array)


def variationskoeffizient(array, mean):
    sigma = stichprobenvarianz(array, mean)
    vk = sigma/erwartungswert(array)
    return vk

with open('urliste_spalte_2.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    array = [row for row in reader]


array = make_ints(array[0:], 0)
array = array[1:]
array = [item for sublist in array for item in sublist]

array = sorted(array, key = lambda x:float(x))
print(array)

mean = calculate_mean(array)
median = calculate_median(array)
#mode = calculate_mode(array[1:, 1])
spannweite= array[len(array)-1] - array[0]

print(mean, median, spannweite)
print(abweichung_median(array, median))
print(stichprobenvarianz(array, mean))
print(variationskoeffizient(array, mean))