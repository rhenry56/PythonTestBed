import csv

with open('C:/Users/richard.henry/Documents/filev.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[1]} Toolkit Update File {row[5]} Location, and TK File Nme {row[6]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

