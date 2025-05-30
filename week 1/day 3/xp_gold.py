# -*- coding: utf-8 -*-
"""xp gold

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19kOFG582E1hrJnNMv9EKMBZ0wZRmR89f

Exercise 1: Birthday Look-up
Instructions
Create a variable called birthdays. Its value should be a dictionary.
Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
Ask the user to give you a person’s name and store the answer in a variable.
Get the birthday of the name provided by the user.
Print out the birthday with a nicely-formatted message.
"""

birthdays = {
    "Albert Einstein": "1879/03/14",
    "Nelson Mandela": "1918/07/18",
    "Marie Curie": "1867/11/07",
    "Leonardo da Vinci": "1452/04/15",
    "Ada Lovelace": "1815/12/10"
}

print("Welcome!")
print("You can look up the birthdays of the people in the list!")

"""
Exercise 2: Birthdays Advanced
Instructions
Before asking the user to input a person’s name print out all of the names in the dictionary.
If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)
"""

name=input("Please enter a name:")
if name in birthdays:
  birthday = birthdays[name]
  print(f"{name}'s birthday is {birthday}.")
else:
  print(f"Sorry, I don't have {name}'s birthday.")

"""Exercise 3: Add Your Own Birthday
Instructions
Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
Ask the user for a person’s name – store it in a variable.
Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
Now add this new data into your dictionary.
Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.

"""

new_name = input("Enter a new person's name: ")
new_birthday = input("Enter their birthday (YYYY/MM/DD): ")
birthdays[new_name] = new_birthday


print("Here's the list of names:")
for name in birthdays:
    print(name)

name = input("Please enter a name: ")
if name in birthdays:
    birthday = birthdays[name]
    print(f"{name}'s birthday is {birthday}.")
else:
    print(f"Sorry, I don't have {name}'s birthday.")

"""Exercise 4: Fruit Shop
Instructions
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
write some code to calculate how much it would cost to buy everything in stock.
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

"""

items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_cost = 0
for item, details in items.items():
  price = details["price"]
  stock = details["stock"]
  item_cost = price * stock
  total_cost += item_cost
  print(f"The cost of all {item} in stock is: {item_cost}")


print(f"The total cost to buy everything in stock is: {total_cost}")