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

with open('data-3-combined.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    array = list(reader)

array = np.array(array, dtype=object)
array = make_numbers(array, 2)
array = make_numbers(array, 3)

save_strings_ranked(array,0, "rangliste_spalte_1.csv")
save_strings_ranked(array, 1,"rangliste_spalte_2.csv" )
save_floats_ranked(array,2, "rangliste_spalte_3.csv")
save_floats_ranked(array, 3,"rangliste_spalte_4.csv" )