import csv
import requests
import collections, re
from datetime import datetime
from lxml import html
from multiprocessing import Manager, cpu_count, Lock, Pool


def main():
    ticker = 'MSFT US Equity'
    print('%i CPU' % cpu_count())
    pool = Pool(processes=cpu_count())

    manager = Manager()
    words = manager.list()
    bags = manager.dict()

    lock = Lock()

    with open('ms_equity.csv', 'r') as ms_equity:
        reader = csv.reader(ms_equity)

        for row in list(reader):
            # ticker = row[0]
            date = row[1]
            bags[(ticker, date)] = dict()

    header = True
    i = 0
    with open('articles.csv', 'r') as ms_articles:
        reader = csv.reader(ms_articles)
        start = datetime.now()
        for row in list(reader):
            if header:
                header = False
                continue
            # i += 1
            url = row[0]
            date = row[3]
            if i > 5:
                break

            if (ticker, date) in bags:
                pool.apply(func=get_sumbag, args=(url, bags, words, date, ))

    pool.close()
    pool.join()

    words = list(set(words))

    with open('result.csv', 'w+') as csv_file:
        field_names = ['ticker', 'date']
        field_names += words
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        print(len(bags))
        for key, bag in bags.items():
            ticker = key[0]
            date = key[1]

            for word in words:
                if word not in bag:
                    bag[word] = 0

            bag['ticker'] = ticker
            bag['date'] = date
            writer.writerow(bag)

    print('Total Operation took: %s' % str(datetime.now() - start))


def get_sumbag(url, bags, words, date):


    ticker = 'MSFT US Equity'
    r = requests.get(url)

    tree = html.fromstring(r.content)

    content = tree.xpath('//p[@class="story-body-text story-content"]/text()')

    bagsofwords = [collections.Counter(re.findall(r'\w+', txt.lower()))
                   for txt in content]

    sumbags = dict(sum(bagsofwords, collections.Counter()))

    # remove articles & common be-verbs
    removals = list()
    with open('stopwords.txt', 'r') as stop_words:
        for line in stop_words:
            line = line[:-1]
            removals.append(line)

    bag = dict()
    for key in sumbags.keys():
        if key not in removals and sumbags[key] > 1:
            bag[key] = sumbags[key]

    words += bag.keys()

    if len(bags[(ticker, date)]) is 0:
        bags[(ticker, date)] = bag

    # else:
    #     tempDict = {x:y for x in bags[(ticker, date)]}
    # else:
    #     tempDict = {x:y for x in bags[(ticker, date)]}
    #     bags[(ticker, date)] = {k: tempDict.get(k, 0) + bags.get(k, 0) for k in set(tempDict) | set(bags)}

    print('Sumbag Length: %i' % len(bag))

if __name__ == '__main__':
    main()
    # test()