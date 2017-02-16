import urllib
import urllib.request
import os
from bs4 import BeautifulSoup

def soup_factory(url):
    theurl = url
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup

main_soup = soup_factory('https://attach.io/startup-pitch-decks/')

decks_array = main_soup.findAll('div', {'class': 'company-cards'})

i = 0
for div in decks_array:
    title = div.find('h2').text
    print(title)
    url = div.find('iframe').get('src')
    single_soup = soup_factory(url)
    images_soup = single_soup.findAll('div', {'class': 'slide'})
    os.makedirs(title)
    for image in images_soup:
        img_url = image.find('img').get('data-full')
        print(img_url)
        file_name = str(i)
        i = i + 1
        imagefile = open(title + '/' + file_name + '.jpeg', 'wb')
        imagefile.write(urllib.request.urlopen(img_url).read())
        imagefile.close()
    i = 0
