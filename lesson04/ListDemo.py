import operator
import random as r
poker1 = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
poker2 = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
print(operator.eq(poker1, poker2))

poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
print(poker)
print(len(poker))
print(poker.count('A'))
# 抽第一張牌
card = poker.pop(0)
print('抽第一張牌: ', card)
print(poker)
# 洗牌
r.shuffle(poker)
print(poker)

