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
    
    return(group_games)

####################################################################################

def plotRelativeFrequencies(group_games):
    '''Plots a bar graph showing the percentage distribution of game conclusions 
    based on the opening gambits eco code'''
    
    data = pd.melt(group_games, id_vars="ECO Code", var_name="Outcome", 
                            value_name="Percentage of Games")
    
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
    
    
def plotStackedFrequencies(group_games):
    '''Create a stacked bar chart showing the percentage of each outcome based 
    on the ECO Grouping'''
    
    white_win = group_games['White']
    draw, black_win = group_games['Draw'], group_games['Black']
    width = 0.4
    
    groups = dict()
    for i, group in enumerate(group_games['ECO Code']):
        groups[group] = round(2*width * (i+1),1)
    print(groups)
    fig, ax = plt.subplots()
    ax.grid(which = 'both', axis = 'y', alpha = 0.25,
            color = 'black')
    ax.set_axisbelow(True)
    ax.set_xticks(list(groups.values()))
    ax.set_xticklabels(list(groups.keys()))
    
    ax.bar(groups.values(), white_win, width, label = 'White',
           edgecolor = 'black')
    ax.bar(groups.values(), draw, width, bottom = white_win,
           label = 'Draw', 
           edgecolor = 'black')
    ax.bar(groups.values(), black_win, width, 
           bottom = white_win + draw,
           label = 'Black',
           edgecolor = 'black')
    
    for group, white_per, black_per in zip(groups.values(), white_win, black_win):
        white = str(round(white_per)) + '%'
        black = str(round(black_per)) + '%'
        #Write white percentage
        ax.text(group-(0.3*width), 0.5 * white_per, s = white,
                color = 'black', fontweight = 'bold')
        ax.text(group-(0.3*width), 100-(0.5*black_per), s = black,
                color = 'black', fontweight = 'bold')
    
    ax.set_ylabel('Percentage of All Outcomes')
    ax.set_xlabel('ECO Code Group')
    ax.set_title('Percentage of Different Outcomes by Opening Gambit Code')
    ax.legend()
    
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
    plotStackedFrequencies(group_frame)
    