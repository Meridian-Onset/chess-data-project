import requests
from bs4 import BeautifulSoup
import re
import os

url = 'https://www.365chess.com/eco.php'

#Define some regular expressions for use in the linegetter function
completeExp = '^[A-Z][0-9][0-9] .+ 1.'
incompleteExp = '^[A-Z][0-9][0-9]'

def lineGetter(webPath):
    connection = requests.get(webPath)
    soup = BeautifulSoup(connection.content, "html.parser")
    connection.close()
    #Parse text data
    gambits = soup.find(id = "ecotree").get_text().splitlines()

    #Clean up resulting list
    gambits = [gambit for gambit in gambits if gambit != '' and gambit != '\t\t\t\t']
    with open('./gambitsRaw.txt', 'w') as f:
        for gambit in gambits:
            f.write(f'{gambit}\n')


def linetoFileParse(filepath):
    '''This function is designed to take the raw text file downloaded using lineGetter
    and process this into a human readable .txt file that can then be used to create a 
    dictionary using linestoDict'''
    with open(filepath, 'r') as f:
        gambits = f.read().splitlines()
    finalgambs = list()
    for i, gambit in enumerate(gambits):
        try: 
            if gambits[i+1].startswith('1.'):
                finalgambs.append(gambit + ' ' + gambits[i+1])
            elif re.search(incompleteExp, gambit) != None: 
                finalgambs.append(gambit)
        except IndexError: pass
    # Write the processed gambit text to a file
    with open('./processedGambits.txt', 'w') as f:
        for gambit in finalgambs:
            f.write(f'{gambit}\n')

def linestoDict(gambitPath):
    '''Function designed to return a dictionary containing the ECO codes as keys with
    gambit names and move sequences as values'''

    
    

if __name__ == "__main__":
    linetoFileParse('./gambitsRaw.txt')

