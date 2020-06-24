import csv
import sys

from csv import DictReader
# receive file from the terminal as an argument
file_name = sys.argv[1]
if '19' in file_name:
    output = 'june_19.csv'
elif '20' in file_name:
    output = 'june_20.csv'
elif '21' in file_name:
    output = 'june_21.csv'
elif '22' in file_name:
    output = 'june_22.csv'

with open(file_name, 'r') as file:
    csv_dict_reader = DictReader(file)
    column_names = csv_dict_reader.fieldnames
    #print(len(column_names))
    #print(column_names)
    email = [None] * len(column_names);
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        for i in range(0,len(column_names)):
            if '@' in row[i]:
                email[i] = row[i]
               # print(i, row[i])
       # print(email)

with open(output, mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['name','email'])
    for i in range(len(column_names)):
        employee_writer.writerow([column_names[i],email[i]])