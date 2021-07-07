# Installation
If this is the first time your are using the
program, complete these steps to include libraries

#### Copy-Paste This code into a terminal
##### Windows:
``py -m venv .venv``

##### Linux:
``python3 -m venv .venv``<br>

##### Next Steps for all operating systems
Select .venv as python interpreter<br>
``pip install bs4``<br>
``pip install nltk``<br>
Insert into imports in wikipedia_game_algorithm.py:<br>
``import nltk``<br>
Insert into \_\_init\_\_:<br>
``nltk.download("wordnet")``<br>
Run once to download wordnet library<br>
Then Delete:<br>
``import nltk``<br>
``nltk.download("wordnet")``

# To run program
**main.py file is already setup**, but to run program:<br>
Initialize WikipediaGameAlgorithm with the string of your desired end link and **make sure it exists and is not a portal**, like so:<br>
``algorithm = WikipediaGameAlgorithm("your ending wikipedia link")``<br>
Then run path_to_end_link on your WikipediaGameAlgorithm object using the string of your starting link, like so:<br>
``algorithm.path_to_end_link("your starting wikipedia link")``<br>

Then just run the program
