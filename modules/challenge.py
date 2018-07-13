from random import choice


class Deck:
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'ace']


class Hands:
    dealer_hand = 0
    players_hand = 0


def add_money(balance, amount):
    balance += amount
    return float(balance)


def dealerplay():
    while Hands.dealer_hand <= 21:
        card = choice(Deck.cards)
        if Hands.dealer_hand > 10 and card == 'ace':
            Hands.dealer_hand += 1
        elif Hands.dealer_hand < 10 and card == 'ace':
            Hands.dealer_hand += 11
        else:
            Hands.dealer_hand += int(card)
        continue
    return Hands.dealer_hand


def play():

    balance = 100
    buy_in = float(input("Please choose the amount you want to buy in with: "))
    if float(buy_in) <= balance:
        print("Proceed to enjoy the game")
        balance -= float(buy_in)

    elif buy_in > balance:
        print("You don't have enough gold, your balance is: " + str(balance))
        answer = input("Do you want to add money to wallet? ")

        while buy_in > balance:
            if answer == 'yes':
                money = float(input("How much do you want to add? "))
                print(money)
                print(float(balance))
                balance = add_money(balance, money)
                print(balance)
            if buy_in <= balance:
                print("Now you have enough. Proceed, the money has been deducted from your account.")
                balance -= buy_in
                break
        else:
            print("This is the end of game for you.")

    while True:
        decision = input('Please choose between hitting or standing or checking balance: ')
        if decision == 'hit':
            card = choice(Deck.cards)
            if Hands.players_hand >= 10 and card == 'ace':
                Hands.players_hand += 1
            elif Hands.players_hand <= 10 and card == 'ace':
                Hands.players_hand += 11
            else:
                Hands.players_hand += int(card)
            print("Your hand is: " + str(Hands.players_hand))
            continue
        elif decision == 'stand':
            print("Your hand is: " + str(Hands.players_hand))
            return Hands.players_hand, buy_in, balance
        elif decision == 'balance':
            print("Your balance is:  " + str(balance))


class BlackJack:
    dealer = dealerplay()
    player_hand, buy_in, balance = play()
    if player_hand == 21:
        print("You won motherfucker!")
        balance += float(buy_in) + (float(buy_in) * 1.5)
        print("Your balance is: " + str(balance))
    elif player_hand == 0:
        print("You lost before even playing")
    elif player_hand < 21:
        if dealer < 21:
            if dealer > player_hand:
                print("House won with: " + str(dealer))
                print("Your balance is: " + str(balance))
        else:
            balance += float(buy_in) * 2
            print("You won, now your balance is: " + str(balance))
    else:
        print("You lost")
        print("House had: " + str(dealer))


BlackJack()

