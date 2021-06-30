"""Import"""
import re
import urllib.request
from bs4 import BeautifulSoup
class WikipideaGameAlgorithm:
    """Housing For Anything Wikipedia Game Algorythm Related"""
    def pathmaker(self, starting_url, ending_url):
        """Shortest Path To Final Word Function"""
        starting_web_url = urllib.request.urlopen(starting_url)
        ending_web_url = urllib.request.urlopen(ending_url)

        starting_html = starting_web_url.read()
        ending_html = ending_web_url.read()

        starting_html = BeautifulSoup(starting_html, 'html.parser')
        ending_html = BeautifulSoup(ending_html, 'html.parser')

        starting_web_links = []
        for link in starting_html.find_all('a', href=True):
            starting_web_links.append(link.get('href'))

        cleaned_links = []
        for link in starting_web_links:
            if re.search('^/wiki/[^:]*$', link):
                cleaned_links.append(link)
        print(cleaned_links[:20])

    def __init__(self):
        pass
        