# -*- coding: utf-8 -*-
"""daily challenge

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Skti8xK8dNNTrSBjjz0icyR0lDPjFbtG

Instructions
Given a “Matrix” string:

7ii
Tsx
h%?
i #
sM
$a
#t%
^r!


The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
A grid means that you could potentially break it into rows and columns, like here:

7	i	i
T	s	x
h	%	?
i		#
s	M
$	a
#	t	%
^	r	!


Matrix: A matrix is a two-dimensional array. It is a grid of numbers arranged in rows and columns.
To reproduce the grid, the matrix should be a 2D list, not a string



To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

Using his technique, try to decode this matrix.

Hints:
Use
● lists for storing data
● Loops for going through the data
● if/else statements to check the data
● String for the output of the secret message

Hint (if needed) : Look at the remote learning “Matrix” video.
"""

matrix_string = """7ii
Tsx
h%?
i #
sM
$a
#t%
^r!"""

matrix = []
for row in matrix_string.split('\n'):
    matrix.append(list(row))

decrypted_message = ""
num_cols = max(len(row) for row in matrix)

for col in range(num_cols):
    for row in range(len(matrix)):
        if col < len(matrix[row]):
            char = matrix[row][col]
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                decrypted_message += char
            elif len(decrypted_message) > 0 and decrypted_message[-1].isalpha():
                decrypted_message += " "

decrypted_message