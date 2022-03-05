# Gets stock data from Yahoo, uses some code from yahoo_fin library

import requests
import time
import pandas as pd
import numpy as np
import json
import re
from Const import HEADERS, BASE_URL

# Static values for the session for data collection

class YahooSession(requests.Session):

    def __init__(self, delay=2.0):
        super(YahooSession, self).__init__()
        self.headers = HEADERS
        self.url = BASE_URL
        self.delay = delay

    def get(self, url, **kwargs):
        result = super(YahooSession, self).get(url, **kwargs)
        # Delay prevents IP blocking
        time.sleep(self.delay)

        return result

    def _build_url(self, ticker, start_date=None, end_date=None, interval="1d"):
        """
            Builds the URL and GET parameters for getting the price of a ticker.
        """
        # Initialize the end date
        if end_date is None:
            end_seconds = int(pd.Timestamp("now").timestamp())
        else:
            end_seconds = int(pd.Timestamp(end_date).timestamp())

        # Initialize the start date
        if start_date is None:
            start_seconds = 7223400
        else:
            start_seconds = int(pd.Timestamp(start_date).timestamp())


        site = self.url + ticker

        # "{}/v8/finance/chart/{}".format(self._base_url, self.ticker)

        params = {"period1": start_seconds, "period2": end_seconds,
                  "interval": interval.lower(), "events": "div,splits"}

        return site, params

    def get_data(self, ticker, start_date=None, end_date=None, index_as_date=True,
                 interval="1d", try_count = 5):
        """Downloads historical stock price data into a pandas data frame.  Interval
           must be "1d", "1wk", or "1mo" for daily, weekly, or monthly data.

           @param: ticker
           @param: start_date = None
           @param: end_date = None
           @param: index_as_date = True
           @param: interval = "1d"
        """

        if interval not in ("1d", "1wk", "1mo"):
            raise AssertionError("interval must be of of '1d', '1wk', or '1mo'")

        # build and connect to URL
        site, params = self._build_url(ticker, start_date, end_date, interval)
        resp = self.get(site, params=params)

        # Try again on error
        if not resp.status_code == 200 and try_count > 0:
            print(str(resp.status_code), 'Code for', ticker, ', retrying in 5 seconds.')
            time.sleep(3)
            return self.get_data(ticker, start_date, end_date, index_as_date, interval, try_count-1)
        elif try_count == 0:
            pass

        # Get JSON response
        data = resp.json()

        # get open / high / low / close data
        frame = pd.DataFrame(data["chart"]["result"][0]["indicators"]["quote"][0])

        # add in adjclose
        # frame["adjclose"] = data["chart"]["result"][0]["indicators"]["adjclose"][0]["adjclose"]

        # get the date info
        temp_time = data["chart"]["result"][0]["timestamp"]

        frame.index = pd.to_datetime(temp_time, unit="s")
        frame.index = frame.index.map(lambda dt: dt.floor("d"))

        # frame = frame[["open", "high", "low", "close", "adjclose", "volume"]]
        frame = frame[["open", "high", "low", "close", "volume"]]

        frame['ticker'] = ticker.upper()

        if not index_as_date:
            frame = frame.reset_index()
            frame.rename(columns={"index": "date"}, inplace=True)

        price_data = np.asarray([frame.close[-1], frame.high[-1], frame.low[-1], frame.open[-1], frame.volume[-1]])

        return price_data

    def get_live_price(self, ticker):
        """Gets the live price of input ticker

           @param: ticker
        """

        df = self.get_data(ticker, start_date=pd.Timestamp.today() + pd.DateOffset(-3), end_date=pd.Timestamp.today())

        return df

    def _parse_json(self, url):
        # Get the HTML response from the website as str
        html = self.get(url=url).text

        # Split the part before JSON
        json_str = html.split('root.App.main =')[1]
        # Split the part after JSON
        json_str = json_str.split('(this)')[0]

        json_str = json_str.split(';\n}')[0].strip()

        # The relevant data is in context -> dispatcher -> stores -> QuoteSummaryStore
        data = json.loads(json_str)['context']['dispatcher']['stores']

        data_summary = data['QuoteSummaryStore']
        data = data['QuoteTimeSeriesStore']

        # Replace empty dictionaries with null
        new_data = json.dumps(data).replace('{}', 'null')
        # TODO: Understand this line
        new_data = re.sub(r'{[\'|\"]raw[\'|\"]:(.*?),(.*?)}', r'\1', new_data)

        json_info = json.loads(new_data)

        # Replace empty dictionaries with null
        new_data = json.dumps(data_summary).replace('{}', 'null')
        # TODO: Understand this line
        new_data = re.sub(r'{[\'|\"]raw[\'|\"]:(.*?),(.*?)}', r'\1', new_data)
        
        json_info_summary = json.loads(new_data)

        return json_info_summary, json_info