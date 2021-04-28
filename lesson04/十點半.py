import random
# 10點半撲克遊戲
# 玩法 : A~10 代表點數 1~10, J,Q,K 代表半點
#       輪流取牌, 若手上的牌點數總和最接近10點半就算贏, 超過就爆(輸了)
# ♠	♥ ♦ ♣
poker1 = ['♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K']
poker2 = ['♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K']
poker3 = ['♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K']
poker4 = ['♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K']

poker = poker1 + poker2 + poker3 + poker4

random.shuffle(poker)
#print(poker)

sum = 0.0
# for item in poker[:2]:
#     num = item[1:2]
#     print(num)
#     if num.isdigit():  # 2~10
#         sum += int(num)
#     elif num == 'A':
#         sum += 1
#     else:
#         sum += 0.5
#
# print(sum)

for item in poker[:5]:
    play = input('是否要牌 y=要 n=不要 ?')
    if(play == 'n'):
        break
    num = item[1:2]
    if num.isdigit():
        sum += int(num)
    elif num == 'A':
        sum += 1
    else:
        sum += 0.5
    print('抽到 %s 總點數 %.1f' % (num, sum))

    if sum == 10.5:
        print('厲害厲害')
        break
    elif sum > 10.5:
        print('Sorry 爆了')
        break

print(sum)
