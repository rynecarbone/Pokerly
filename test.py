import Deck
from Deck import Card as Card
import Player

d = Deck.Deck()
a = Player.Player('a')
b = Player.Player('b')
c = Player.Player('c')

d.deal_card(a)
d.deal_card(a)
d.deal_card(b)
d.deal_card(b)
c.add_card(Card(2,'D'))
c.add_card(Card(3,'H'))

print('{0} < {1} ? {2}'.format(a,c,a.hand<c.hand))
print('{0} < {1} ? {2}'.format(a,b,a.hand<b.hand))
print('{0} < {1} ? {2}'.format(c,b,c.hand<b.hand))

print('{0} = {1} ? {2}'.format(a,c,a.hand==c.hand))
print('{0} = {1} ? {2}'.format(a,b,a.hand==b.hand))
print('{0} = {1} ? {2}'.format(c,b,c.hand==b.hand))


def aa():
  print('A')

def bb():
  print('B')

funcs = [aa,bb]
for f in funcs:
  f()
