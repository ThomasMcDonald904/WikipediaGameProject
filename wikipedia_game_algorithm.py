"""Import"""
import re
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import wordnet

class WikipideaGameAlgorithm:
    """Housing For Anything Wikipedia Game Algorythm Related"""

    def __init__(self, end_url):
        end_word = re.sub('https://en.wikipedia.org/wiki/', '', end_url)
        self.end_url = end_url.lower()
        self.end_word_synset = wordnet.synsets(end_word)[0]


    def get_most_similar_link(self, url):
        """Initial Link"""
        starting_web_url = urllib.request.urlopen(url)
        starting_html = starting_web_url.read()
        starting_html = BeautifulSoup(starting_html, 'html.parser')

        starting_web_links = []
        for link in starting_html.find_all('a', href=True):
            starting_web_links.append(link.get('href'))

        cleaned_links = []
        for link in starting_web_links:
            if re.search('^/wiki/[^:#-%]*$', link):
                cleaned_links.append(link)
        word_links = []
        for link in cleaned_links:
            word_links.append(re.sub(r'/wiki/', '', link))
        word_links = list(dict.fromkeys(word_links))

        link_synsets = []
        for link in word_links:
            if not wordnet.synsets(link) == []:
                link_synsets.append(wordnet.synsets(link)[0])
            else:
                #print("Word Not In WordNet Library")
                word_links.remove(link)

        ratings = []
        for link in link_synsets:
            ratings.append(self.end_word_synset.wup_similarity(link))

        synset_ratings = zip(link_synsets, ratings)
        synset_ratings = list(synset_ratings)

        for i in range(len(synset_ratings)):
            synset_ratings[i] = list(synset_ratings[i])

        synset_ratings.sort(key=lambda l:l[1], reverse=True)

        best_link = str(synset_ratings[0][0].name())
        link_name = re.sub('\.n\.0\d+', '', best_link)
        full_best_url = f"https://en.wikipedia.org/wiki/{link_name}"
        if full_best_url == url:
            index = 0
            while full_best_url == url:
                best_link = str(synset_ratings[index][0].name())
                link_name = re.sub('\.n\.0\d+', '', best_link)
                full_best_url = f"https://en.wikipedia.org/wiki/{link_name}"
                index += 1
            return full_best_url
        else:
            return full_best_url

    def get_path_to_end_link(self, url, print_path=True):
        """Method To Get Path from URL To Final URL """
        current_url = url
        while not current_url == self.end_url:
            current_url = self.get_most_similar_link(current_url)
            if print_path:
                print(current_url)
        print("End URL Reached")
