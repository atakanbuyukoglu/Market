# A file to keep all constants for the base files

# Online Connection & Data Fetching
BASE_URL = "https://query1.finance.yahoo.com/v8/finance/chart/"
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36 '
}

FINANCIALS_SITE = lambda ticker : "https://finance.yahoo.com/quote/" + ticker + "/financials?p=" + ticker
