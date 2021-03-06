from itertools import combinations as combinations
from operator import attrgetter
import Player as P

###
class PokerPool(P.Player):
  '''Derived class for pool of common cards'''
  max_cards = 5
  def __init__(self, name):
    P.Player.__init__(self, name)
    self.hand.max_cards = self.max_cards

###
class PokerHand():
  '''Class for finding best hand with pool'''
  max_cards = 5
  #_____________________________
  def __init__(self, hand, pool):
    self.hand = hand.cards
    self.pool = pool.cards
    self.score = 0
  
  #_____________________________
  def is_tie(self, score, rank_cards, kicker_cards):
    '''
    Returns true if score is same, rank cards are identical,
    and kicker cards are identical
    '''
    if score != self.score:
      return False
    if rank_cards != self.rank_cards:
      return False
    if kicker_cards != self.kicker_cards:
      return False
    return True
  #_______________________
  def is_better(self, score, rank_cards, kicker_cards):
    '''Returns true if input score, rank, kicker
       is better than current hand
    '''
    if score > self.score:
      return True
    elif score == self.score:
      # Better rank of hand (e.g. KK vs QQ) FIXME be careful about two or more rank cards, order
      if rank_cards > self.rank_cards:
        return True
      # Better kickers (e.g. KK, Ace High vs KK, J high)
      elif rank_cards == self.rank_cards and kicker_cards > self.kicker_cards:
        return True
    # Current hand is better
    return False
    
  #__________________
  def get_score(self):
    my_poker  = Poker()
    card_pool = self.hand + self.pool
    hands     = list(combinations(card_pool, self.max_cards))
    for h in hands:
      i_s, i_rc, i_kc = my_poker.eval_hand(h)
      if self.is_better(i_s, i_rc, i_kc):
        self.update_hand(i_s, h, i_rc, i_kc)
  #_______________________________      
  def update_hand(self, s, fh, rc, kc):
    self.score = s
    self.rank_cards = rc
    self.kicker_cards = kc
    final_hand = P.Hand()
    for c in fh:
      final_hand.add_card(c)
    self.final_hand = final_hand

###
class Poker:
  '''Class to evaluate Poker hand'''
  
  def __init__(self):
    v = []
    s = []
    pass

  def values(self, cards):
    '''Returns sorted values'''
    #return sorted([c.value for c in cards], reverse=True)
    return [c.value for c in cards]
  def suits(self, cards):  
    '''Returns suits'''
    return [c.suit for c in cards]
  def n_kind(self, n, values):
    '''Returns n-of-a-kind value if exists'''
    return set( v for v in values if values.count(v) >= n)
  def is_straight(self, values):
    '''Returns straight, and ace-low'''
    ace_low  = len(set(values)) == 5 and values[0]-values[-1] == 12 and values[1] ==5
    straight = (len(set(values)) == 5 and values[0]-values[-1] == 4) or ace_low
    return straight, ace_low
  def is_flush(self, suits):
    '''Returns true if all same suit'''
    return len(set(suits)) == 1
  
  #______________________________________
  def straight_flush(self, cards, rc, kc):
    st, al = self.is_straight(self.v)
    fl = self.is_flush(self.s)
    # Royal Flush
    if st and fl:
      if self.v[-1] == 10:
        sc = 10
      #vAce-low straight flush
      elif al and fl:
        sc = 9
        rc.add_card(cards[1])
      # Other straight flush
      elif st and fl:
        sc = 9
        rc.add_card(cards[0])
      return sc, rc, kc
    return False
  #______________________________________
  def four_of_a_kind(self, cards, rc, kc):
    if self.k_4:
      sc = 8
      for c in cards:
        if c.value in self.k_4: rc.add_card(c)
        else: kc.add_card(c)
      return sc, rc, kc
    return False
  #__________________________________
  def full_house(self, cards, rc, kc):
    if self.k_3 and self.k_2 and len(self.k_2-self.k_3) > 0:
      sc = 7
      for c in cards:
        if c.value in self.k_3: rc.add_card(c)
      for c in cards:
        if c.value in (self.k_2 - self.k_3): rc.add_card(c)
      return sc, rc, kc
    return False
  #______________________________
  def flush(self, cards, rc, kc):
    if self.is_flush(self.s):
      sc = 6
      for c in cards:
        rc.add_card(c)
      return sc, rc, kc
    return False
  #________________________________
  def straight(self, cards, rc, kc):
    st, al = self.is_straight(self.v)
    if st:
      sc = 5
      rc.add_card(cards[1]) if al else rc.add_card(cards[0])
      return sc, rc, kc
    return False
  #_______________________________________
  def three_of_a_kind(self, cards, rc, kc):
    if self.k_3:
      sc = 4
      for c in cards:
        if c.value in self.k_3: rc.add_card(c)
        else: kc.add_card(c)
      return sc, rc, kc
    return False
  #________________________________
  def pair(self, cards, rc, kc):
    # Two pair
    if len(self.k_2) > 1:
      sc = 3
      for c in cards:
        if c.value == max(self.k_2): rc.add_card(c)
        elif c.value not in self.k_2: kc.add_card(c)
      for c in cards:
        if c.value == min(self.k_2): rc.add_card(c)
    # Pair
    elif self.k_2:
      sc = 2
      for c in cards:
        if c.value in self.k_2: rc.add_card(c)
        else: kc.add_card(c)
    # High card
    else:
      sc = 1
      for c in cards:
        if c.value == self.v[0]: rc.add_card(c)
        else: kc.add_card(c)
    return sc, rc, kc

  #_________________________
  def eval_hand(self, cards):
    poker_hands = [self.straight_flush,self.four_of_a_kind,self.full_house,
                   self.flush,self.straight,self.three_of_a_kind,self.pair]
    
    s_cards = sorted(cards, key=attrgetter('value','suits'), reverse=True)
    self.v = self.values(s_cards)
    self.s = self.suits(s_cards)
    self.k_4 = self.n_kind(4, self.v)
    self.k_3 = self.n_kind(3, self.v)
    self.k_2 = self.n_kind(2, self.v)

    rank_cards   = P.Hand()
    kicker_cards = P.Hand()
    for ranker in poker_hands:
      rank = ranker(s_cards, rank_cards, kicker_cards)
      if rank: break
    
    return rank[0], rank[1], rank[2]
