from bs4 import BeautifulSoup
from urllib.request import urlopen

r = urlopen("https://google.com")
soup = BeautifulSoup(r, "html.parser")
print(soup)

