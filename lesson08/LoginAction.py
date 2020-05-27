import lesson08.MyException as me

def login(username, password):
    if username == 'admin' and password == '1234':
        pass
    else:
        raise me.LoginException('登入失敗!')

if __name__ == '__main__':
    try:
        login('admin', '5678')
    except me.LoginException as e:
        print(e)
        e.howToDo()