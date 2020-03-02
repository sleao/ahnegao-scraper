from scraper import Scraper
import argparse

parser = argparse.ArgumentParser(
  prog='Galdêncio',
  description='A simple scraper for Ahnegao.com.br',
  allow_abbrev=False
)

group = parser.add_mutually_exclusive_group()

group.add_argument(
  '-p', '--pages',
  nargs='+',
  help="set the number of pages to scrape"
)

parser.add_argument(
  '-c', '--clear',
  help='clear the cache'
)

group.add_argument(
  '-s', '--sentry',
  nargs="?",
  help='enable sentry mode'
)

args = parser.parse_args()
print(args.sentry)