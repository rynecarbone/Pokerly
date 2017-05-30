from operator import attrgetter

###
class Hand:
  '''Class to define each hand and compare ranks'''
  #_________________
  def __init__(self):
    self.cards     = []
  #_________________
  def __repr__(self):
    return ' '.join(str(c) for c in self.sort_cards())
  #__________________
  def __len__(self):
    return len(self.cards)
  #______________________
  def __eq__(self, other):
    for s, o in zip(self.sort_cards(), other.sort_cards()):
      if s != o: return False
    return True
  #_____________________
  def __neq__(self, other):
    return not self.__eq__(other)
  #_____________________
  def __gt__(self, other):
    '''Don't reorder here, rank cards can have order,
       kickers, should be already sorted'''
    if self.__eq__(other): return False
    for s, o in zip(self.cards, other.cards):
      if s < o:
        return False
    return True
  #_____________________
  def __lt__(self, other):
    if self.__eq__(other): return False
    return not self.__gt__(other)
  #______________
  def sort_cards(self):
    return sorted(self.cards, key=attrgetter('value','suit'), reverse=True)
  #_______________________
  def add_card(self, card):
    self.cards.append(card)


###
class Player:
  '''Class to keep track of players'''
  max_cards = 2
  max_players = 5
  #_______________________
  def __init__(self, name):
    self.name = name
    self.hand = Hand()
  #________________
  def __repr__(self):
    return '%15s: %s'%(self.name, str(self.hand))
  #_______________________
  def add_card(self, card):
    if len(self.hand) < self.max_cards:
      self.hand.add_card(card)
    else:
      print('Too many cards! I musn\'t accept!')
