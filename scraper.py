from bs4 import BeautifulSoup
import requests
import pickle
import re

# REGEX = r'(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?'
BASE_URL = "https://www.ahnegao.com.br/c/videos"

class Scraper:
  def __init__(self):
    self.lst = self._loadCache()

  def __del__(self):
    self._saveCache()

  def _saveCache(self):
    arq = open('cache', 'wb')
    pickle.dump(self.lst, arq)

  def _loadCache(self):
    try:
      lst = pickle.load(open('cache', 'rb'))
      return lst
    except:
      return []

  def _clearCache(self):
    self.lst = []
    self._saveCache()
    return True

  def _addToCache(self, link):
    video_id = link.split('/')[-1]
    self.lst.append(video_id)

  def _scrapeSoup(self, soup):
    links = []
    for link in soup.find_all('iframe'):
      a = link.get('src')
      if a.split('/')[-1] not in self.lst:
        a = re.sub('/embed', '', a)
        links.append(a)
        self._addToCache(a)
    return links

  def scrape(self, page='1'):
    url = BASE_URL+f'/pag/{page}'
    soup = BeautifulSoup(requests.get(url).text, features="html.parser")
    links = self._scrapeSoup(soup)
    return links


  def run(self, pages=[]):
    r = []
    for page in pages:
        r.append(self.scrape(page))
    return r


if __name__ == "__main__":
  print(Scraper().scrape())