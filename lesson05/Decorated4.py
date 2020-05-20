
def login(password):
    def decorated(func):
        def check():
            if password == 1234:
                print("登入成功")
                func()
            else:
                print("登入失敗")
                return None
        return check
    return decorated

@login(password=1234)
def report():
    print("密件: 今日頭條...")


report()

