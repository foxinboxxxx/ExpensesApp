import os, fnmatch
from datetime import datetime
import csv
import re

months = ["январь", "февраль", "март", "апрель", "май",
     "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

modified_data = []

class File:

    def __init__(self):
        self.modified_data = []
        self.sort_by_month = []

    def match(self,fld, search):
        for fn in os.listdir(fld):
            if fnmatch.fnmatch(fn, search):
                print(fn)

    def get_date(self, timestmp):
        return datetime.utcfromtimestamp(timestmp).strftime('%d %b %Y')

    def get_file_attrs(self, fld):
        with os.scandir(fld) as dir:
            for f in dir:
                if f.is_file():
                    inf = f.stat()
                    print(f'Modified {self.get_date(inf.st_mtime)} {f.name}')

    def remove_file(self, file):
        if os.path.isfile(file):
            try:
                os.remove(file)
            except OSError as error:
                print(f"Error: {file}: {error.strerror}")
        else:
            print(f"Error: {file} is not valied file")

    def read_file(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.read()
        print(lines)
        return lines

    def read_file_by_lines(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                filter_line = ''.join(i for i in line if not i.isdigit())
                # check if line contains month
                if filter_line.strip() in months:
                    self.modified_data.append(line)
                # check if line is empty
                elif len(line.strip()) == 0 :
                    pass
                # calculate sum of all numbers in line
                else:
                    self.modified_data.append(self.sum_of_line(line))

    def write_to_file(self, file, data):
        with open(file, 'w', encoding='utf-8') as f:
            f.write(data)

    def append_line_to_file(self, file, data):
        with open(file, 'a', encoding='utf-8') as f:
            f.write('\n')
            f.write(data)

    def read_csv(self, file, delimeter):
        with open(file) as csv_f:
            cnt = -1
            rows = csv.reader(csv_f, delimiter=delimeter)
            for r in rows:
                if cnt == -1:
                    print(f'{" | ".join(r)}')
                else:
                    print(f'{r[0]} | {r[1]}')
                cnt += 1
            print(f'{cnt} lines')

    def sum_of_line(self, data):
        # 'Кёльн 150€ + 36€ + 43€ + 105€ + 10€ + 13.5€ + 8€ + 14€ + 7.5€ + 20€ + 5€ + 45€'
        # replace all '+' and Substitute multiple whitespace with single whitespace
        data = ' '.join(data.replace('+', ' ').split())
        data = data.replace('€', '').split(' ')
        index = 0
        # find index of number
        for index in range(0, len(data)):
            try:
                int(data[index])
            except ValueError:
                continue
            else:
                break

        # slice to have only numbers
        numbers_line = [eval(i) for i in data[index::]]
        # slice to have only words
        reason = ' '.join(data[:index:])
        return {'Reason': reason, 'Expense': sum(numbers_line)}

    def process_file_and_data(self):
        pass

print("--------------------------------")
text_file = File()
#write_to_file("new.txt", "")
text_file.read_file_by_lines('data/expenses.txt')
#read_file('data/expenses.txt')

print(text_file.modified_data)

#match(".", "*.t*")
#get_file_attrs(".")