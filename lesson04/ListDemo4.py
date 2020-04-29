# 跟電腦對戰
import random as r

poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
# 計算分數
def getScore(po): # 假設 po = ['A', 9, 'J']
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
# 是否要補牌 (True, False)
def draw(pc):
    score = getScore(pc)
    if score >= 9:  # 不補牌
        return False
    if score <= 6:  # 強迫補牌
        return True
    if 6 < score < 8:  # 6.5, 7, 7.5
        # A、2、3, J, Q, K 剩餘的牌 >= 12 (補)
        count = poker.count('A') + \
                poker.count(2) + \
                poker.count(3) + \
                poker.count('J') + \
                poker.count('Q') + \
                poker.count('K')
        if count >= 12:
            return True
        else:
            return False
    if 8 <= score < 9:  # 8, 8.5
        # A、2、J, Q, K 剩餘的牌 >= 10 (補)
        count = poker.count('A') + \
                poker.count(2) + \
                poker.count('J') + \
                poker.count('Q') + \
                poker.count('K')
        if count >= 10:
            return True
        else:
            return False

