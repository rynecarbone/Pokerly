#! /usr/bin/env python3
import Deck as D
import Player as P
import Game as G

#_______________________
def main():
  
  # Create game
  #my_poker = G.Poker()

  # Create deck
  my_deck = D.Deck()
  my_deck.shuffle()
  
  # Create 3 Players
  p_names = ['Coco','Murulai','Naughtily']
  players = []
  for p in p_names:
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

  # Print Deck
  print('Deck state:\n%s'%my_deck)
  
  # Print Pool
  print('\nPool of common cards:\n%s'%my_pool)
  
  # Print hands
  print('\nPlayers\' hands:')
  for p in players:
    i_poker_hand = G.PokerHand(p.hand,my_pool.hand)
    i_poker_hand.get_score()
    print('\n{0}  Score:{1}'.format(p, i_poker_hand.score))
    print('\t\t  Final Hand: {0}'.format(i_poker_hand.final_hand))
    print('\t\t  Rank cards: {0}'.format(i_poker_hand.rank_cards)) 
    print('\t\tKicker Cards: {0}'.format(i_poker_hand.kicker_cards)) 
#________________________
if __name__ == "__main__":
  main()
