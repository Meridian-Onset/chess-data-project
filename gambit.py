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

    def __len__(self):
        #Returns the number of exchanged (WB pairs) moves
        movelist = [move.strip() for move in self.sequence.split('.')]
        finalmove = movelist[-1]
        try:
            finalmove.split(' ')
            return(2 * len(self.sequence.split('.')) - 3)
        except: 
            return(2 * len(self.sequence.split('.')) - 2)

    def move_sequence(self):
        #Return a dictionary of moves
        moves = dict()
        for i, move in enumerate(self.sequence.split('.')):
            if i == 0: pass
            elif (len(move)-1) > 4 : moves[i] = move[0:len(move)-1].strip()
            else: moves[i] = move[0:len(move)].strip()
        return(moves)

    def wb_split(self):
        moves = self.move_sequence()
        white = len(moves)
        if len(moves[list(moves.keys())[-1]]) > 4: black = white
        else: black = white - 1

        return(f"W:{white} \nB:{black}\nTotal:{black+white}")

    def to_dict(self):
        #Returns a dictionary object that can be used to update an existing dictionary
        return({self.code : (self.name, self.move_sequence())})

