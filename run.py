#! /usr/bin/env python3
import Deck as D
import Player as P
import Game as G
import matplotlib.pyplot as plt
import cProfile
score_dict = {1:'High Card',
              2:'One Pair',
              3:'Two Pair',
              4:'Three of a Kind',
              5:'Straight',
              6:'Flush',
              7:'Full House',
              8:'Four of a Kind',
              9:'Straight Flush',
              10:'Royal Flush'}
tot_hands = float(133784560.) # 7 cards, choose best 5 (52 choose 7)
odds_dict = {1:23294460/tot_hands,
             2:58627800/tot_hands,
             3:31433400/tot_hands,
             4:6461620/tot_hands,
             5:6180020/tot_hands,
             6:4047644/tot_hands,
             7:3473184/tot_hands,
             8:224848/tot_hands,
             9:37260/tot_hands,
             10:4324/tot_hands}
#_________________
def print_result(deck, pool, players):
  '''Output results'''
  best_hand = None
  best_player = None
  tie_list = []
  # Print Deck
  print('Deck state:\n%s'%deck)
  # Print Pool
  print('\nPool of common cards:\n%s'%pool)
  # Print hands
  print('\nPlayers\' hands:')
  for p in players:
    i_poker_hand = G.PokerHand(p.hand,pool.hand)
    i_poker_hand.get_score()
    if not best_hand:
      best_player = p
      best_hand = i_poker_hand
    elif i_poker_hand.is_tie(best_hand.score, best_hand.rank_cards, best_hand.kicker_cards):
      tie_list.append(p)
    # if current is better than best, update
    elif not i_poker_hand.is_better(best_hand.score, best_hand.rank_cards, best_hand.kicker_cards):
      best_player = p
      best_hand = i_poker_hand
      tie_list = []
    print('\n{0}  Score:({1}) {2}'.format(p, i_poker_hand.score, score_dict[i_poker_hand.score]))
    print('\t\t  Final Hand: {0}'.format(i_poker_hand.final_hand))
    print('\t\t  Rank cards: {0}'.format(i_poker_hand.rank_cards)) 
    print('\t\tKicker Cards: {0}'.format(i_poker_hand.kicker_cards))
  # Print the winner
  print('\nWinner:\n{} ({})\n\t\t Final Hand:{}'.format(best_player, score_dict[best_hand.score] ,best_hand.final_hand))
  if len(tie_list) > 0:
    print('Tied:')
    for t in tie_list:
      print('{}'.format(t))
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
def set_up(n_runs=1000, num_players=3, print_state=False, print_stats=False):
  
  names_list = ['Alice','Bob','Cthulhu','Dude','Einstein','Feynman','Gandolf','Humpledink','Io','Jenkins']
  names = []
  if num_players > 10: num_players = 10
  for i in range(num_players):
    names.append(names_list[i])
  scores = [0,0,0,0,0,0,0,0,0,0]
  l_scores = []
  print('Simulating {} hands for {} players'.format(n_runs, num_players)) 
  for x in range(n_runs):
    
    if not x%1000: print('Simulation: {0}'.format(x))
    
    deck, pool, players, score = sim_game(names)
    if score > 10 or score < 1:
      print('Invalid score! {}'.format(score))
    scores[score-1] += 1
    l_scores.append(score)
    if print_state:
      print_result(deck, pool, players)
  
  
  if print_stats:
    for i in range(10,0,-1):
      print('({1:>2}) {0:>20}: {2:6.4f} % ({3:6.4f} %)'.format(score_dict[i], i, 
            100.*scores[i-1]/float(n_runs), 100*odds_dict[i]))
    odds_list = [odds_dict[x] for x in range(1,11)]
    bins = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5]
    # Plot histograms and ratio
    fig, (ax1, ax2) = plt.subplots(nrows=2)
    ns, bs, ps = ax1.hist(l_scores, bins=bins, normed=True, color="g", alpha=0.5, label="simulation")
    n2, b2, p2 = ax1.hist([x for x in range(1,11)], bins=bins, weights=odds_list, color="crimson",alpha=0.45, label="theory")
    ax1.legend(loc='upper right')
    ax1.set_xlim(0.5, 10.5)
    ax1.set_ylabel('Frequency')
    ratio = [ns[i]/n2[i]-1 if n2[i] != 0 else 0 for i in range(10)]
    bins = [i for i in range(1,11) ]
    ax2.bar(bins, ratio,align="center",bottom=1.0, width=1.0, alpha=0.75, color="midnightblue")
    ax2.set_ylabel('Ratio sim/theory')
    ax2.axhline(1, color='black')
    ax2.set_ylim(0.5,1.5)
    ax2.set_xlim(0.5,10.5)
    plt.show()

#__________
def main():
  # Verify long-term odds match expected for each outcome
  set_up(100000,num_players=1,print_state=False, print_stats=True) 
  # Analyze output of example round
  #set_up(1,num_players=5,print_state=True, print_stats=False) 

#________________________
if __name__ == "__main__":
  main()
