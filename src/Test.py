from OnlineData import YahooSession

session = YahooSession(delay=2.0)

ticker = 'MSFT'
financials_site = "https://finance.yahoo.com/quote/" + ticker + \
                    "/financials?p=" + ticker

result = session._parse_json(financials_site)
print(result.keys())
with open('file.txt', 'w') as file:
    file.write(str(result))