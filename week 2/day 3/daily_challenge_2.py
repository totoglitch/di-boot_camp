# -*- coding: utf-8 -*-
"""daily challenge 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16gaE-gVIMdRYn4XP9X0dNsX1sLHWJ7NJ

Instructions :
Consider this list

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
Look at this result :
{"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
You have to recreate the result using a translator module. Take a look at the googletrans module
"""

!pip install googletrans==4.0.0-rc1

from googletrans import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translator = Translator()

# Create an empty dictionary to store translations
translations = {}

# Iterate through the french words list and translate each word
for word in french_words:
  translated_word = translator.translate(word, dest='en').text
  translations[word] = translated_word

translations