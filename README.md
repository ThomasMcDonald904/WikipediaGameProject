# Installation
If this is the first time your are using the
program complete these steps to include libraries

#### Copy-Paste This code into a new terminal
##### Windows:
``py -m venv .venv``

##### Linux:
``python3 -m venv .venv``<br>
Select .venv as python interpreter
``pip install bs4``
``pip install nltk``

##### Next Steps for all operating systems
Insert into imports:
``import nltk``
Insert into \_\_init\_\_:
``nltk.download("wordnet")``
Run once to download wordnet library
Then Delete:
``import nltk``
``nltk download``

# To run program
**main.py file is already setup**, but to run program:
Initialize WikipediaGameAlgorithm with the string of your desired end link and make sure it exists and is not a portal, like so:
``algorithm = WikipediaGameAlgorithm("your ending wikipedia link")``
Then run path_to_end_link on your WikipediaGameAlgorithm object using the string of your starting link, like so:
``algorithm.path_to_end_link("your starting wikipedia link")``

Then just run the program
