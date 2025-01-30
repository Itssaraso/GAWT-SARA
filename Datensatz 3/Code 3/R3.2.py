import numpy as np
import csv

with open('data-3-a-edited.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    table_1 = list(reader)
table_1 = np.array(table_1, dtype=object)

with open('data-3-b-edited.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    table_2 = list(reader)

table_2 = np.array(table_2, dtype=object)

combined_tables = np.empty((57,4), dtype=object)

combined_tables[0, 0] = 'Schlüssel'
combined_tables[0, 1] = table_1[0, 1]
combined_tables[0, 2] = table_2[0, 1]
combined_tables[0, 3] = table_2[0, 2]

for i in range(1, len(table_1)):
    indice = np.where(table_2[:, 0] == table_1[i, 0])[0][0]
    a = table_2[indice][1]
    b = table_2[indice][2]
    combined_tables[i] = [table_1[i, 0], table_1[i, 1], a, b]

print(combined_tables)

with open('data-3-combined.csv', mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',', quotechar='"')
        writer.writerows(combined_tables)