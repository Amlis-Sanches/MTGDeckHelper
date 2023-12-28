'''
# Define Variables:
- deck_size: Integer, size of the deck. (60 for standard, 100 for commander or custom decks)
- mana_types: List, types of mana (blue, black, red, white, green, clear).
- card_data: Dictionary or list to store mana cost and type for each card.

# Input Deck Data:
- Prompt user to input deck_size.
- Prompt user to input the number of different mana types and their names.
- For each card in the deck, input mana cost and type, storing it in card_data.
'''

#import data
from scipy.stats import hypergeom
import pandas as pd
import sys

def main():
    YN = input("For a new deck? Y or N: ")
    if YN == "Y":
        deck_name = input("What is the deck name: ")
        deck_size, color_list, land_count, deck_spells = deck_info()
    elif YN == "N":
        pass
    else:
        print("Not an option, Exiting the program")
        sys.exit()

def check_num(string):
        while True:
            try:
                num = int(input(string))
                return num 
            except ValueError:
                print("Invalid input. Please enter a number.")

def check_mana(user_input):
    mana_types = user_input.lower().split(',')
    for mana in mana_types: 
        match mana:
            case "black"|"blue"|"white"|"green"|"red":
                check = True
            case "w"|"u"|"b"|"g"|"r":
                check = True
            case _ :
                check = False
                return False
    if check == True: 
        return mana_types

def deck_info():
    #get the size of the deck they will be making. 
    deck_size = check_num("What is your deck size? ")

    while True:
        color_list = check_mana(input("What mana types are in your deck? (separtate with ,) "))
        if color_list





'''
# Calculate Mana Requirements:
- Analyze card_data to determine the proportion of each mana type.
- Use statistical methods (like probability calculations) to estimate the optimal number of each land type needed.
'''
def probability_count(deck_size, lands, turns = '7', lands_needed = '1'):
    # Calculate the probability of drawing number of lands needed in how many turns
    prob = hypergeom.pmf(lands_needed, deck_size, lands, turns)

'''
# Save to File:
- Provide an option to save the results in a CSV or text file.
- Use Python's csv module or file handling methods to write the data to a file.
'''
def save_info():
    pass


if __name__ == '__main__':
    main()