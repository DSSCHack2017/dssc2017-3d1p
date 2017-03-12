import csv
import requests
import collections, re
from datetime import datetime
from lxml import html
from multiprocessing import Manager, cpu_count, Lock, Pool


# This file is used to fetch data from NYTimes, or any news articles, and find the content.
# The content then is used to generate bag of words.
def main(ticker):
    start = datetime.now()
    pool = Pool(processes=cpu_count())

    manager = Manager()
    words = manager.list()
    bags = manager.dict()

    with open(('result/%s.csv' % ticker), 'r') as ms_equity:
        reader = csv.reader(ms_equity)

        for row in list(reader):
            date = row[1]
            bags[(ticker, date)] = dict()

    header = True
    with open('articles.csv', 'r') as ms_articles:
        reader = csv.reader(ms_articles)
        for row in list(reader):
            if header:
                header = False
                continue

            url = row[0]
            date = row[3]

            if (ticker, date) in bags:
                pool.apply(func=get_sumbag, args=(ticker, url, bags, words, date, ))

    pool.close()
    pool.join()

    words = list(set(words))

    # Write to CSV file
    with open(('result/%s_result.csv' % ticker), 'w+') as csv_file:
        field_names = ['ticker', 'date']
        field_names += words
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()

        for key, bag in bags.items():
            ticker = key[0]
            date = key[1]

            # Count 0 word, that are in the other articles
            for word in words:
                if word not in bag:
                    bag[word] = 0

            bag['ticker'] = ticker
            bag['date'] = date
            writer.writerow(bag)

    print('Total Operation took: %s' % str(datetime.now() - start))


def get_sumbag(ticker, url, bags, words, date):

    r = requests.get(url)

    tree = html.fromstring(r.content)

    content = tree.xpath('//p[@class="story-body-text story-content"]/text()')

    # Generate bag of words
    bag_of_words = [collections.Counter(re.findall(r'\w+', txt.lower())) for txt in content]

    sum_bag = dict(sum(bag_of_words, collections.Counter()))

    # remove articles & common be-verbs
    removals = list()
    with open('stopwords.txt', 'r') as stop_words:
        for line in stop_words:
            line = line[:-1]
            removals.append(line)

    bag = dict()
    for key in sum_bag.keys():
        if key not in removals and sum_bag[key] > 1:
            bag[key] = sum_bag[key]

    words += bag.keys()

    if len(bags[(ticker, date)]) is 0:
        bags[(ticker, date)] = bag

    # This was supposed to merge if there were multiple articles on the same date
    # else:
    #     tempDict = {x:y for x in bags[(ticker, date)]}
    # else:
    #     tempDict = {x:y for x in bags[(ticker, date)]}
    #     bags[(ticker, date)] = {k: tempDict.get(k, 0) + bags.get(k, 0) for k in set(tempDict) | set(bags)}

    print('Sumbag Length: %i' % len(bag))

if __name__ == '__main__':
    main(ticker='US MSFT')  # Needs to be found and replaced
