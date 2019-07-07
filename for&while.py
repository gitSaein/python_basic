for _ in range(3):
    print("아주 잘 했어요!")
for i, n in enumerate(range(3)):
    print(n + 1)
num2 = []
for n in range(1, 6):
    num2.append((n ** 2))
    print(num2)
num2 = [n ** 2 for n in range(1, 6)]
print(num2)

profiles = [['이', '성주'], ['김', '성주']]
print(profiles[0])
성, 이름 = profiles[0]
print(성 + 이름)

for 성, 이름 in profiles:
    print(성 + 이름)

profiles = {0: "성주", 1: '1234'}
for key in profiles:
    value = profiles[key]
    print(key, value)
suits = ["a", "b", "c", "d"]
ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
print(ranks)

deck = []
for s in suits:
    for r in ranks:
        cards = [s, r]
        deck.append(cards)
print(deck)
