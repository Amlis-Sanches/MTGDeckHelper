'''

'''
def main():
    deck_size, deck_type, card_data, land_data = deck_info()
    manna_calc(deck_size, deck_type, card_data)

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

def main():
    deck_size, deck_type, card_data, land_data = deck_info()


def dic(user_input):
    #takes a string and turns it into a dictionary
    dic = {}
    for i in user_input.split(','):
        dic[i.split(':')[0]] = i.split(':')[1]
    return dic

def deck_info():
    deck_size = int(input("Enter the size of the deck: "))
    deck_land = dic(input("Enter the color and number of lands in the deck: ")) #will give a dictionary
    Turns = 7 + int(input("Enter the number of turns you want to calculate: "))
    
    card_details = input("Enter the card name, mana cost, and type: ") #will give a dictionary

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