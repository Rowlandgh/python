import collections

card = collections.namedtuple('card',['rank','suit'])
""" card1 = card('7','方片')
print(card1) """

class Pokerdeck:
    ranks = [str(n) for n in range(2,11)] + ['j','d','q','k','a']
    suits = '红心,黑桃,方片,梅花'.split(',')

    def __init__(self):
        self.cards = [card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self,position):
        return self.cards[position]

deck = Pokerdeck()
#print(len(deck))

#print(deck[0],deck[-1])

from random import choice
#print(choice(deck),choice(deck),choice(deck))

#print(deck[:3])             #拿前3张牌

#print(deck[3::2])           #从第4张牌开始，每隔2张拿一次

#for singlecard in deck:
    #print(singlecard)

suit_values = dict(黑桃=3,红桃=2,方片=1,梅花=0)

print(suit_values)

def whos_high(card):
    rank_value = Pokerdeck.ranks.index(card.rank)
    return rank_value*len(suit_values) + suit_values[card.suit]

for card in sorted(deck,key=whos_high):
    print(card)