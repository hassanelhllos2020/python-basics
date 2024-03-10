import csv
# access modes r, w, a, r+, w+, etc.
with open("names2.csv", newline="") as csvfile :
    reader = csv.DictReader(csvfile)
    i = 0
    for row in reader :
        print(i, row['fname'] , row['lname'])
        i += 1
