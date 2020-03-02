from bs4 import BeautifulSoup
import requests
import pickle
import sys
import re

REGEX = r'(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?'
BASE_URL = "https://www.ahnegao.com.br/c/videos"

class Scraper:
  def __init__(self):
    self.lst = self.loadCache()

  def __del__(self):
    self.saveCache()

  def _saveCache(self):
    arq = open('cache', 'wb')
    pickle.dump(self.lst, arq)

  def _loadCache(self):
    lst = pickle.load(open('cache', 'rb'))
    return lst

  def _clearCache(self):
    self.lst = []
    self.saveCache()
    return True

  def _addToCache(self, link):
    video_id = link.split('/')[-1]
    self.lst.append(video_id)

  def scrape(self, page=''):
    links = []
    if page != '': url = BASE_URL+f'/pag/{page}'
    else: url = BASE_URL
    soup = BeautifulSoup(requests.get(url).text, features="html.parser")
    for link in soup.find_all('iframe'):
      a = link.get('src')
      if a.split('/')[-1] not in self.lst:
        a = re.sub('/embed', '', a)
        links.append(a)
        self._addToCache(a)
    return links


  def run(self, pages=[]):
    r = []
    for page in pages:
        r.append(self.scrape(page))
    return r


if __name__ == "__main__":
  print(Scraper().run())