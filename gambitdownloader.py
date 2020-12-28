import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.365chess.com/eco.php'

#Define some regular expressions for use in the linegetter function
completeExp = '^[A-Z][0-9][0-9] .+ 1\.'
incompleteExp = '^[A-Z][0-9][0-9]'

def linegetter(webPath):
    connection = requests.get(webPath)
    soup = BeautifulSoup(connection.content, "html.parser")
    connection.close()
    #Parse text data
    gambits = soup.find(id = "ecotree").get_text().splitlines()

    #Clean up resulting list
    gambits = [gambit for gambit in gambits if gambit != '' and gambit != '\t\t\t\t']
    finalgambs = list()
    for i, gambit in enumerate(gambits):
        code = gambit[0:4]
        if re.search(completeExp, gambit) != None: 
            finalgambs.append(gambit.split(code)) 
        elif re.search(incompleteExp, gambit) != None: 
            finalgambs.append(gambit + gambits[i+1])
        else: pass
    #File into dictionary object
    gambitDict = dict()
    for gambit in finalgambs:
        try:
            codename, moves = gambit.split('1.')
            gambitDict[codename] = moves
        except ValueError: print(gambit)
    #print(gambitDict)

if __name__ == "__main__":
    linegetter(url)

