def make_dress(func):
    def dress():
        print("穿衣服")
        func()
    return dress

def out():
    print("我出門了")


m = make_dress(out)
m()
