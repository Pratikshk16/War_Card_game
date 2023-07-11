import random
#Creating the Tuples and Dictionary for Card Deck
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#Creating a card class to further compare the values of different cards
class card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit

#Creating a deck class that holds the deck of cards, shuffles and deals the card to player
class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card = card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()


#Player class that removes a card during each round and takes back cards won
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self, new_cards):
        if type(new_cards)==type([]):
            self.add_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self) :
        return (f"Player {self.name} has {len(self.all_cards)} Cards")

#Getting game started
Player1 = Player("Pratik")
Player2 = Player("Yash")
Our_Deck = Deck()
Our_Deck.shuffle()

#Dealing the cards
count = 0
for i in Our_Deck.all_cards:
    if(count<26):
        Player1.add_cards(i)
        count+=1
    else:
        Player2.add_cards(i)

game_on = True
round_num=0
while game_on:
    round_num+=1
    print("Round",round_num)
    if (len(Player1.all_cards)==0):
        print(Player1.name, " Out of Cards ", Player2.name, " Wins!!")
        game_on=False
        break
    if (len(Player2.all_cards)==0):
        print(Player2.name, " Out of Cards ", Player1.name, " Wins!!")
        game_on=False
        break
    c1=Player1.remove_one()
    c2=Player2.remove_one()
    Player1_cards = []
    Player1_cards.append(c1) #Appending the cards removed in a list so that its value can be compared
    Player2_cards = []
    Player2_cards.append(c2)

    at_war = True
    while at_war:
        if Player1_cards[-1].values > Player2_cards[-1].values: #calling the card class method for comparision
            Player1.add_cards(c1)
            Player1.add_cards(c2)
            at_war=False
        elif Player2_cards[-1].values > Player1_cards[-1].values:
            Player2.add_cards(c1)
            Player2.add_cards(c2)
            at_war=False
        else:
            print("War")
            #War conditions
            if len(Player1.all_cards)<5:
                print(Player1.name, " unable to play war! Game Over at War")
                print(Player2.name, " Wins! ",Player1.name , " Loses!")
                game_on = False
                break
            elif len(Player2.all_cards)<5:
                print(Player2.name, " unable to play war! Game Over at War")
                print(Player1.name, " Wins! ",Player2.name , " Loses!")
                game_on = False
                break
            else:
                for i in range(5):
                    Player1_cards.append(Player1.remove_one())
                    Player2_cards.append(Player2.remove_one())


    

