# MTGDeckHelper
a program where you can input your mana values and determine the mana needed for your deck. 
the outline pseudo code is as follows:

# Define Variables:
- deck_size: Integer, size of the deck. (60 for standard, 100 for commander or custom decks)
- mana_types: List, types of mana (blue, black, red, white, green, clear).
- card_data: Dictionary or list to store mana cost and type for each card.

# Input Deck Data:
- Prompt user to input deck_size.
- Prompt user to input the number of different mana types and their names.
- For each card in the deck, input mana cost and type, storing it in card_data.

# Calculate Mana Requirements:
- Analyze card_data to determine the proportion of each mana type.
- Use statistical methods (like probability calculations) to estimate the optimal number of each land type needed.

# Output Calculation Results:
- Display the suggested number of each land type to the user.

# Save to File:
- Provide an option to save the results in a CSV or text file.
- Use Python's csv module or file handling methods to write the data to a file.

# Refinement and Testing:
- Refine the code, test with different deck configurations.
- Consider adding features like importing deck data from a file.

# Python Libraries to Consider:
- csv for file operations.
- statistics or numpy for more complex statistical analysis (if needed).

# Here's a more detailed approach to this aspect:
## Modeling Card Draw Probability:
For each card, calculate the probability of drawing enough lands to play it at any given turn.
Consider the deck's composition and the order in which cards are drawn.

## Accounting for Mana Reusability:
Since mana is reusable, the probability model should reflect that once a land is drawn, it remains available for future turns.
This affects the probability of playing higher-cost cards in later turns.

## Sequential Draw and Play Considerations:
Implement a sequential model where the probability of drawing a specific mana type is adjusted after each draw.
Factor in the probability of having already drawn certain mana types in previous turns.

## Optimizing Land Count:
Use your model to determine the optimal number of each land type, balancing the need to play cards of different mana costs effectively.
Run simulations or use iterative methods to find the most effective land distribution.

## Python Libraries and Techniques:
Consider using Python libraries like numpy for numerical calculations and itertools for permutations and combinations.
You may also explore Monte Carlo simulations for more complex probability assessments.

## Saving and Analyzing Results:
Save your probability calculations and land distribution suggestions in a CSV or text file for analysis and review.
Include both the raw data and summary statistics for easy interpretation.