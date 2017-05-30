from random import shuffle
from operator import attrgetter

###
class Card:
  '''Class to define type of cards'''
  suits = {'H': '\u2661',
           'D': '\u2662', 
           'S': '\u2660', 
           'C': '\u2663'}
  faces = {11: 'J',
           12: 'Q',
           13: 'K',
           14: 'A'}
  #______________________________
  def __init__(self, value, suit):
    self.value  = value
    self.suit   = suit
    self.name   = value if value < 11 else self.faces[value]
    self.symbol = self.suits[suit] 
  #______________________
  def __eq__(self, other):
    return self.value == other.value
  #______________________
  def __neq__(self, other):
    return not self.__eq__(other) 
  #______________________
  def __gt__(self, other):
    return self.value > other.value
  #_____________________
  def __lt__(self, other):
    return self.value < other.value
  #_______________
  def __repr__(self):
    return '[{0:>2}{1} ]'.format(self.name, self.symbol)
  #___________________
  def dump_state(self):
    print('{0}{1} (value={2}, suit={3})'.format(self.name,self.symbol,self.value,self.suit))




###
class Deck:
  '''Class to keep track of 
    state of deck'''
  suits  = ['H','D','S','C']
  values = [x for x in range(2,15)]
  #_________________
  def __init__(self):
    self.cards_left = 52
    self.deck = []
    self.fill_deck()
  #___________________
  def __repr__(self):
    s_deck = sorted(self.deck, key=attrgetter('suit', 'value'))
    h = " ".join(str(x) for x in s_deck if x.suit is 'H')
    d = " ".join(str(x) for x in s_deck if x.suit is 'D')
    s = " ".join(str(x) for x in s_deck if x.suit is 'S')
    c = " ".join(str(x) for x in s_deck if x.suit is 'C')
    return '{0}\n{1}\n{2}\n{3}'.format(h,d,s,c)
  #_________________
  def fill_deck(self):
    for s in self.suits:
      for v in self.values:
        self.deck.append(Card(v,s))
  #__________________
  def shuffle(self):
    shuffle(self.deck)
  #_________________________
  def deal_card(self, player):
    if len(self.deck) > 0:  
      if len(player.hand) < player.max_cards:
        card_to_deal = self.deck.pop(0)
        player.add_card(card_to_deal)
      else:
        print('{0} has too many cards !!!'.format(player.name))
    else:
      print('No more cards left!!')
