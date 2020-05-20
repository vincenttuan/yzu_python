class Account:
    name = '' # 公有變數
    __balance = 100  # 私有變數

    def addBalance(self, money):
        self.__balance = self.__balance + money

    def __str__(self):
        return self.name + "有 $" + str(self.__balance)

if __name__ == '__main__':
    acc = Account()
    acc.name = 'Vincent'
    acc.addBalance(200)
    print(acc)
