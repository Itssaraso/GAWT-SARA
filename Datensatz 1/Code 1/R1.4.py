import csv
import numpy as np

def make_ints(data, column):
    for row in data[1:]:
        try:
            row[column] = int(row[column])
        except ValueError:
            pass

    return data

def save_lists_original(list, column, name):
    with open(name, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile, quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerows([[item] for item in list[:, column]])


with open('data-1-edited.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    array = list(reader)

array = np.array(array, dtype=object)
array = make_ints(array, 1)
save_lists_original(array, 0, 'urliste_spalte_1.csv')
save_lists_original(array, 1, 'urliste_spalte_2.csv')

