# -*- coding: utf-8 -*-
"""daily challenge

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fySuRKBVAgEllCrAJoi8EkTi0959S9B-

Challenge 1 : Sorting


Instructions
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Use List Comprehension
Example:

Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world
"""

# prompt: write a program that accepts a comma separated sequence of words

def sort_words():
  """Accepts a comma-separated sequence of words and prints them in alphabetical order."""
  words = input("Enter comma-separated words: ")
  word_list = words.split(',')
  sorted_words = sorted(word_list)
  print(','.join(sorted_words))

if __name__ == "__main__":
  sort_words()

"""Challenge 2 : Longest Word
Instructions
Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
"""

def find_longest_word(sentence):
  """Finds the longest word in a sentence.

  Args:
      sentence: The input sentence.

  Returns:
      The longest word in the sentence.
  """
  words = sentence.split()
  longest_word = ""
  for word in words:
    if len(word) > len(longest_word):
      longest_word = word
  return longest_word