#!/usr/bin/env python3

class Account(object):
    """The Account class,
    The amount is in dollars.
    """
    def __init__(self, rate):
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        "The amount of money in the account"
        return self.__amt

    @property
    def inr(self):
        "Gives the money in INR value."
        return self.__amt * self.rate

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("Sorry, no negative amount in the account.")
            return
        self.__amt = value

if __name__ == '__main__':
    acc = Account(rate=61) # Based on today's value of INR :(
    acc.amount = 20
    print("Dollar amount:", acc.amount)
    print("In INR:", acc.inr)
    acc.amount = -100
    print("Dollar amount:", acc.amount)
