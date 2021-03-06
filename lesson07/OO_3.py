class Account:
    name = '' # 公有變數
    __balance = 100  # 私有變數

    def __init__(self, name, money):
        self.name = name
        self.__balance = self.__balance + money

    def addBalance(self, money):
        if money > 0:
            self.__balance = self.__balance + money

    def __str__(self):
        return self.name + "有 $" + str(self.__balance)

if __name__ == '__main__':
    Account.bank = '元大銀行' # 靜態/類別變數
    acc = Account('Vincent', 200)
    print(Account.bank, acc)
    acc2 = Account('Mary', 500)
    print(Account.bank, acc2)
