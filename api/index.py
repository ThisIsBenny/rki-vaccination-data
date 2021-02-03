""" API Endpont """
from http.server import BaseHTTPRequestHandler
import json
import datetime
# pylint: disable=import-error
from api._utils import scrap_data

try:
  data = scrap_data.get_data()
  res = {
    'lastUpdate': data['lastUpdate'].isoformat(),
    'states': data['states'],
    'vaccinated': data['sumStates'],
    '2nd_vaccination': {
      'vaccinated': data['sumStates2nd'],
      'difference_to_the_previous_day': data['sumDiffStates2nd']
    },
    'sum_vaccine_doses': data['sumStates'] + data['sumStates2nd'],
    'difference_to_the_previous_day': data['sumDiffStates'],
    'vaccinations_per_1000_inhabitants': round(data['sumStates'] / data['totalGermany'] * 1000, 2),
    'total': data['totalGermany'],
    'quote': round(data['sumStates'] / data['totalGermany'] * 100, 2)
  }
  HTTPCODE = 200
except TypeError:
  res = {
    'message': 'scrapping data from RKI excel failed'
  }
  HTTPCODE = 500

class Handler(BaseHTTPRequestHandler):
  """ HTTP Handler """
  # pylint: disable=invalid-name
  def do_GET(self):
    """ GET Method """
    self.send_response(HTTPCODE)
    self.send_header('Content-Type', 'application/json')
    self.send_header('X-Cache-Timestamp', datetime.datetime.now().isoformat())
    self.end_headers()
    self.wfile.write(json.dumps(res).encode())
