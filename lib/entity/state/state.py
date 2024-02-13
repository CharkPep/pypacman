from abc import ABC, abstractmethod


class EntityState(ABC):

    @abstractmethod
    def handle_event(self, event):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def next(self):
        pass
