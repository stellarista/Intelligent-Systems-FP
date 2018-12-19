import csv

with open('data.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    data = [['',''], []]
    a.writerows(data)