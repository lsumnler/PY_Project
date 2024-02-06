"""Bagels, by Al Sweigart @ al@inventwithpython.com
A deductive logic game where you must guess a number Based on clues.
View this code at https://nostarch.cm/Big-book-small-python-projects
A version of this gameis featured in the book "Invent your own 
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3  # (!)  Try setting this to 1 or 10:
MAX_GUESSES = 10    # (!) Try setting this to 1 or 100

def main():
    print('''Bagels a deductive logic game.
          By Al Sweigart al@inventwithpython.com
          
          I am thinking of a {} digit number with no re[eated digits.
          Try to guess what it is.  Here are some clues:
            Pico        One digit is correct but in the wrong position.end
            Fermi       One digit is correct and in the right position.
            Bage;s      No digit is correct. 
          For example, if the secret number is 248 and your guess was 841, the
          clues would be Fermi Pico.'''.format(NUM_DIGITS))