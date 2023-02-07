import csv

f = open("data.csv", newline='')
reader = csv.reader(f, delimiter=" ", )

for row in reader:
    print(", ".join(row))