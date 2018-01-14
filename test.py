import Deck
from Deck import Card as Card
import Player
from Game import PokerPool as PP
from Game import PokerHand as PH

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

def test_tie():
  print('Testing two players tieing')
  pool = PP('pool')
  pool.add_card(Card(10,'S'))
  pool.add_card(Card(10,'C'))
  pool.add_card(Card(14,'D'))
  pool.add_card(Card(4,'H'))
  pool.add_card(Card(7,'C'))
  
  alice = Player.Player('Alice')
  alice.add_card(Card(9,'H'))
  alice.add_card(Card(9,'D'))
  poker_alice = PH(alice.hand, pool.hand)
  poker_alice.get_score()
  
  bob = Player.Player('Bob')
  bob.add_card(Card(9,'C'))
  bob.add_card(Card(9,'S'))
  poker_bob = PH(bob.hand, pool.hand)
  poker_bob.get_score()
  print('{}'.format(pool))
  print('{}:\n\t\t final hand:{}\n{}:\n\t\t final hand:{}'.format(alice, poker_alice.final_hand, bob, poker_bob.final_hand))
  
  if poker_alice.is_tie(poker_bob.score, poker_bob.rank_cards, poker_bob.kicker_cards):
    print('\nHands are equal, there is a tie!')
  else:
    print('\nHands are not equal, no tie :(')

funcs = [aa,bb, test_tie]
for f in funcs:
  f()
