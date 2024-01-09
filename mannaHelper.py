#import data
from scipy.stats import hypergeom
import pandas as pd
import csv
import sys, os

def main():
    #prompt the user for how they are going to input their informaiton
    deck_option = input("Are you creating a new deck Y, N, Pull?: ").strip().lower()

    #If a new deck and not created, prompt the user for the amount of mana and each card. 
    if deck_option == "y":
        deck_name = input("What is the deck name: ").strip()
        deck_size, color_list, land_count, deck_spells = deck_info()

        #save general deck information to a text file
        file = open(deck_name+".txt", "w")
        file.write(f"deck_size:{deck_size}\n")
        file.write(f"color_list:{', '.join(color_list)}\n")
        file.write(f"land_count:{', '.join(land_count)}\n")

        #save the df to a cvs file
        deck_spells.to_csv(deck_name+'.csv',index=False)

    elif deck_option == "n":
        deck_list = []
        with open("deck_list.txt") as file:
            for line in file:
                deck_list.append(line.rstrip())
        print("You have the following deck options: ")
        i = 0
        for deck in sorted(deck_list):
            i += 1
            print(deck,"| Deck number: ",i)
        chosen_one = int(input("whitch deck do you want? choose a number: "))
        deck_size, color_list, land_count, deck_spells = pull_info(deck_name[chosen_one])

    elif deck_option == "pull":
        while True:
            deck_name, opt1, opt2 = input('What is the name of your file?, do you have an info file?, do you have a csv? (Y or N):').lower().split(',')
            deck_size, color_list, land_count, deck_spells = pull_info(deck_name, opt1, opt2)
            if deck_name == 'exit':
                print('Exiting program')
                sys.exit()
            else:
                break

    else:
        print("Not an option, Exiting the program")
        sys.exit()

    print("Completed, stop here")


def check_num(string=""):
        while True:
            try:
                num = int(input(string))
                return num 
            except ValueError:
                print("Invalid input. Please enter a number.")

def pull_info(filename, info_file = 'y', card_list = 'y'):
    try:
        if info_file == 'y':
            #pull information from the text file
            info = []
            with open(filename+'.txt', "r") as file:
                lines = file.readlines()
            for line in lines:
                colon_index = line.find(':')
                # If there's a colon in the string
                if colon_index != 1:
                    # Remove everything before the colon (and the colon itself)
                    line = line[colon_index + 1:]
                info.append(line.strip())  # Add each line to the info list
            deck_size = info[0]
            color_list = info[1].split(',')
            land_count = info[2].split(',')
        else:
            deck_size, color_list, land_count = '',[],[]

        if card_list == 'y':
            #pull information from cvs file
            deck_spells = pd.read_csv(filename+'.csv', index_col=0)
        else:
            deck_spells = []

        return deck_size, color_list, land_count, deck_spells
    except:
        print("Error: pull wasn't able to exicute")
        sys.exit()


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
        'collorless': [],
        'Total Mana': []
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
            total_mana += new_row[mana]
        new_row['Total Mana'] = total_mana
        deck_spell_df = deck_spell_df._append(new_row, ignore_index=True)
        
    return deck_size, color_list, land_count, deck_spell_df
    
def deck_land_stats(deck_size, land_count):
    # Assuming land_count is a dictionary where the key is the mana type
    # and the value is the count of that land type
    all_land = sum(land_count.values())  # Sum all land inputted
    
    # Convert land_count to a DataFrame
    land_count_df = pd.DataFrame(land_count.items(), columns=['Mana', 'Count'])

    # Calculate percent_of_deck and probability for each mana type
    land_count_df['percent_of_deck'] = (land_count_df['Count'] / deck_size) * 100
    land_count_df['probability'] = (hypergeom.pmf(1, deck_size, land_count_df['Count'], 7))*100
    
    percent_land = (all_land / deck_size) * 100

    #print values
    print(f"Your mana is {all_land}% of your deck. It's recommended 40% land or {int(deck_size*.4)} cards.")
    for index, row in land_count_df.iterrows():
        print(f"The percent of {row['Mana']} mana in your deck is {int(row['percent_of_deck'])}%")
        print(f"The probability of you picking up a {row['Mana']} mana at the start is {int(row['probability'])}%")

    return land_count_df, percent_land

def deck_spell_stats(spells_df, land_df, deck_size,turn = '10'):
    for mana in land_df:
        spell_df[f'{mana}Mana Probability in 10'] = (hypergeom.pmf(1, deck_size, land_count_df['Count'], 7))*100
    pass

if __name__ == '__main__':
    main()