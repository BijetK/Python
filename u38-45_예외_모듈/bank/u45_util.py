class Account:
    def __init__(self, ano, owner, balance):
        self.ano = str(ano)
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        if self.__balance + amount >= 10000000:
            print('입금할 수 없습니다.')
            return
        self.__balance += amount
        print(f'남은 잔액은 {self.__balance}원 입니다.')

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print('잔액이 부족합니다.')
            return
        self.__balance -= amount
        print(f'남은 잔액은 {self.__balance}원 입니다')

    def __str__(self):
        return f'계좌번호 : {self.ano}, 소유주 : {self.owner}, 잔액 : {self.__balance}'