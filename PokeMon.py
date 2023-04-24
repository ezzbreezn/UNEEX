from collections import defaultdict

players = defaultdict(set)
decks = defaultdict(set)
s = input()
while s:
    if s[0] >= '0' and s[0] <= '9':
        num_deck, name = s.split(' / ')
        decks[num_deck].add(name)
    else:
        player, num_deck = s.split(' / ')
        players[player].add(num_deck)
    s = input()
    
players_max_set = []
max_num = 0
for name, nums in players.items():
    deck = set()
    for elem in nums:
        deck = deck.union(decks[elem])
    deck_size = len(deck)
    if max_num < deck_size:
        max_num = deck_size
        players_max_set = [name]
    elif max_num == deck_size:
        players_max_set.append(name)
            
for name in sorted(players_max_set):
    print(name)
