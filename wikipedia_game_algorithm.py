"""Import"""
import re
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import wordnet

class WikipideaGameAlgorithm:
    """Housing For Anything Wikipedia Game Algorythm Related"""

    def __init__(self, end_url):
        end_word = re.sub('https://en.wikipedia.org/wiki/', '', end_url)
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
        link_name = re.sub('.n.01', '', best_link)
        return f"https://en.wikipedia.org/wiki/{link_name}"

        # for i in link_synsets:
        #     link_synsets.append(self.end_word_synset.wup_similarity(i))
        # print(link_synsets)

    # def get_synset(self, wiki_url):
    #     word = re.sub('/wiki/', '', wiki_url)
    #     word = word.lower()
    #     try:
    #         word_synset = wordnet.synsets(word)[0]
    #     except:
    #         print("Your Wikipedia URL End Topic is not Compatible with the Wordnet Library")
    #     finally:
    #         exit()
    #     return word_synset
