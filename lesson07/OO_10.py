class YoyoCard:
    __balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, money):
        if money > 0:
            self.__balance = self.__balance + money

card = YoyoCard()
print(card.balance)
card.balance = 100
print(card.balance)