"""Portfolio Project - Blackjack Card Game"""

'''Lets make a Blackjack Card Game'''

'''Tasks'''
# 1) Need to fix the extra comma at the end of the list of cards in a deck -DONE
# 2) Need to solve for the Ace as it can equal 1 or 10
# 3) Need to solve the shuffle deck function -DONE
# 4) Add high score counter -DONE
# 5) Ensure the bet amount is fixed at two decimal places -DONE
# 6) What happens if the player and dealer tie? -DONE
# 7) If player recieves a blackjack hand - Jack and an Ace, they should recieve a message indicating so -DONE

'''Imports'''

import random
from cards import card, deck, create_Standard_Deck
# import json 


'''Blackjack Game'''
highscores = {}
continue_to_play = True

while continue_to_play:
    s_amount = 50.00
    starting_amount = round(s_amount, 2)
    name_for_highscore = input('Type your name in for the Highscore Board. \n')

    while starting_amount > 0:
        play = input(f'Would you like to play Blackjack? You have ${round(starting_amount, 2)}\n'
                    '1) Yes \n'
                    '2) No \n'
                    'Shall we play? \n').lower()
        play = play.capitalize()
        if play == '1' or play == 'Yes' or play == 'Y':
            d = create_Standard_Deck()
            d.shuffleDeck()
            print(f'You start out with ${round(starting_amount, 2)}, would you like to place a bet?')
            '''The Bet Loop'''
            while True:
                bet = input('Select the amount you would like to bet, \n'
                            f' You have ${round(starting_amount, 2)} left \n'
                            ' If you would like to pass enter p \n')
                if bet == 'p' or bet == '0':
                    bet = 0.00
                    break
                elif float(bet) > starting_amount:
                    print('You cannot bet more than you have, try again')
                elif float(bet) < 0:
                    print('You cannot bet negative amounts, try again')
                else:
                    starting_amount -= float(bet)
                    break
            player1c = random.choice(d.current_deck())
            d.remove(player1c)
            dealer1c = random.choice(d.current_deck())
            d.remove(dealer1c)
            print(f'Your first card is {player1c} and the Dealers first card is {dealer1c}')
            player2c = random.choice(d.current_deck())
            d.remove(player2c)
            print(f'Your second card is {player2c}')
            hand = player1c.getNumberValue() + player2c.getNumberValue()
            '''The Player Card Loop'''
            while True:
                if hand > 21:
                    print(f'You Bust, your card values are {hand}')
                    break
                elif hand == 21:
                    starting_amount += (float(bet) + float(bet) * 1.5)
                    print('You got Blackjack, congratulations! You win this hand!')
                    break
                else:
                    additional_card = input(f' Your hand is {hand}, would you like another card? \n'
                                            f'Yes (y) or No (n) \n').lower()
                    additional_card = additional_card.capitalize()
                    if additional_card == 'Y' or additional_card == 'Yes':
                        player_extra_card = random.choice(d.current_deck())
                        hand += player_extra_card.getNumberValue()
                        d.remove(player_extra_card)
                        print(f'You received a {player_extra_card} and your hand is now {hand}')
                    elif additional_card == 'N' or additional_card == 'No':
                        print(f' You have decided to hold with a hand value of {hand}.')
                        break
                    else:
                        continue

            '''The Dealer's Cards'''
            dealer2c = random.choice(d.current_deck())
            d.remove(dealer2c)
            dealer_hand = dealer1c.getNumberValue() + dealer2c.getNumberValue()
            
            if hand < 21 and dealer_hand < 21:
                print(f'The dealer recieved a {dealer2c}, the dealer\'s hand is now {dealer_hand}')
            else:
                pass

            while hand < 21: 
                if dealer_hand == 21:
                    print('The Dealer gets Blackjack. Dealer wins.')
                    break
                elif dealer_hand > 21:
                    starting_amount += (float(bet) + float(bet) * 1.5)
                    print('The Dealer Busts. You won, Congratulations!')
                    break
                elif dealer_hand < 17:
                    dealer_extra_card = random.choice(d.current_deck())
                    dealer_hand += dealer_extra_card.getNumberValue()
                    d.remove(dealer_extra_card)
                    print(f'The dealer recieved a {dealer_extra_card}, the dealer\'s hand is now {dealer_hand}')
                else:
                    if hand == dealer_hand:
                        print(f'Blackjack push! You and the Dealer have a hand of {hand} \n'
                                'You receive your bet back')
                        starting_amount += float(bet)
                        break
                    elif hand > dealer_hand:
                        starting_amount += (float(bet) + float(bet) * 1.5)
                        print(f'Your hand of {hand} beats the Dealers hand of {dealer_hand} \n'
                            'You won, Congratulations!')
                        break
                    else:
                        print(f'The Dealers hand of {dealer_hand} beats your hand of {hand} \n'
                            'You lose, try again')
                        break
        elif play == '2' or play == 'No' or play == 'N':
            print('Thank you for playing, come again soon.')
            highscores[name_for_highscore] = starting_amount
            continue_to_play = False
            break
        elif starting_amount > 0:
            continue
        else:
            print('Invalid input, please try again.')
            continue

    if starting_amount <= 0:
        print('You lost all your money. The game is over...')
        
        continue_play = input('Would you like to play again?\n'
                    '1) Yes \n'
                    '2) No \n'
                    'Shall we play? \n').lower()
        continue_play = continue_play.capitalize()
        if continue_play == '1' or continue_play == 'Yes' or continue_play == 'Y':
            highscores[name_for_highscore] = starting_amount
            pass
        elif continue_play == '2' or continue_play == 'No' or continue_play == 'N':
            print('Thank you for playing, come again soon.')
            highscores[name_for_highscore] = starting_amount
            continue_to_play = False
            break
        else:
            print('Invalid input, please try again.')
            continue
        pass

    


'''Highscore Board'''

# If you would like to save high scores from multiple games

# hs = json.dumps(highscores)
# with open('Highscores.json', 'w') as f:
#     f.write(hs)
#     f.close()

# hs_record = json.load(open('highscore.json'))


sortedByHighScore = {key: value for key, value in sorted(highscores.items(), key= lambda value: value[1], reverse=True)}

for name, highscores in sortedByHighScore.items():
    format = (f'Player: {name.ljust(len(name) + 2)}  \t Score: {highscores}')
    print(format)




# created by Austen J. Querino for Nucamp Python Fundamentals Portfolio Project