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
            else: moves.append(move)
        return(moves)
    
    def to_dict(self):
        #Returns a dictionary object that can be used to update an existing dictionary
        return({self.code : (self.name, self.sequence)})

