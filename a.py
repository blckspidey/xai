import pickle

file_path = "s01.dat"   # apna file path yaha daalo

with open(file_path, "rb") as f:
    data = pickle.load(f, encoding="latin1")

import pandas as pd

df = pd.DataFrame(data['labels'], columns=['valence','arousal','dominance','liking'])
print(df.head())