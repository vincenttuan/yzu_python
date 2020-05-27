class LoginException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()

    def howToDo(self):
        print('請重新登入')
        print('若仍無法登入請電詢xxx-xxx-xxxx')
