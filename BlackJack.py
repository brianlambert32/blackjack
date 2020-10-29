

import random




card_list = ["A_Spades", "A_Hearts", "A_Clubs", "A_Diamonds",
             "2_Spades", "2_Hearts", "2_Clubs", "2_Diamonds",
             "3_Spades", "3_Hearts", "3_Clubs", "3_Diamonds",
             "4_Spades", "4_Hearts", "4_Clubs", "4_Diamonds",
             "5_Spades", "5_Hearts", "5_Clubs", "5_Diamonds",
             "6_Spades", "6_Hearts", "6_Clubs", "6_Diamonds",
             "7_Spades", "7_Hearts", "7_Clubs", "7_Diamonds",
             "8_Spades", "8_Hearts", "8_Clubs", "8_Diamonds",
             "9_Spades", "9_Hearts", "9_Clubs", "9_Diamonds",
             "10_Spades", "10_Hearts", "10_Clubs","10_Diamonds",
             "J_Spades", "J_Hearts", "J_Clubs", "J_Diamonds",
             "Q_Spades", "Q_Hearts", "Q_Clubs", "Q_Diamonds",
             "K_Spades", "K_Hearts", "K_Clubs", "K_Diamonds"]



random.shuffle(card_list)

values = {"A_Spades":1, "A_Hearts":1, "A_Clubs":1, "A_Diamonds":1,
          "2_Spades":2, "2_Hearts":2, "2_Clubs":2, "2_Diamonds":2,
          "3_Spades":3, "3_Hearts":3, "3_Clubs":3, "3_Diamonds":3,
          "4_Spades":4, "4_Hearts":4, "4_Clubs":4, "4_Diamonds":4,
          "5_Spades":5, "5_Hearts":5, "5_Clubs":5, "5_Diamonds":5,
          "6_Spades":6, "6_Hearts":6, "6_Clubs":6, "6_Diamonds":6,
          "7_Spades":7, "7_Hearts":7, "7_Clubs":7, "7_Diamonds":7,
          "8_Spades":8, "8_Hearts":8, "8_Clubs":8, "8_Diamonds":8,
          "9_Spades":9, "9_Hearts":9, "9_Clubs":9, "9_Diamonds":9,
          "10_Spades":10, "10_Hearts":10, "10_Clubs":10,"10_Diamonds":10,
          "J_Spades":10, "J_Hearts":10, "J_Clubs":10, "J_Diamonds":10,
          "Q_Spades":10, "Q_Hearts":10, "Q_Clubs":10, "Q_Diamonds":10,
          "K_Spades":10, "K_Hearts":10, "K_Clubs":10, "K_Diamonds":10}

aces = ["A_Spades", "A_Hearts", "A_Clubs", "A_Diamonds"]

tens = ["10_Spades", "10_Hearts", "10_Clubs","10_Diamonds",
            "J_Spades", "J_Hearts", "J_Clubs", "J_Diamonds",
            "Q_Spades", "Q_Hearts", "Q_Clubs", "Q_Diamonds",
            "K_Spades", "K_Hearts", "K_Clubs", "K_Diamonds"]

playercard = []
dealercard = []

toContinue = True
playerWin = "Unknown"


#

def takecard(mycard):
    mycard.append(card_list[0])
    card_list.pop(0)

def check_aces(val):
    for i in range(len(aces)):
        if val == aces[i]:
            return True

def check_tens(val):
    for i in range(len(tens)):
        if val == tens[i]:
            return True

def is_blackjack(mycards):

    if (check_aces(mycards[0]) and check_tens(mycards[1])):
        return "Blackjack"
    elif (check_tens(mycards[0]) and check_aces(mycards[1])):
        return "Blackjack"
    else:
        return "Would you like to hit?"

def values_of_Aces(mycard, my_sum):
    for i in range(len(mycard)):
        if check_aces(mycard[i]):
            my_sum += 10
            if my_sum > 21:
                my_sum -= 10
    return my_sum

def sum_cards(mycard):
    my_sum = 0
    for i in range(len(mycard)):
        my_sum += values[mycard[i]]
    my_sum = values_of_Aces(mycard, my_sum)
    if len(mycard) == 2:
        if check_aces(mycard[0]) and check_aces(mycard[1]):
            my_sum = 21
    return my_sum



