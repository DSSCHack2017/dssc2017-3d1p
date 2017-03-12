from multiprocessing import Pool, Manager
from customObject import Article
import requests
import csv
import os
import sys


def run(years, months):
    manager = Manager()
    article_list = manager.list()
    pool = Pool()

    for year in years:
        for month in months:
            pool.apply(func=fetch_data, args=(year, month, article_list,))

    pool.join()
    pool.close()

    # Sort the article based on the published date
    article_list = sorted(article_list, key=lambda article: article.pub_date)

    with open('result/articles.csv', 'w+') as csvFile:
        fieldNames = ['web_url', 'snippet', 'keywords', 'pub_date']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        writer.writeheader()

        for article in article_list:
            try:
                article.pub_date = str(article.pub_date)[:10]  # Write only YYYY-MM-DD
                writer.writerow(article.__dict__)

            except UnicodeEncodeError:
                # Sometimes this erro happens, and couldn't figure out why. But it happens very rarely
                pass


# Fetch data from NYT Url at specific time
# This is used ofr multiprocessing
def fetch_data(year, month, articles):

    # Keyword we are looking for
    k_word = 'microsoft'

    api_key = os.environ.get('api_key')
    # We are using formatting because it is not a simple get_request
    nyt_url = 'http://api.nytimes.com/svc/archive/v1/%i/%i.json' % (year, month)

    r = requests.get(nyt_url, params={'api-key': api_key})

    if r.status_code is 200:

        try:
            r = r.json().get('response')
            r = r.get('docs')

            for doc in r:

                keyword_list = ''
                found_word = False
                for keyword in doc.get('keywords'):
                    word = keyword.get('value').lower()

                    # Test if the word we are looking for is within the keywords
                    if k_word in word:
                        found_word = True
                    keyword_list += word + ','

                if not found_word:
                    continue

                keyword_list = keyword_list[:-1]

                article = Article(
                    web_url=doc.get('web_url').replace('\'', ''),
                    snippet=doc.get('snippet').replace('\'', ''),
                    keywords=keyword_list,
                    pub_date=doc.get('pub_date')
                )

                articles.append(article)

        except ValueError:
            pass

    print('Process %s - %s FINISHED' % (year, month))


if __name__ == '__main__':
    years = range(2007, 2018)
    months = range(1, 13)
    run(years=years,
        months=months)
