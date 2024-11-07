import random
import time

cards = [11,1,2,3,4,5,6,7,8,9,10,10,10]

user_hand_amount = 0
user_hand_status = ''
dealer_hand_amount = 0
dealer_hand_status = ''

def deal(player_hand):

    for i in range(0,2): player_hand.append(random.choice(cards))
    return player_hand

def hit(player_hand): 
    
    player_hand.append(random.choice(cards))
    return player_hand

def calculate(player_hand):

    player_hand_amount = 0  

    for i in range(0, len(player_hand)): player_hand_amount = player_hand_amount + player_hand[i]
    return player_hand_amount

def determine_winner(user_amount, dealer_amount, user_status):

    if user_status == 'jackpot':

        print('You won!')

    elif user_amount > dealer_amount:

        print('You won!')

    elif user_amount == dealer_amount:

        print('You pushed!')

    else: print('You lost!')


game_is_not_over = True

while game_is_not_over:

    user_hand = []
    dealer_hand = []

    user_hand = deal(user_hand)
    dealer_hand = deal(dealer_hand)

    print(f'Player hand: {user_hand}')
    print(f'Dealer hand: [{dealer_hand[1]}]\n')

    if user_hand == 21: user_hand_is_not_over = False
    else: user_hand_is_not_over = True

    while user_hand_is_not_over:

        choice = input(f'Your hand is {user_hand}, do you want to hit or stand: ')

        if choice == 'hit':

            user_hand = hit(user_hand)
            user_hand_amount = calculate(user_hand)

            if user_hand_amount > 21:

                user_hand_status = 'bust'
                user_hand_is_not_over = False

                print('You busted! (pause lmao)')

            elif user_hand_amount == 21:

                user_hand_status = 'jackpot'
                user_hand_is_not_over = False

                print('You hit Jackpot! lets see what the dealer gets..')

        else: 
            user_hand_is_not_over = False

            print('Lets see what the dealer gets..')

        
    print(f'Dealer reveals: {dealer_hand}')


    dealer_hand_is_not_over = True

    while dealer_hand_is_not_over:

        dealer_hand_amount = calculate(dealer_hand)

        if dealer_hand_amount >= 17 and dealer_hand_amount < 21: dealer_hand_is_not_over = False

        elif dealer_hand_amount < 17:

            dealer_hand = hit(dealer_hand)
            time.sleep(2)

            print(f'Dealer hits: {dealer_hand}')

        elif dealer_hand_amount == 21: 
            
            dealer_hand_status = 'jackpot'
            dealer_hand_is_not_over = False

            print(f'Dealer hit Jackpot!')

        else: 
            dealer_hand_is_not_over = False

            print('Dealer busted! (pause wtf)')

    determine_winner(user_amount=user_hand_amount, dealer_amount=dealer_hand_amount, user_status=user_hand_status)

    direction = input('Do you want to play another hand? Type either yes or no: ')

    if direction == 'No' or direction == 'no': game_is_not_over = False






