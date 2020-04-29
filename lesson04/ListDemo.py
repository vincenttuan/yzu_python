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
# 計算前三張的點數, A=1, 2=2 ... J,Q,K = 0.5
print(poker[:3])
def score(po): # 假設 po = ['A', 9, 'J']
    sum = 0
    for p in po:
        if p == 'A':
            sum = sum + 1
            continue

        if p == 'J' or p == 'Q' or p == 'K':
            sum = sum + 0.5
            continue

        sum = sum + p

    return sum

print(poker[:3], score(poker[:3]))
