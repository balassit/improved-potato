#!/usr/bin/env python
import threading

shared_balance = 0


class Deposit(threading.Thread):
    def run(self):
        for _ in range(1000000):
            global shared_balance
            shared_balance += 100


class Withdraw(threading.Thread):
    def run(self):
        for _ in range(1000000):
            global shared_balance
            shared_balance -= 100


threads = [Deposit(), Withdraw()]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(shared_balance)
