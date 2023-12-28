import mannaHelper as mh
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Add a new value to column 'A'
df.loc[3, 'A'] = 7

print(df)
