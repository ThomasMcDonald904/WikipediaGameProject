"""Test For Similarity NLTK Algorithm"""
import os
from nltk.corpus import wordnet

os.system('powershell clear')

# Score denoting how similar two word senses are,
# based on the shortest path that connects the senses in the is-a (hypernym/hypnoym) taxonomy
felis = wordnet.synset("felis.n.01")
animalia = wordnet.synset("animalia.n.01")
carnivora = wordnet.synset("carnivora.n.01")

ant = wordnet.synset("ant.n.01")
termite = wordnet.synset("termite.n.01")

print("Path Similarity")
print(felis.path_similarity(animalia))
print(felis.path_similarity(carnivora))
print("---------------")
print('\n')


#Leacock-Chodorow Similarity: Return a score denoting how similar two word senses are,
# based on the shortest path that connects the senses (as above)
# and the maximum depth of the taxonomy in which the senses occur.
# The relationship is given as -log(p/2d)
# where p is the shortest path length and d the taxonomy depth.
print("Leacock-Chodorow Similarity")
print(felis.lch_similarity(animalia))
print(ant.lch_similarity(termite))
print("---------------")
print('\n')


#Wu-Palmer Similarity: Return a score denoting how similar two word senses are,
# based on the depth of the two senses in the taxonomy and
# that of their Least Common Subsumer (most specific ancestor node)
print("Wu-Palmer Similarity")
print(felis.wup_similarity(animalia))
print(ant.wup_similarity(termite))
print("---------------")


# print(syns.hyponyms())
# print(syns.definition())
