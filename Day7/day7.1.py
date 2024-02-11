with open("input.txt","r") as ifile:
    cards={}
    for line in ifile:
        c,v = line.strip().split(" ")
        # replace the letters in descending order of values (for sorting later on, kinda hacky)
        c=c.replace("A","Z")
        c=c.replace("K","Y")
        c=c.replace("Q","X")
        c=c.replace("J","W")
        c=c.replace("T","V")
        cards[c]=v
# print(cards)
        
types={"high":[], "pair":[], "tp":[],"troak":[],"fh":[],"fooak":[],"fioak":[]} #five of a kind, four of a kind, full house, three of a kind, two pair, pair, high card
# types ordered from lowest to highest (to retrieve ranks at the end)
types_in_order_of_value = ["high","pair","tp","troak","fh","fooak","fioak"]

# sort cards into types
for card in cards:
    sets = set(list(card))
    # print(sets)
    counts={y:card.count(y) for y in sets}
    # print(counts)

    if len(sets) == 1:
        types["fioak"].append(card)
    elif len(sets) == 2:
        if 4 in counts.values():
            types["fooak"].append(card)
        else:
            types["fh"].append(card)
    elif len(sets) == 3:
        if 3 in counts.values():
            types["troak"].append(card)
        else:
            types["tp"].append(card)
    elif len(sets) == 4:
        types["pair"].append(card)
    else:
        types["high"].append(card)

# print(types)
# print(types_in_order_of_value)

# sort types
for t in types:
    types[t].sort()
# print(types)

rank = 1
scores = 0
for t in types_in_order_of_value:
    for card in types[t]:
        # print('Rank: {} \tCard: {} \tBid: {} \tScore: {}'.format(rank,card,cards[card],rank*int(cards[card])))
        scores+=rank*int(cards[card])
        rank+=1
print(scores)

        

