import random as r

lotto = set()
while len(lotto) < 5:
    lotto.add(r.randint(1, 39))
print(lotto)
