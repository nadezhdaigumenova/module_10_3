import time
import threading
from random import randint

class Bank:
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            how_much = randint(50, 500)
            self.balance +=how_much
            print(f'Пополнение: {how_much}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            how_much = randint(50, 500)
            print(f'Запрос на {how_much}.')
            if how_much <= self.balance:
                self.balance -= how_much
                print(f'Снятие: {how_much}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()