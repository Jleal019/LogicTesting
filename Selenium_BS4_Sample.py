from bs4 import BeautifulSoup
from selenium import webdriver
import lxml # use lxml parser for speed
# sets options for browser
options = webdriver.FirefoxOptions()
options.add_argument('-headless')

# opens browser and downloads the page
url = "https://fdoh.maps.arcgis.com/apps/opsdashboard/index.html#/74c7375b03894e68920c2d0131eef1e6"
browser = webdriver.Firefox(firefox_options = options)
page = browser.get(url)
page_html = browser.page_source

soup = BeautifulSoup(page_html, 'lxml')

embers = soup.find_all('div')
print(embers)

# print(page_html)


# supposed to close the driver session completely but doesn't seem to actually work.
browser.stop_client()
browser.close()
