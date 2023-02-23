from flask import Flask, render_template
from alpha_vantage.timeseries import TimeSeries

import requests




"""
A example for creating a Table that is sortable by its header
"""

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=AG47OQX2ERZB1NEK'
r = requests.get(url)
data = r.json()

lastRefreshed = data['Meta Data']['3. Last Refreshed']

app = Flask(__name__)
data = [{
  "Stock" : data['Meta Data']['2. Symbol'],
  "Date" : lastRefreshed,
  "Open": data['Time Series (5min)'][lastRefreshed]['1. open'],
  "High": data['Time Series (5min)'][lastRefreshed]['2. high'],
  "Low": data['Time Series (5min)'][lastRefreshed]['3. low'],
  "Close": data['Time Series (5min)'][lastRefreshed]['4. close'],
  "Volume" : data['Time Series (5min)'][lastRefreshed]['5. volume']
}]
# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
columns = [
  {
    "field": "Stock", # which is the field's name of data key 
    "title": "Stock", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "Date", 
    "title": "Date(Last Refreshed)",
    "sortable": True,
  },
  {
    "field": "Open",
    "title": "Open",
    "sortable": True,
  },
  {
    "field": "High",
    "title": "High",
    "sortable": True,
  },
  {
    "field": "Low",
    "title": "Low",
    "sortable": True,
  },
  {
    "field": "Close",
    "title": "Close",
    "sortable": True,
  },
  {
    "field": "Volume",
    "title": "Volume",
    "sortable": True,
  }
]


@app.route('/')
def index():
    return render_template("table.html",
      data=data,
      columns=columns,
      title='Stock Table')


if __name__ == '__main__':

  app.run(debug=True)