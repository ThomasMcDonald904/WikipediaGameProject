"""Main File"""
import os
from wikipedia_game_algorithm import WikipideaGameAlgorithm

os.system('powershell clear')

algorithm = WikipideaGameAlgorithm()

algorithm.pathmaker("https://en.wikipedia.org/wiki/Pangolin", "https://en.wikipedia.org/wiki/Claw")
