import csv


def main():
    days = dict()
    a = 0
    b = 0
    days['0'] = dict()
    with open('5_average_prediction.csv', 'r') as file:
        lines = list(csv.reader(file))

        for line in lines:
            days[str(a)]['real'] = line[0]

            days[str(a+1)]['predicted'] = line