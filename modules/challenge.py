from random import choice


class Deck:
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'ace']


class Hands:
    dealer_hand = 0
    players_hand = 0


class playerMoney:
    balance = 100.00


def dealerplay():
    while Hands.dealer_hand <= 21:
        card = choice(Deck.cards)
        if Hands.dealer_hand > 10 and card == 'ace':
            Hands.dealer_hand += 1
        elif Hands.dealer_hand < 10 and card == 'ace':
            Hands.dealer_hand += 11
        else:
            Hands.dealer_hand += int(card)
        # print("Your hand is: " + str(Hands.dealer_hand))
        continue
    return Hands.dealer_hand
    # if Hands.dealer_hand > 21:
        # print("Your hand is: " + str(Hands.dealer_hand))


def play():

    while True:
        decision = input('Please choose between hitting or standing: ')
        if decision == 'hit':
            card = choice(Deck.cards)
            if Hands.players_hand > 10 and card == 'ace':
                Hands.players_hand += 1
            elif Hands.players_hand < 10 and card == 'ace':
                Hands.players_hand += 11
            else:
                Hands.players_hand += int(card)
            print("Your hand is: " + str(Hands.players_hand))
            continue
        elif decision == 'stand':
            print("Your hand is: " + str(Hands.players_hand))
            return Hands.players_hand


class BlackJack:
    player = 0
    buy_in = input("Please declare sum you want to buy in: ")
    if float(buy_in) <= playerMoney.balance:
        print("Proceed to enjoy the game")
        playerMoney.balance -= float(buy_in)
        player = play()
    else:
        print("You ain't made of money")

    dealer = dealerplay()

    if player == 21:
        print("You won motherfucker!")
        playerMoney.balance += float(buy_in) + (float(buy_in) * 1.5)
    elif player == 0:
        print("You lost before even playing")
    elif player < 21:
        if dealer < 21:
            if dealer > player:
                print("House won with: " + str(dealer))
        else:
            print("You won")
            playerMoney.balance += float(buy_in) * 2

    else:
        print("You lost")
        print("House had: " + str(dealer))


BlackJack()

