from OnlineData import YahooSession
import Company

session = YahooSession(delay=2.0)

ticker = 'MSFT'
msft = Company.PublicCompany(ticker, ticker, session)

print(msft.get_valuation())