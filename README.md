# blackjackgame
A Simple Command Line Blackjack Game in Python

Nucamp Python Fundamentals Portfolio Project
Austen J. Querino
blackjack_game.py
cards.py

1. Introduction

It is a simple CLI blackjack game displayed in the terminal, where a user can enter their name and play as many 
hands of blackjack as they would like. The player starts out with an initial $50.00 and tries and make as much 
money as they can by betting on their blackjack hands. The dealer is also receiving cards and can win and take 
all your money. The rules are exactly like real blackjack. 

2. Design and Implementation 

I created a card class and a deck class to represent a standard playing card and deck of cards used in blackjack. 
With attributes that allow us to value the card in the game of blackjack. Then I wrote a simple function called 
create_Standard_Deck() which built a representation of a standard deck of cards using the card and deck class. I 
then create the actual blackjack game with loops to allow the player to continuously play for as long as they l
ike even if they lose all their play money. They can re-enter their names and try again starting with $50.00. I 
stored their names in a dictionary to later display any high scores they may have. 

3. Conclusions

I learned a lot from this project, simply by utilizing a lot of the tools I learned in this bootcamp and doing 
my own research on a few other topics. Creating control flow to see how a blackjack player might interact with 
a dealer was very interesting and creating simple classes to represent cards and decks of cards also helped 
solidify the skills we learned in this bootcamp. One thing I learned that was beyond the scope of this course 
was to sort a dictionary for displaying the high scores at the end of the game. With the background of sorting a
lgorithms that I learned from this course, I was able to build on that knowledge and find useful information from 
resources like stack overflow and github. The biggest shortcoming in the blackjack game that I was unable to 
solve was the fact that an ace can be valued at either 1 or 10 depending on what the player wants. I do not know 
the more intricate rules of blackjack, so I didn’t know how to code this in. I do have an attribute in my card 
class that details if the card is in fact an ace so I can add it later. 
