from json import loads,dumps
from urllib2 import urlopen

def url(scraper_name):
  return "https://api.scraperwiki.com/api/1.0/scraper/getinfo?format=jsondict&name="+ \
  scraper_name+ \
  "&version=-1&quietfields=runevents%7Cdatasummary%7Cuserroles%7Chistory"

def getcode(scraper_name):
  return loads(urlopen(url(scraper_name)).read())[0]['code']

def demo():
  print getcode('rifidec')

if __name__ == "__main__":
  demo()
