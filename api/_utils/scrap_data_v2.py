""" Scrap Data from Excel sheet """
import re
import datetime
from io import BytesIO
import urllib.request
import openpyxl
from .statics import inhabitants


def get_file():
  """ Get remote file content """
  # Request to load excel sheet
  url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten' \
      '/Impfquotenmonitoring.xlsx?__blob=publicationFile'
  hdr = {
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11'
      ' (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

  req = urllib.request.Request(url, headers=hdr)
  with urllib.request.urlopen(req) as response:
    return response.read()


def get_data():
  """ Get Data for API """
  states = inhabitants.STATES

  file = get_file()

  # Read excel sheet
  work_book = openpyxl.load_workbook(filename=BytesIO(file))
  sheet = work_book[work_book.sheetnames[2]]

  # Load update time
  last_update_raw_string = work_book.sheetnames[2]
  relast_update_match = re.search(
      r"[\d]{2}\.[\d]{2}\.[\d]{2}", last_update_raw_string)
  last_update = datetime.datetime.strptime(
      relast_update_match.group(), '%d.%m.%y')

  # Load data from rows
  rows = []
  for row in sheet.iter_rows(max_row=21):
    if row[1].value is None:
      continue
    state = row[1].value.replace("*", "").strip()
    if state in states or state == 'Bundesressorts':
      if state == 'Bundesressorts':
        total = 0
      else:
        total = states[state]['total']

      d = {
        "name": state,
        "inhabitants": total,
        "rs": str(row[0].value),
        "vaccinatedAtLeastOnce": {
          "doses": row[2].value,
          "difference_to_the_previous_day": row[7].value,
          "vaccine": [
            {
              "name": "biontech",
              "doses": row[3].value
            },
            {
              "name": "moderna",
              "doses": row[4].value
            },
            {
              "name": "astrazeneca",
              "doses": row[5].value
            },
            {
              "name": "janssen",
              "doses": row[6].value
            }
          ]
        },
        "fullyVaccinated": {
          "doses": row[8].value,
          "difference_to_the_previous_day": row[13].value,
          "vaccine": [
            {
              "name": "biontech",
              "doses": row[9].value
            },
            {
              "name": "moderna",
              "doses": row[10].value
            },
            {
              "name": "astrazeneca",
              "doses": row[11].value
            },
            {
              "name": "janssen",
              "doses": row[12].value
            }
          ]
        }
      }
      rows.append(d)
  return {
    "lastUpdate": last_update,
    "data": rows
  }