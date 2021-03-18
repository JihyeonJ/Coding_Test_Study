n = int(input())
card = [i for i in range(1, n+1)]
discarded_card = []

while len(discarded_card) != (n-1):
    discarded_card.append(card.pop(0))
    card.append(card.pop(0))

for i in discarded_card:
    print(i, end=' ')
print(card[0])