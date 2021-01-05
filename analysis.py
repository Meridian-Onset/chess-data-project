import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from gambit import Gambit, GambitParse
from gambitdownloader import linestoDict



filename = "./games.csv"

####################################################################################

def winCounter(data):
    # Returns the number of white wins and black wins in a dataframe
    return

####################################################################################

def WB_ECOGroups(data):
    # Return a dataframe of ECO groups and their win proportions
    eco_groups = ["A","B","C","D","E"]
    col_names = ["ECO Code", "White", "Draw", "Black"]
    group_games = pd.DataFrame(columns = col_names)
    white_wins, draws, black_wins = [], [], []
    
    for group in eco_groups:
        games = data[data.eco_group == group]
        winning_vals = games.winner.value_counts()
        total_games = winning_vals.sum()
        white_wins.append(winning_vals['white'] / total_games * 100)
        black_wins.append(winning_vals['black'] / total_games * 100)
        draws.append(winning_vals['draw'] / total_games * 100)
        
    group_games['White'], group_games['Black'] = white_wins, black_wins
    group_games['Draw'] = draws; group_games['ECO Code'] = eco_groups
    group_games = pd.melt(group_games, id_vars="ECO Code", var_name="Outcome", 
                            value_name="Percentage of Games")
    
    return(group_games)

####################################################################################

def plotRelativeFrequencies(data):
    '''Plots a bar graph showing the percentage distribution of game conclusions 
    based on the opening gambits eco code'''
    
    sns.set_style('darkgrid')

    #Create a new column containing ECO code group 
    data[["eco_group"]] = [code[0] for code in data.opening_eco]
    group_frame = WB_ECOGroups(data)

    #Create bar plot 
    ax = sns.catplot(x = "ECO Code", y = "Percentage of Games", 
                     hue = "Outcome", data = group_frame, 
                     hue_order = ['White', 'Black', 'Draw'],
                     kind = 'bar', palette = 'muted')
    sns.despine()
    plt.title("Plot of Outcome Percentages Grouped by ECO Code")
    #Show
    plt.show()

####################################################################################
    


if __name__ =='__main__':
    with open(filename, 'r') as f:
        data = pd.read_csv(f)
    #Drop columns not needed
    dropnames = ["white_id", "black_id"]
    data = data.drop(dropnames, axis = 1)

    #Create a new column containing ECO code group 
    data[["eco_group"]] = [code[0] for code in data.opening_eco]
    group_frame = WB_ECOGroups(data)
    plotRelativeFrequencies(data)
    