def message(text):
    text = '元智:' + text
    def print_message():
        print(text)
    return print_message() # 有括號會直接執行

m1 = message("Hello1")
