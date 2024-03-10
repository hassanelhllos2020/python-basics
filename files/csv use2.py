import csv
with open("name1.csv", 'w', newline="") as csvfile:
    header = ['name', 'age']
    writer = csv.DictWriter(csvfile, header)

    writer.writeheader()
    writer.writerow({
    'name': 'hassan',
    'age': 22})
    writer.writerow({
    'name': 'ahmed',
    'age': 18})