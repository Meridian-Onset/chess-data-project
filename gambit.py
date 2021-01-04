def GambitParse(gambitStr):
    '''Function to be used in conjunction with the preprocessed gambit text data
    and the below Gambit class'''
    nonMoveLen = int(len(gambitStr.split('1.')[0]))
    try:
        if gambitStr[3] == '-':
            code = gambitStr[0:7]
        else: code = gambitStr[0:3]

    except: pass
    name = gambitStr[len(code) + 1 : nonMoveLen]
    moves = gambitStr[nonMoveLen : len(gambitStr)] 

    return((code, name, moves))


class Gambit:
    def __init__(self, ECOcode, Name, MoveSequence):
        self.name = Name
        self.code = ECOcode
        self.sequence = MoveSequence

    def __str__(self):
        return(f'{self.code}, {self.name}: {self.sequence}')

    def move_sequence(self):
        moves = list()
        for i, move in enumerate(self.sequence.split('.')):
            if i == 0: pass
            else: moves.append(move[0:len(move)-1])
        return(moves)

    def to_dict(self):
        #Returns a dictionary object that can be used to update an existing dictionary
        return({self.code : (self.name, self.sequence)})

if __name__=="__main__":
    gambitparams = GambitParse('A42  Modern defence, Averbakh system, Randspringer variation1. d4 d6 2. c4 g6 3. Nc3 Bg7 4. e4 f5 ')
    one = Gambit(*gambitparams)
    
