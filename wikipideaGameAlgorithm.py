from bs4 import BeautifulSoup
import urllib.request
import re
class WikipideaGameAlgorithm:
    def pathmaker(self, StartingURL, EndingURL):
        startingWebURL = urllib.request.urlopen(StartingURL)
        endingWebURL = urllib.request.urlopen(EndingURL)
        
        startingHTML = startingWebURL.read()
        endingHTML = endingWebURL.read()
        
        startingHTML = BeautifulSoup(startingHTML, 'html.parser')
        endingHTML = BeautifulSoup(endingHTML, 'html.parser')

        startingWebLinks = []
        for link in startingHTML.find_all('a', href=True):
            startingWebLinks.append(link.get('href'))

        cleanedLinks = []
        for link in startingWebLinks:
            if re.search('^/wiki/[^:]*$', link):
                cleanedLinks.append(link)
        

        print(cleanedLinks[:20])

    def __init__(self):
        pass
        