# Defines a company and related classes
from OnlineData import YahooSession

class Company:

    def __init__(self, name) -> None:
        # Defining properties of the company
        self.name = name

class PublicCompany(Company):

    def __init__(self, name, ticker, session=None) -> None:
        super().__init__(name)
        self.ticker = ticker

            
        # Update online info if a connection is given
        if session:
            self.update_online_info(session)
        else:
            self.info = None

        
    def update_online_info(self, session: YahooSession):
        financials_site = "https://finance.yahoo.com/quote/" + self.ticker + "/financials?p=" + self.ticker
        self.info = session._parse_json(financials_site)
