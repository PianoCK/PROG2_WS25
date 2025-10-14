from abc import ABC, abstractmethod

class Zahlungsmethode(ABC):
    @abstractmethod
    def pay(self):
        pass

class Paypal(Zahlungsmethode):

    def pay(self):
        pass


paypal = Paypal()
paypal.pay()


