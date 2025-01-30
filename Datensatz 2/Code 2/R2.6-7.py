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

def save_lists_original(list, column, name):
    with open(name, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows([[item] for item in list[:, column]])

def save_floats_ranked(list, column, name):
    data = [item for item in list[:, column]]
    data[1:] = sorted(data[1:], key = lambda x:float(x))
    data = [[item] for item in data[:]]
    with open(name, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)

def save_strings_ranked(list, column, name):
    data = [item for item in list[:, column]]
    data[1:] = sorted(data[1:])
    data = [[item] for item in data[:]]
    with open(name, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(data)

with open('data-2-edited.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    array = list(reader)

array = np.array(array, dtype=object)
array = make_ints(array, 1)
save_lists_original(array,0, "urliste_spalte_1.csv")
save_lists_original(array, 1,"urliste_spalte_2.csv" )
save_strings_ranked(array, 0, 'rangliste_spalte_1.csv')
save_floats_ranked(array, 1, 'rangliste_spalte_2.csv')