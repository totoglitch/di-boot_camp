# -*- coding: utf-8 -*-
"""daily challenge gold

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aOBaCByMyuuzZVhAGkkw8tmomDcaickP

Instructions
Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
Display a little cake as seen below:
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~

The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

Bonus : If they were born on a leap year, display two cakes !
"""

from datetime import datetime

def display_cake(candles):
    print("        ___iiiii___")
    print("       |:H:a:p:p:y:|")
    print("     __|___________|__")
    print("    |^^^^^^^^^^^^^^^^^|")
    print(f"    |:B:i:r:t:h:d:a:y:{'|' * (8 - candles)}")
    print("    |                 |")
    print("    ~~~~~~~~~~~~~~~~~~~")
    print(f"{'_' * candles}")


def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


birthdate_str = input("Enter your birthdate in DD/MM/YYYY format: ")
try:
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
except ValueError:
    print("Invalid date format. Please use DD/MM/YYYY.")
else:
    age = calculate_age(birthdate)
    candles = int(str(age)[-1])

    is_leap_year = (birthdate.year % 4 == 0 and birthdate.year % 100 != 0) or (birthdate.year % 400 == 0)

    display_cake(candles)
    if is_leap_year:
        print("\nHappy Leap Year Birthday!!\n")
        display_cake(candles)