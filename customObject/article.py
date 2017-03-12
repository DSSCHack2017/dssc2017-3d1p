from datetime import datetime


class Article(object):

    def __init__(self, web_url, snippet, keywords, pub_date):
        self.web_url = web_url
        self.snippet = snippet[:-4]
        self.keywords = keywords

        self.pub_date = datetime.strptime(pub_date[:10], '%Y-%m-%d')

    def stringify_date(self):
        self.pub_date = str(self.pub_date)