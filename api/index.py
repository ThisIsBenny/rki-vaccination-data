from http.server import BaseHTTPRequestHandler
import json
import re
import datetime
import openpyxl
from io import BytesIO
import urllib.request

# Source http://www.statistikportal.de/de/bevoelkerung/flaeche-und-bevoelkerung
states = {
  'Baden-Württemberg': {
    'total': 11069533
  },
  'Bayern': {
    'total': 13076721
  },
  'Berlin': {
    'total': 3644826
  },
  'Brandenburg': {
    'total': 2511917
  },
  'Bremen': {
    'total': 682986
  },
  'Hamburg': {
    'total': 1841179
  },
  'Hessen': {
    'total': 6265809
  },
  'Mecklenburg-Vorpommern': {
    'total': 1609675
  },
  'Niedersachsen': {
    'total': 7982448
  },
  'Nordrhein-Westfalen': {
    'total': 17932651
  },
  'Rheinland-Pfalz': {
    'total': 4084844
  },
  'Saarland': {
    'total':  990509
  },
  'Sachsen': {
    'total': 4077937
  },
  'Sachsen-Anhalt': {
    'total': 2208321
  },
  'Schleswig-Holstein': {
    'total': 2896712
  },
  'Thüringen': {
    'total': 2143145
  }
}

sumStates = 0
sumDiffStates = 0
sum100States = 0

# Request to load excel sheet
url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquotenmonitoring.xlsx?__blob=publicationFile'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

req = urllib.request.Request(url, headers=hdr)
response = urllib.request.urlopen(req)
file = response.read()


# Read excel sheet
wb = openpyxl.load_workbook(filename = BytesIO(file)) 
sheet = wb[wb.sheetnames[1]]

# Load update time
lastUpdateRawString = wb.sheetnames[1]
relastUpdateMatch = re.search(r"[\d]{2}\.[\d]{2}\.[\d]{2}", lastUpdateRawString)
lastUpdate = datetime.datetime.strptime(relastUpdateMatch.group(), '%d.%m.%y')

# Load data from rows
for row in sheet.iter_rows(max_row=17):
  aColumn = row[1].value.replace("*", "")
  if aColumn in states:
    states[aColumn]['rs'] = str(row[0].value)
    states[aColumn]['vaccinated'] = row[2].value
    states[aColumn]['difference_to_the_previous_day'] = row[3].value
    states[aColumn]['vaccinations_per_1000_inhabitants'] = row[4].value
    states[aColumn]['quote'] = round(states[aColumn]['vaccinated'] / states[aColumn]['total'] * 100, 2)
    sumStates += states[aColumn]['vaccinated']
    sumDiffStates += states[aColumn]['difference_to_the_previous_day']
    sum100States += states[aColumn]['vaccinations_per_1000_inhabitants']

res = {
  'lastUpdate': lastUpdate.isoformat(),
  'states': states,
  'vaccinated': sumStates,
  'difference_to_the_previous_day': sumDiffStates,
  'vaccinations_per_1000_inhabitants': sum100States,
  'total': 83019213,
  'quote': round(sumStates / 83019213 * 100, 2)
}

# HTTP handler
class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-Type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(res).encode())
    return
