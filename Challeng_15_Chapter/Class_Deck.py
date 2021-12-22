from random import shuffle
class Deck:
    def __init__(self):
        self.cards = []
        for i in range (2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len (self.card) == 0:
            return
        return self.card.pop()

     
deck = Deck()
for card in deck.cards:
    print (card)
