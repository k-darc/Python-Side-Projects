import random
cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["Ace": 11, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
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
card = deal(1)[0]