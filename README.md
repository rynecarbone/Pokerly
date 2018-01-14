# Pokerly
Attempt at poker simulator

## Basic example

### Create the deck and shuffle
```
my_deck = Deck()
my_deck.shuffle()
```

### Create some players
```
names = ['Alice','Bob','Cthulhu']
players = []
for n in names:
  players.append(Player.Player(n))
```

### Deal cards to the players
```
for _ in range(Player.max_cards):
  for p in players:
    my_deck.deal_card(p)
```

### Deal the flop, river turn
```
my_pool = PokerPool('Common Pool')
for _ in range(PokerPool.max_cards):
  my_deck.deal(my_pool)
```

### Print the state of the deck
Print out deck, ordered by value and suit for debugging
```
print(my_deck)
```

### Print the table cards
List the flop, river, turn cards available to all players
```
print(my_pool)
```

### Print players hands
Print players name and two dealt cards. Afterwards, display the highest ranking hand using the community pool cards. Print the cards used to rank the hand, and the kickers if any.
```
for p in players:
  i_hand = PokerHand(p.hand, my_pool.hand)
  i_hand.get_score()
  print('{0} Score:{1}'.format(p, i_hand.score))
  print('  Final Hand: {0}'.format(i_hand.final_hand))
  print('  Rank cards: {0}'.format(i_hand.rank_cards))
  print('Kicker Cards: {0}'.format(i_hand.kicker_cards))
```

### Simulation compared to theory
After 10k simulations, the number of hands reflects the theory probabilities very well
![Simulation histogram odds](poker_sim_ratio.png)

Score | Hand | % Simulated | % Predicted |
------|------|-------------|-------------|
1 |      High Card| 17.4710| 17.4119|
2 |       One Pair| 43.7390| 43.8225|
3 |       Two Pair| 23.5070| 23.4955|
4 |Three of a Kind| 4.7600 | 4.8299| 
5 |       Straight| 4.6030 | 4.6194| 
6 |          Flush| 3.1210 | 3.0255| 
7 |     Full House| 2.6240 | 2.5961| 
8  |Four of a Kind| 0.1500 | 0.1681| 
9  |Straight Flush |0.0220 | 0.0279 |
10 |Royal Flush | 0.0030 | 0.0032 |
