import random
class Cards:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    def print_card(self):
        return(self.suit + " " + str(self.number))
    def count_card(self, counter):
        if self.number == "Jack":
            counter+=10
        elif self.number == "Queen":
            counter+=10
        elif self.number == "King":
            counter+=10
        elif self.number == "Ace" and counter<=10:
            counter+=11
        elif self.number =="Ace" and counter>10:
            counter+=1
        else:
            counter+=self.number
        return(counter)
def start_game():
    turn = 1
    players_count = 0
    dealers_count = 0
    card1 = Cards("Hearts", 2)
    card2 = Cards("Hearts", 3);
    card3 = Cards("Hearts", 4);
    card4 = Cards("Hearts", 5);
    card5 = Cards("Hearts", 6);
    card6 = Cards("Hearts", 7);
    card7 = Cards("Hearts", 8);
    card8 = Cards("Hearts", 9);
    card9 = Cards("Hearts", 10);
    card10 = Cards("Hearts", "Ace");
    card11 = Cards("Hearts","Jack");
    card12 = Cards("Hearts","Queen");
    card13 = Cards("Hearts", "King");
    card14 = Cards("Diamonds", 2);
    card15 = Cards("Diamonds", 3);
    card16 = Cards("Diamonds", 4);
    card17 = Cards("Diamonds", 5);
    card18 = Cards("Diamonds", 6);
    card19 = Cards("Diamonds", 7);
    card20 = Cards("Diamonds", 8);
    card21 = Cards("Diamonds", 9);
    card22 = Cards("Diamonds", 10);
    card23 = Cards("Diamonds", "Ace");
    card24 = Cards("Diamonds","Jack");
    card25 = Cards("Diamonds","Queen");
    card26 = Cards("Diamonds", "King");
    card27 = Cards("Clubs", 2);
    card28 = Cards("Clubs", 3);
    card29 = Cards("Clubs", 4);
    card30 = Cards("Clubs", 5);
    card31 = Cards("Clubs", 6);
    card32 = Cards("Clubs", 7);
    card33 = Cards("Clubs", 8);
    card34 = Cards("Clubs", 9);
    card35 = Cards("Clubs", 10);
    card36 = Cards("Clubs", "Ace");
    card37 = Cards("Clubs","Jack");
    card38 = Cards("Clubs","Queen");
    card39 = Cards("Clubs", "King");
    card40 = Cards("Spades", 2);
    card41 = Cards("Spades", 3);
    card42 = Cards("Spades", 4);
    card43 = Cards("Spades", 5);
    card44 = Cards("Spades", 6);
    card45 = Cards("Spades", 7);
    card46 = Cards("Spades", 8);
    card47 = Cards("Spades", 9);
    card48 = Cards("Spades", 10);
    card49 = Cards("Spades", "Ace");
    card50 = Cards("Spades","Jack");
    card51 = Cards("Spades","Queen");
    card52 = Cards("Spades", "King");
    deck=[card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, card26, card27, card28, card29, card30, card31, card32, card33, card34, card35, card36, card37, card38, card39, card40, card41, card42, card43, card44, card45, card46, card47, card48, card49, card50, card51, card52]
    random.shuffle(deck)
    players_count = Cards.count_card(deck[0], players_count)
    players_count = Cards.count_card(deck[2], players_count)
    dealers_count = Cards.count_card(deck[1], dealers_count)
    print("Dealer's cards are: " + Cards.print_card(deck[1]) + ", hidden")
    print("Your cards are: " + Cards.print_card(deck[0]) + ", " + Cards.print_card(deck[2]) + "\n" + "Your total is: " + str(players_count))
    if players_count == 21:
        print("\nYou have a BlackJack!\nCongratulations! You won!")
        play_again()
    elif dealers_count == 21:
        print("\nDealer has a BlackJack!\nDealer won")
    else:
        play(deck, players_count, turn)
def play(deck, players_count, turn):
    choice = input("\nDo you want to hit or stay?\n(Type 'h' to hit and 's' to stay)\n").lower()
    if choice == "h":
        players_count = Cards.count_card(deck[turn+2], players_count)
        print("Dealer's cards are: " + Cards.print_card(deck[1]) + ", hidden")
        print("Your cards are: " + Cards.print_card(deck[0]) + ", " + Cards.print_card(deck[2]), end="")
        for i in range(turn):
            print(", " + Cards.print_card(deck[i+3]), end="")
        print("\nYour total is: " + str(players_count))
        turn+=1
        if players_count == 21:
            print("\nCongratulations! You won!")
            play_again()
        elif players_count>21:
            print("\nYou are busted!\nYou lost!")
            play_again()
        else:
            play(deck, players_count, turn)
    elif choice == "s":
        dealers_turn()
    else:
        print("You entered wrong letter!")
        play(deck, players_count, turn)
def dealers_turn():
    print()
def play_again():
    print()

print("Welcome to BlackJack!\nHere is a quick manual for playing blackjack: https://shorturl.at/hyDUZ")
start_game()