import random
class Player:
    def __init__(self, initial_money=1000):
        self.money = initial_money

    def place_bet(self):
        while True:
            try:
                bet = int(input(f"You have ${self.money}. How much would you like to bet? "))
                if 0 < bet <= self.money:
                    self.money -= bet
                    return bet
                else:
                    print(f"Please enter a valid amount between 1 and ${self.money}.")
            except ValueError:
                print("Please enter a valid number.")

    def win(self, bet):
        print(f"You won ${bet * 2}!")
        self.money += bet * 2
        print(f"Your money now is ${self.money}")

    def lose(self, bet):
        print(f"You lost your bet of ${bet}.")
        print(f"Your money now is ${self.money}")

    def tie(self, bet):
        print("It's a tie. You get your bet back.")
        self.money += bet
        print(f"Your money now is ${self.money}")
player = Player() 
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

def create_deck():
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
    return deck


def start_game():
  while True:  
    deck = create_deck()  # Create a new deck for every game
    bet = player.place_bet()
    turn = 1
    players_count = 0
    dealers_count = 0
    
    players_count = deck[0].count_card(players_count)
    players_count = deck[2].count_card(players_count)
    dealers_count = deck[1].count_card(dealers_count)

    print("Dealer's cards are: " + deck[1].print_card() + ", hidden")
    print("Your cards are: " + deck[0].print_card() + ", " + deck[2].print_card() + "\n" + "Your total is: " + str(players_count))
    if players_count == 21:
        print("\nYou have a BlackJack!\nCongratulations! You won!")
        play_again()
    elif dealers_count == 21:
        print("\nDealer has a BlackJack!\nDealer won")
    else:
      play(deck, players_count, turn, dealers_count, bet)
    play_again()
def play(deck, players_count, turn, dealers_count, bet):
    choice = input("\nDo you want to hit or stay?\n(Type 'h' to hit and 's' to stay)\n").lower()
    if choice == "h":
        players_count = deck[turn + 2].count_card(players_count)
        print("Dealer's cards are: " + deck[1].print_card() + ", hidden")
        print("Your cards are: " + deck[0].print_card() + ", " + deck[2].print_card(), end="")
        for i in range(turn):
            print(", " + deck[i+4].print_card(), end="")
        print("\nYour total is: " + str(players_count))
        turn+=1
        if players_count == 21:
            print("\nCongratulations! You won!")
        elif players_count>21:
            print("\nYou are busted!\nYou lost!")
        else:
            play(deck, players_count, turn, dealers_count, bet)
    elif choice == "s":
     card_index = 4  # After dealing, the 5th card (index 4) in the deck is the next to be drawn
     dealers_turn(deck, dealers_count, players_count, card_index, bet)
    else:
     print("You entered the wrong letter!")
     play(deck, players_count, turn, dealers_count)
  

def dealers_turn(deck, dealers_count, players_count, card_index, bet):
    print("\nDealer's turn:")
    print("Dealer's cards are: " + deck[1].print_card() + ", " + deck[3].print_card())

    while dealers_count < 17 and card_index < len(deck):  # Ensure we don't run out of cards in the deck
        new_card = deck[card_index]
        dealers_count = new_card.count_card(dealers_count)
        card_index += 1  # Increment the card_index to point to the next card

        print("Dealer draws: " + new_card.print_card())
        print("Dealer's new total: " + str(dealers_count))
        
        # Account for a scenario where Ace should be counted as 1 to avoid bust
        if dealers_count > 21 and "Ace" in [card.number for card in deck[:card_index]]:
            dealers_count -= 10  # Substituting Ace value: 11 -> 1
    
    if dealers_count > 21:
        print("\nDealer is busted! You win!")
        player.win(bet)
    elif dealers_count >= 17 and dealers_count <= 21:
        print("\nDealer stands with a total of " + str(dealers_count))
        
        if players_count > dealers_count:
            print("Congratulations! You win!")
            player.win(bet)
        elif players_count < dealers_count:
            print("Dealer wins.")
            player.lose(bet)
        else:
            print("It's a tie.")
            player.tie(bet)
    else:
        print("\nUnexpected scenario in dealer's turn logic.")
    return card_index  # Return the updated card_index for future reference if needed

def play_again():
    while True:  # Keep asking until valid input is given
        user_input = input("Do you want to play again? (yes/no): ").strip().lower()
        
        if user_input in ["yes", "no"]: 
            break  # Exit the loop if input is valid
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    

    if user_input == "yes":
        print("Starting a new game...\n")
        start_game()  # Restart the game
    else:
        print("Thank you for playing! See you next time.")




player = Player()
print("Welcome to BlackJack!\nHere is a quick manual for playing blackjack: https://shorturl.at/hyDUZ")
start_game()

