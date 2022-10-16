"""Card and Deck Classes & Standard Deck of Cards Function"""

import random

'''Card Class'''

class card:
    """Creating a Card object"""

    def __init__(self):
        self.number_value = None
        self.suit = None
        self.faceCard = False
        self.ace = False

    def createCard(self, number_value, suit, faceCard, ace):
        self.number_value = number_value
        self.suit = suit
        self.faceCard = faceCard
        self.ace = ace

    def getSuit(self):
        return self.suit

    def getNumberValue(self):
        if self.faceCard:
            return 10
        else:
            return self.number_value

    def ifSuit(self):
        return self.suit

    def ifFaceCard(self):
        return self.faceCard

    def __str__(self):
        """Returns a string representation of the card"""
        return f'{self.number_value} of {self.suit}'


'''Deck of Cards Class'''

class deck:

    def __init__(self):
        self.currentCards = []

    def insert(self, c):
        if c not in self.currentCards:
            self.currentCards.append(c)

    def remove(self, c):
        try:
            self.currentCards.remove(c)
        except:
            raise ValueError(str(c), 'Not found')

    def member(self, c):
        return c in self.currentCards

    def current_deck(self):
        return self.currentCards[:]

    def numberOfCardsInDeck(self):
        return len(self.currentCards)

    def len(self):
        return len(self.currentCards)
    
    def shuffleDeck(self):
        return random.shuffle(self.currentCards)

    def __str__(self):
        result = ''
        for c in self.currentCards:
            result += str(c) + ', '
        return result[:-2]


'''Standard Deck of Cards Function'''

def create_Standard_Deck():
    deckOfCards = deck()

    four_suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

    '''Lets create the numbered cards'''
    for c in range(2, 11):
        for s in four_suits:
            y = card()
            y.createCard(c, s, False, False)
            deckOfCards.insert(y)

    '''Creating the Face Cards'''
    faceCards = ['Jack', 'Queen', 'King', 'Ace']

    for s in four_suits:
        for f in faceCards:
            y = card()
            if f == 'Ace':
                y.createCard(f, s, True, True)
                deckOfCards.insert(y)
            else:
                y.createCard(f, s, True, False)
                deckOfCards.insert(y)

    return deckOfCards


'''Checks for the Standard Deck Function'''

# d = create_Standard_Deck()
# d.shuffleDeck()
# print(len(d.current_deck()))
# print(d)


# created by Austen J. Querino for Nucamp Python Fundamentals Portfolio Project