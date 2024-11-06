import random

cards = [11,1,2,3,4,5,6,7,8,9,10,10,10]

user_hand = []
dealer_hand = []

def deal(player):
    for i in range(0,2): player.append(random.choice(cards))
    return player

def hit(player):
    player.append(random.choice(cards))
    return player

user_hand = deal(user_hand)
dealer_hand = deal(dealer_hand)

game_is_not_over = True

while game_is_not_over:

    choice = input(f'Your hand is {user_hand}, do you want to hit or stand: ')

    user_hand = hit(user_hand)

    hand_amount = 0

    for i in range(0, len(user_hand)):
        hand_amount = hand_amount + user_hand[i]

    print(user_hand)
    print(hand_amount)

    game_is_not_over = False
    


