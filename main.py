"""Main File"""
import os
from wikipedia_game_algorithm import WikipideaGameAlgorithm

os.system('powershell clear')

algorithm = WikipideaGameAlgorithm("https://en.wikipedia.org/wiki/Banana")
link = algorithm.get_most_similar_link("https://en.wikipedia.org/wiki/Custard")

print(link)
