from __future__ import print_function
from .generalized import Scraper


class Baidu(Scraper):
    """Scrapper class for Baidu"""

    def __init__(self):
        Scraper.__init__(self)
        self.url = 'https://www.baidu.com/s'
        self.defaultStart = 0
        self.queryKey = 'wd'
        self.startKey = 'pn'
        self.name = 'baidu'

    @staticmethod
    def parse_response(soup):
        """ Parse the response and return set of urls
        Returns: urls (list)
                [[Tile1,url1], [Title2, url2],..]
        """
        urls = []
        for div in soup.findAll('div', {'class': 'result'}):
            title = div.h3.a.getText()
            url = div.h3.a['href']
            urls.append({'title': title, 'link': url})

        print('Baidu parsed: ' + str(urls))

        return urls
