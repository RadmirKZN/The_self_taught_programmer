class Card:
    
    suits = ['пикей','червей','бубей','треф']

    values = [None, None, '2','3','4','5','6','7','8','9','10','валета','даму','короля','туза']


    def __init__(self, v, s):
        '''suits и value - целые числа'''
        self.value = v
        self.suit = s

    def __it__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __reper__(self):
        v = self.values[self.value] + ' of '\
        + self.suits[self.suit]
        return v 

