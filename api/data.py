from http.server import BaseHTTPRequestHandler
import json
import openpyxl
from io import BytesIO
import urllib.request

states = {
  'Baden-Württemberg': {
    'total': 0
  },
  'Bayern': {
    'total': 0
  },
  'Berlin': {
    'total': 0
  },
  'Brandenburg': {
    'total': 0
  },
  'Bremen': {
    'total': 0
  },
  'Hamburg': {
    'total': 0
  },
  'Hessen': {
    'total': 0
  },
  'Mecklenburg-Vorpommern': {
    'total': 0
  },
  'Niedersachsen': {
    'total': 0
  },
  'Nordrhein-Westfalen': {
    'total': 0
  },
  'Rheinland-Pfalz': {
    'total': 0
  },
  'Saarland': {
    'total': 0
  },
  'Sachsen': {
    'total': 0
  },
  'Sachsen-Anhalt': {
    'total': 0
  },
  'Schleswig-Holstein': {
    'total': 0
  },
  'Thüringen': {
    'total': 0
  }
}

sumStates = 0

url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquotenmonitoring.xlsx?__blob=publicationFile'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

req = urllib.request.Request(url, headers=hdr)
response = urllib.request.urlopen(req)
file = response.read()

wb = openpyxl.load_workbook(filename = BytesIO(file)) 
sheet = wb['Presse']
for row in sheet.iter_rows(max_row=17):
  aColumn = row[0].value.replace("*", "")
  if aColumn in states:
    states[aColumn]['vaccinated'] = row[1].value
    sumStates = sumStates + row[1].value

response = {
  'states': states,
  'vaccinated': sumStates,
  'total': 0
}

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.send_header('Cache-Control', 's-maxage=7200, stale-while-revalidate')
    self.end_headers()
    self.wfile.write(json.dumps(res).encode())
    return