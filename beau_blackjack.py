import random

cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

shuffle()
cards_dealt = deal(2)
card = cards_dealt[0]
rank = card[1]

if rank == "Ace":
    value = 11
elif rank == "J"or rank == "Queen" or rank == "King":
    value = 10
else:
    value = rank

rank_dict = {"rank": rank, "value": value}


print(rank_dict["rank"], rank_dict["value"])