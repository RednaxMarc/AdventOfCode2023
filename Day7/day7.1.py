rank_map = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
hands = {}

with open('test.txt', 'r') as file:
    for line in file:
        hand, bid = line.strip().split(' ')    
        # Hands
        hands[hand] = bid
    print(hands)

    types={"fioak":[], "fooak":[], "fh":[],"troak":[],"tp":[],"pair":[],"high":[]} #five of a kind, four of a kind, full house, three of a kind, two pair, pair, high card
    types_in_order_of_value = ["high","pair","tp","troak","fh","fooak","fioak"]
    for hand in hands:
        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1
        print(counts)
