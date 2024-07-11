# import random
# number = random.randint(1,10)
# print(number)
# print(random.choice(["Headd", "tail"]))

# from random import choice
# coin = choice(["heads", "tails", "draw"])
# print(coin)

# import random
# number = random.randint(1,10)
# print(number)


import random
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
