from abc import ABC, abstractmethod

class BillingStrategy(ABC):
    @abstractmethod
    def calculate(self, amount):
        pass

class InsuranceBilling(BillingStrategy):
    def calculate(self, amount):
        return amount * 0.2

class PrivateBilling(BillingStrategy):
    def calculate(self, amount):
        return amount

class AgreementBilling(BillingStrategy):
    def calculate(self, amount):
        return amount * 0.5