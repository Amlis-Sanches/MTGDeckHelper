import random
import csv

# Initialize deck
deck = {'blue': 10, 'black': 8, 'red': 7, 'white': 5, 'green': 5, 'clear': 5}
deck_size = sum(deck.values())
probabilities = {}

# Calculate initial probabilities
for color in deck:
    probabilities[color] = deck[color] / deck_size

# Simulate draws and update probabilities
for turn in range(1, deck_size + 1):
    drawn_card = random.choice(list(deck.keys()))
    deck[drawn_card] -= 1
    deck_size -= 1
    for color in deck:
        probabilities[color] = deck[color] / deck_size if deck_size else 0
    print(f"Turn {turn}: {probabilities}")  # For debugging

# Save results to a file
with open('deck_probabilities.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Turn'] + list(deck.keys()))
    for turn, probs in enumerate(probabilities.values()):
        writer.writerow([turn + 1] + list(probs))


