import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

filename = "./games.csv"

with open(filename, 'r') as f:
    data = pd.read_csv(f)

print(data.head())