#import data
from scipy.stats import hypergeom
import pandas as pd
import sys

def main():
    YN = input("For a new deck? Y or N: ").strip().lower()
    if YN == "y":
        deck_name = input("What is the deck name: ")
        deck_size, color_list, land_count, deck_spells = deck_info()
    elif YN == "n":
        pass
    else:
        print("Not an option, Exiting the program")
        sys.exit()

def check_num(string=""):
        while True:
            try:
                num = int(input(string))
                return num 
            except ValueError:
                print("Invalid input. Please enter a number.")

def check_mana(user_input):
    #take the users input and seporate the colors and form a list. 
    mana_types = user_input.lower().strip().split(',')

    #check and make sure that all the values in the list are valid. 
    for mana in mana_types: 
        match mana:
            case "black"|"blue"|"white"|"green"|"red":
                check = True
            case "w"|"u"|"b"|"g"|"r":
                check = True
            case "exit":
                sys.exit()
            case _ : # if value isn't valid return false: 
                return False
    if check == True: 
        mana_types.append("colorless")
        return mana_types

def deck_info():
    #get the size of the deck they will be making. 
    deck_size = check_num("What is your deck size? ")

    #get a list of colors from the user. 
    while True:
        color_list = check_mana(input("What mana types are in your deck? (separtate with ,) "))
        if color_list != False: 
            break
    #get a count of lands for each color
    land_count = {}
    for mana in color_list:
        count = check_num(f"how many {mana} lands are there?")
        land_count[mana] = count

    data_outline = {
        'Card Name': [],
        'Copies': [],
        'white': [],
        'blue': [],
        'black': [],
        'green': [],
        'red': [],
        'collorless': []
    }
    deck_spell_df = pd.DataFrame(data_outline)
    while True:
        card_name = input("What's the name of the card or enter done: ").lower()
        if card_name == "done":
            break
        copies = check_num("How many copies are there? ")
        new_row = {'Card Name': card_name, 'Copies': copies}
        for mana in color_list:
            new_row[mana] = check_num(f"how many {mana} does this card take? ")
        deck_spell_df = deck_spell_df.append(new_row, ignore_index=True)
        
    return deck_size, color_list, land_count, deck_spell_df
    

    

    
    

    





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