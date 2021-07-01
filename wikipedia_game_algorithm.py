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
        except:
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
            if re.search('^/wiki/[^:#%]*$', link) and not re.search('_\(identifier\)', link):
                cleaned_links.append(link)
        word_links = []
        for link in cleaned_links:
            word_links.append(re.sub(r'/wiki/', '', link))
        word_links = list(dict.fromkeys(word_links))

        link_synsets = []
        for link in word_links:
            result = wordnet.synsets(link)
            if result != []:
                link_synsets.append([link, result[0]])


        ratings = []

        for item in link_synsets:
            rating = self.end_word_synset.wup_similarity(item[1])
            ratings.append([item[0], rating])

        ratings.sort(key=lambda l:l[1], reverse=True)

        # best_link = str(synset_ratings[0][0].name())
        # link_name = re.sub('\.n\.0\d+', '', best_link)
        # full_best_url = f"https://en.wikipedia.org/wiki/{link_name}"
        full_best_url = ""
        index = 0
        best_link_rating = 0
        while (full_best_url == "" or full_best_url in past_links) and index < len(ratings):
            best_link = ratings[index][0]
            best_link_rating = ratings[index][1]
            # link_name = re.sub('\.n\.0\d+', '', best_link)
            full_best_url = f"https://en.wikipedia.org/wiki/{best_link}"
            index += 1
        if not full_best_url in past_links:
            return full_best_url, best_link_rating
        else:
            return "", 0
        
            

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
