import csv
import os
import math
from datetime import datetime


# def main():
#     found = list()
#     field_names = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close']
#     with open('/Users/Justin/Downloads/Commodity.csv', 'r') as file:
#         for line in file:
#             row = line.split(',')
#             ticker = row[0]
#
#             with open(('classified_csv/%s.csv' % ticker), 'a+') as csvFile:
#                 writer = csv.DictWriter(csvFile, fieldnames=field_names)
#                 if ticker not in found:
#                     writer.writeheader()
#                     found.append(ticker)
#
#                 writer.writerow({
#                     'Ticker': row[0],
#                     'Date': row[1],
#                     'Open': row[2],
#                     'High': row[3],
#                     'Low': row[4],
#                     'Close': row[5][:-2]
#                 })


def find_company(k_word):
    lines = list()
    with open('/Users/Justin/Downloads/Equity.csv', 'r') as file:
        found = False
        for idx, line in enumerate(file):
            line = line.split(',')

            if found:
                if k_word in line[0]:
                    lines.append(line)
                else:
                    break

            if not found:
                print(idx)
                if k_word in line[0]:
                    lines.append(line)
                    found = True

    with open(('result/%s.csv' % k_word), 'w+') as file:
        for line in lines:
            input_string = ','.join(line)
            file.write(input_string)

    sort_data(k_word=k_word)


def sort_data(k_word):
    rows = dict()

    with open(('result/%s.csv' % k_word), 'r') as file:
        reader = list(csv.reader(file))
        min_date = datetime.now()

        for line in reader:
            date = datetime.strptime(line[1], '%Y-%m-%d')
            if date < min_date:
                min_date = date

        for line in reader:
            date = datetime.strptime(line[1], '%Y-%m-%d')

            diff = (date - min_date).days

            open_price = line[2]
            close = line[5]
            avg = (float(open_price) + float(close)) / 2
            avg = math.ceil(avg * 1000) / 1000
            rows[diff] = avg

    with open(('result/%s_sorted.csv' % k_word), 'w+') as file:
        field_names = ['time', 'data']
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()

        for key, item in rows.items():
            writer.writerow({
                'time': key,
                'data': item
            })

if __name__ == '__main__':
    find_company(k_word='MSFT')
