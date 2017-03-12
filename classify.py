import csv
import os
import math
from datetime import datetime


found = list()
def main():
    fieldNames = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close']
    with open('/Users/Justin/Downloads/Commodity.csv', 'r') as file:
        for line in file:
            row = line.split(',')
            ticker = row[0]

            with open(('classified_csv/%s.csv' % ticker), 'a+') as csvFile:
                writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
                if ticker not in found:
                    writer.writeheader()
                    found.append(ticker)

                writer.writerow({
                    'Ticker': row[0],
                    'Date': row[1],
                    'Open': row[2],
                    'High': row[3],
                    'Low': row[4],
                    'Close': row[5][:-2]
                })


def find_tesla():
    lines = list()
    with open('/Users/Justin/Downloads/Equity.csv', 'r') as file:
        found = False
        for idx, line in enumerate(file):
            line = line.split(',')

            if found and 'MSFT' in line[0]:
                lines.append(line)

            if found and 'MSFT' not in line[0]:
                break

            if 'MSFT' in line[0] and not found:
                lines.append(line)
                found = True

            if not found:
                print(idx)

    with open('ms_equity.csv', 'w+') as file:
        for line in lines:
            str = ','.join(line)
            file.write(str)
            # print(line)


def sort_data():
    rows = dict()

    with open('ms_equity.csv', 'r') as file:
        reader = list(csv.reader(file))
        min_date = datetime.now()
        # max_date = datetime.strptime(reader[0][0], '%Y-%m-%d')
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

    with open('ms_equity_avg.csv', 'w+') as file:
        field_names = ['time', 'data']
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()

        for key, item in rows.items():
            writer.writerow({
                'time': key,
                'data': item
            })




if __name__ == '__main__':
    # main()
    # find_tesla()
    sort_data()