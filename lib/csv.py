import csv
with open("name.csv", 'w', newline="",) as csvfile:
    fieldnames = ['Fname', 'Lname', 'age', 'sex']
    writer = csvfile.dictwriter(csvfile, fieldnames=fieldnames)
writer.writeheader()