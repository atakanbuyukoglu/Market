from OnlineData import YahooSession
import Company

session = YahooSession(delay=2.0)

ticker = 'MSFT'
msft = Company.PublicCompany(ticker, ticker, session)

result = msft.info
print(result.keys())
with open('file.txt', 'w') as file:
    file.write(str(result))