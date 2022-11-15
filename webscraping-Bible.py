import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

chapterCount = random.randint(1, 21)

if chapterCount < 10:
    webpage = f'https://ebible.org/asv/JHN0{str(chapterCount)}.htm'
else:
    webpage = f'https://ebible.org/asv/JHN{str(chapterCount)}.htm'

req = Request(webpage, headers=headers)
reading_webpage = urlopen(req).read()
soup = BeautifulSoup(reading_webpage,'html.parser')
page_verses = soup.findAll("div", attrs={"class": "main"})

for verse in page_verses:
    verse_list = verse.text.replace('''\xa0''', ' ').split('.')


my_verse = random.choice(verse_list[:-5])
print(f'Chapter {chapterCount} - Verse(s):{my_verse}')