""" API Endpont """
from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime
import pytz
# pylint: disable=import-error
from api._utils import scrap_data_v2

try:
  data = scrap_data_v2.get_data()
  res = {
    'lastUpdate': data['lastUpdate'].isoformat(),
    'data': data['data']
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
    self.send_header('X-Cache-Timestamp',
      pytz.timezone('Europe/Berlin').localize(datetime.now()).isoformat())
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()
    self.wfile.write(json.dumps(res).encode())
