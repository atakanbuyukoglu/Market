# Component classes for the companies

from abc import ABC, abstractmethod


class Component(ABC):

    def __init__(self) -> None:
        # TODO: Implement a general component
        pass

    @abstractmethod
    def get_value(self) -> float:
        pass

class CashComponent(Component):

    def __init__(self, amount, multiplier=1.0) -> None:
        super().__init__()
        self.amount = amount
        self.mult = multiplier

    def get_value(self) -> float:
        return self.amount * self.mult

# TODO: Implement a Business Component
class BusinessComponent(Component):

    def __init__(self) -> None:
        super().__init__()