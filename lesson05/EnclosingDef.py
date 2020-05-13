def message(text):
    text = '元智:' + text
    def print_message():
        print(text)
    return print_message

m1 = message("Hello1")
m2 = message("Hello2")
m3 = message("Hello3")
#m1()