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


class BusinessComponent(Component):

    def __init__(self, sales, sale_costs, running_costs, tax, sector_multiplier) -> None:
        super().__init__()

        self.sales = sales
        self.sale_costs = sale_costs
        self.gross_income = sales - sale_costs
        self.running_costs = running_costs
        self.ebit = self.gross_income - running_costs
        self.earn_bef_int = self.ebit - tax
        self.tax = tax

        self.multiplier = sector_multiplier

    def get_value(self) -> float:
        return self.earn_bef_int * self.multiplier
