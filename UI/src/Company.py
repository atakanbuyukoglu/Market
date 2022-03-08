# Defines a company and related classes
from .OnlineData import YahooSession
from .Const import FINANCIALS_SITE
from abc import ABC, abstractmethod
from .Components import Component, CashComponent
from typing import Dict

class Company(ABC):

    def __init__(self, name) -> None:
        # Defining properties of the company
        self.name = name
        self.components = {}

    def add_component(self, comp_name: str, comp: Component):
        self.components[comp_name] = comp

    @abstractmethod
    def get_valuation(self):
        pass

class PublicCompany(Company):

    def __init__(self, name, ticker, session=None) -> None:
        super().__init__(name)
        self.ticker = ticker

            
        # Update online info if a connection is given
        if session:
            self.update_online_info(session)
        else:
            self.info_sum = None
            self.info = None

        
    def update_online_info(self, session: YahooSession):
        financials_site = FINANCIALS_SITE(self.ticker)
        self.info_sum, self.info = session._parse_json(financials_site)
        # Update the components using new information
        self.update_components()

    # TODO: Add a business component
    def update_components(self):
        # The cash component
        cash_amount = self.info_sum['balanceSheetHistoryQuarterly']['balanceSheetStatements'][0]['cash']
        cash_comp = CashComponent(amount=cash_amount)
        self.components['cash'] = cash_comp

    def get_valuation(self):
        total_value = 0.0
        for comp in self.components.values():
            comp_value = comp.get_value()
            total_value += comp_value

        return total_value
