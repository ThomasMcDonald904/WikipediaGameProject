"""Import"""
import re
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import wordnet


class WikipideaGameAlgorithm:
    """Housing For Anything Wikipedia Game Algorythm Related"""

    def __init__(self, end_url):
        end_word = re.sub('https://en.wikipedia.org/wiki/', '', end_url)
        self.end_url = end_url
        try:
            self.end_word_synset = wordnet.synsets(end_word)[0]
        except IndexError:
            print("End Word Not In WordNet Library")
            exit()


    def get_most_similar_link(self, url, past_links):
        """Initial Link"""      
        starting_web_url = urllib.request.urlopen(url)
        starting_html = starting_web_url.read()
        starting_html = BeautifulSoup(starting_html, 'html.parser')

        starting_web_links = []
        for link in starting_html.find_all('a', href=True):
            starting_web_links.append(link.get('href'))

        cleaned_links = []
        for link in starting_web_links:
            if re.search('^/wiki/[^:#%]*$', link) and not re.search('_\(identifier\)', link):# pylint: disable=anomalous-backslash-in-string
                cleaned_links.append(link)
        word_links = []
        for link in cleaned_links:
            word_links.append(re.sub(r'/wiki/', '', link))
        word_links = list(dict.fromkeys(word_links))

        cleaned_word_links = []
        for word in word_links:
            if not f"https://en.wikipedia.org/wiki/{word}" in past_links:
                cleaned_word_links.append(word)

        link_synsets = []
        for link in cleaned_word_links:
            result = wordnet.synsets(link)
            if result != []:
                link_synsets.append([link, result[0]])


        ratings = []

        for item in link_synsets:
            rating = self.end_word_synset.wup_similarity(item[1])
            ratings.append([item[0], rating])

        ratings.sort(key=lambda l:l[1], reverse=True)

        best_link = ratings[0][0]
        best_link_rating = ratings[0][1]
        full_best_url = f"https://en.wikipedia.org/wiki/{best_link}"
        return full_best_url, best_link_rating

                

    def get_path_to_end_link(self, url, print_path=True, chart=True):
        """Method To Get Path from URL To Final URL """
        current_url = url
        past_links = [current_url]
        while not current_url == self.end_url and not current_url == "":
            current_url, current_url_rating = self.get_most_similar_link(current_url, past_links)
            if current_url != "":
                past_links.append(current_url)
            if print_path and chart:
                print(current_url + " - " + str(round(current_url_rating, 4)))
            

        if current_url == "":
            print("End URL could not be reached :-(")
        else:
            print("End URL Reached!")
