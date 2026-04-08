from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class EmailNotifier(Observer):
    def update(self, message):
        print(f"[Email] {message}")

class SMSNotifier(Observer):
    def update(self, message):
        print(f"[SMS] {message}")

class NotificationService:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for obs in self.observers:
            obs.update(message)