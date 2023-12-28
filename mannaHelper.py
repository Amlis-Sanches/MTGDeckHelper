#import data
from scipy.stats import hypergeom
import pandas as pd
import sys

def main():
    YN = input("For a new deck? Y or N: ").strip().lower()
    if YN == "y":
        deck_name = input("What is the deck name: ").strip()
        deck_size, color_list, land_count, deck_spells = deck_info()
        land_count, percent_land = deck_land_stats(deck_size, land_count)

        #save general deck information to a text file
        file = open(deck_name+".txt", "w")
        file.write(f"deck_size:{deck_size}\n")
        file.write(f"color_list:{', '.join(color_list)}\n")
        file.write(f"land_count:{', '.join(land_count)}\n")
        file.write(f"percent_land:{percent_land}\n")

        #save the df to a cvs file
        deck_spells.to_csv(deck_name+'.cvs',index=False)

    elif YN == "n":
        print("Not currently avalible. Sorry")
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
    mana_types = user_input.lower().replace(' ','').split(',')

    #check and make sure that all the values in the list are valid. 
    for mana in mana_types:
        match mana:
            case "black"|"blue"|"white"|"green"|"red": #check if mana is spelled this way.
                check = True #set check to true but don't return yet
            case "wh"|"bl"|"bk"|"gr"|"rd": #check if mana is spelled this way.
                check = True #set check to true but don't return yet
            case "w"|"u"|"b"|"g"|"r": #check if mana is spelled this way.
                check = True #set check to true but don't return yet
            case "exit": #If wanting to exit the program. 
                sys.exit()
            case _ : # if value isn't valid return false: 
                return False
    if check == True: #Once all values have been checked return the mana list. 
        mana_types.append("colorless")
        return mana_types
    else:
        print("Error: values not accepted.")

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
        deck_spell_df = deck_spell_df._append(new_row, ignore_index=True)
        
    return deck_size, color_list, land_count, deck_spell_df
    
def deck_land_stats(deck_size, land_count):
    #land stats:
    all_land = 0
    for mana in land_count: #sum all land inputted
        all_land = land_count[mana] + all_land
        if mana not in land_count:
            land_count[mana] = {}
        land_count[mana][1] = land_count[mana]/deck_size
        num_of_lands = land_count[mana][0]
        land_count[mana][2] = hypergeom.pmf(1, deck_size, num_of_lands, 7)
    percent_land = (deck_size/all_land)*100

    #print values
    print(f"The percent of land in your deck is {percent_land}%. The standard is 40% land per deck")
    for mana in land_count:
        print(f"The percent of {mana} mana in your deck is {land_count[1, mana]}")
        print(f"The probability of you picking up a {mana} mana at the start is {land_count[2, mana]}")

    return land_count, percent_land

def probability_count(deck_size, lands, turns = '7', lands_needed = '1'):
    # Calculate the probability of drawing number of lands needed in how many turns
    prob = hypergeom.pmf(lands_needed, deck_size, lands, turns)

if __name__ == '__main__':
    main()