# Play
print("Welcome to Blackjack")
input("Press <enter> to proceed")
answer = input("Number of decks, 1 or 2:")
if answer == "2":
    card_list = card_list*2
else:
    card_list = card_list

print("\nOriginal shuffled cards:\n", card_list)
takecard(playercard)
takecard(dealercard)
takecard(playercard)
takecard(dealercard)


##
          
          
print("\nPlayer's Cards:", playercard)
print("Player's score is:", sum_cards(playercard))
print("\nDealer's Cards:", "[x]", dealercard[1])
print("Deal's score is: unknown \n")
              
if is_blackjack(playercard) != "Would you like to hit?" and is_blackjack(dealercard) != "Would you like to hit?":
    print("Nobody wins! Both have Blackjack")
    toContinue = False
    playerWin = "Draw"
elif is_blackjack(playercard) != "Would you like to hit?":
    print("Blackjack! Player wins!")
    toContinue = False
    playerWin = "Win"
elif is_blackjack(dealercard) != "Would you like to hit?":
    print("House wins! Blackjack!")
    toContinue = False
    playerWin = "Lose"



print("\nIt is now the player's turn.")
while toContinue:
    answer = input("Do you want to adjust bust to 25? (yes or no):")
    if answer == "yes":
        while toContinue:
            answer = input("Do you want to hit or stay?:")
            if answer == "hit":
                takecard(playercard)
                print("\nPlayer's cards:", playercard)
                print("Player card value is: ", sum_cards(playercard))
                if sum_cards(playercard) > 25:
                    print("\nPlayer bust! House wins.")
                    toContinue = False
                    playerWin = "Lose"
                elif sum_cards(playercard) == 25:
                    print("\nPlayer has 25, you win!")
                    toContinue = False
                    playerWin = "Win"
                    break
            elif answer == "stay":
                print("\nPlayer chooses to stay")
                print("\nPlayer has :", playercard)
                print("Final sum is: ", sum_cards(playercard))
                toContinue = False
                break
    elif answer == "no":

        while toContinue:
            answer = input("Do you want to hit or stay?:")
            if answer == "hit":
                takecard(playercard)
                print("\nPlayer's cards:", playercard)
                print("Player card value is: ", sum_cards(playercard))
                if sum_cards(playercard) > 21:
                    print("\nPlayer bust! House wins.")
                    toContinue = False
                    playerWin = "Lose"
                elif sum_cards(playercard) == 21:
                    print("\nPlayer has 21, you win!")
                    toContinue = False
                    playerWin = "Win"
                    break
#not a necessary add in for this ^, but could be used for a similar implementation
            elif answer == "stay":
                print("\nPlayer chooses to stay")
                print("\nPlayer has :", playercard)
                print("Final sum is: ", sum_cards(playercard))
                toContinue = False
                break

if playerWin == "Unknown":
    print("\nIt is now the dealer's turn.")
    while True:
        if sum_cards(dealercard) < sum_cards(playercard):
            takecard(dealercard)
            print("\nDealer has:", dealercard)
            print("The Dealer sum is: ", sum_cards(dealercard))
        else:
            print("\nFinal cards for dealer:", dealercard)
            print("Final sum for dealer: ", sum_cards(dealercard))
            break





    if sum_cards(dealercard) > 21:
        print("\nDealer bust! Player wins")
        playerWin = "Win"
    elif sum_cards(dealercard) > sum_cards(playercard):
        print("\nDealer wins!")
        playerWin = "Lose"
    elif sum_cards(dealercard) < sum_cards(playercard):
        print("\nPlayer wins!")
        playerWin = "Win"
    elif sum_cards(dealercard) == sum_cards(playercard):
        print("\nIt is draw, nobody wins")
        playerWin = "Draw"


#print("\nRemaining cards:\n", card_list)
print("there are", len(card_list), " left.")

#if playerWin == "Unknown":
#new_game = input("Would you like to play again? Enter yes or no")
#while False:
 
 # if new_game[0] == "yes":
 ##  takecard(playercard)
            #  takecard(dealercard)
            #         takecard(playercard)
            #takecard(dealercard)

#else:
#           print("\nHope you had fun!")
 







