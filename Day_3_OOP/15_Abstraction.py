# 15_Abstraction
# hiding the unnecessary data for others
# client Application
# self driving car

#  Hierarichal inheritance

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ${amount} using UPI")


payment = UPI()
payment.pay(500)

payment = CreditCard()
payment.pay(2000)

    