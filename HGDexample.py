# might want to use hypergeometric distribution instead of random.choice
# https://en.wikipedia.org/wiki/Hypergeometric_distribution
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.hypergeom.html
# https://stackoverflow.com/questions/35766647/how-to-use-scipy-stats-hypergeom-pmf
        
from scipy.stats import hypergeom

# Define parameters for the hypergeometric distribution
N = 60  # Total number of cards in the deck
K = 5   # Total number of red lands in the deck
n = 10  # Number of cards drawn (for example, first 10 draws)
k = 2   # Number of red lands we want to draw

# Calculate the probability of drawing exactly 2 red lands in 10 draws
prob = hypergeom.pmf(k, N, K, n)

# Define parameters for the hypergeometric distribution
N = 60  # Total number of cards in the deck
K = 1   # Total number of red lands in the deck
n = 10  # Number of cards drawn (for example, first 10 draws)
k = 1   # Number of red lands we want to draw

# Calculate the probability of drawing exactly 2 red lands in 10 draws
prob2 = hypergeom.pmf(k, N, K, n)

print(f"Probability of drawing exactly {k} red lands in {n} draws: {prob*100:.2f}%")
print(f"Probability of drawing exactly {k} red cards in {n} draws: {prob2*100:.2f}%")