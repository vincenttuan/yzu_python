def make_dress(func):
    def dress():
        print("穿衣服")
        func()
    return dress

@make_dress
def out():
    print("我出門了")

out()
