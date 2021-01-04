import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from gambit import Gambit
from gambitdownloader import linestoDict

filename = "./games.csv"



if __name__ =='__main__':
    with open(filename, 'r') as f:
        data = pd.read_csv(f)
    
    print(data.white_rating.mean())