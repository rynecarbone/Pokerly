#! /usr/bin/env python3
import Deck as D
import Player as P
import Game as G
import matplotlib.pyplot as plt
import cProfile

#_________________
def print_result(deck, pool, players):
  '''Output results'''
  # Print Deck
  print('Deck state:\n%s'%deck)
  # Print Pool
  print('\nPool of common cards:\n%s'%pool)
  # Print hands
  print('\nPlayers\' hands:')
  for p in players:
    i_poker_hand = G.PokerHand(p.hand,pool.hand)
    i_poker_hand.get_score()
    print('\n{0}  Score:{1}'.format(p, i_poker_hand.score))
    print('\t\t  Final Hand: {0}'.format(i_poker_hand.final_hand))
    print('\t\t  Rank cards: {0}'.format(i_poker_hand.rank_cards)) 
    print('\t\tKicker Cards: {0}'.format(i_poker_hand.kicker_cards)) 

#______________
def sim_game(names):
  '''Create deck, deal to players'''
  # Create deck
  my_deck = D.Deck()
  my_deck.shuffle()
  # Create 3 Players
  players = []
  for p in names:
    if len(players) < P.Player.max_players:
      players.append(P.Player(p))
  # Deal hands
  for _ in range(P.Player.max_cards):
    for p in players:
      my_deck.deal_card(p)
  # Deal Pool
  my_pool = G.PokerPool('common_pool')
  for _ in range(G.PokerPool.max_cards):
    my_deck.deal_card(my_pool)
  # Score hands
  top_score = 0
  for p in players:
    i_poker_hand = G.PokerHand(p.hand,my_pool.hand)
    i_poker_hand.get_score()
    if i_poker_hand.score > top_score: top_score = i_poker_hand.score
  return my_deck, my_pool, players, top_score

#_______________________
def set_up(n_runs=1000, print_state=False, print_stats=False):
  
  names = ['Alice','Bob','Cthulhu']
  scores = [0,0,0,0,0,0,0,0,0,0]
  l_scores = []
  
  for x in range(n_runs):
    
    if not x%1000: print('Simulation: {0}'.format(x))
    
    deck, pool, players, score = sim_game(names)
    scores[score-1] += 1
    l_scores.append(score)
    if print_state:
      print_result(deck, pool, players)
  

  if print_stats:
    for i,s in enumerate(scores):
      print('{0} {1}'.format(i, s/10000.))
    plt.hist(l_scores,range(11))
    plt.show()

#__________
def main():
  set_up(3,print_state=True) 

#________________________
if __name__ == "__main__":
  main()
