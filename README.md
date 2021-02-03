---
home: true
lang: en-EN
footer: Made with ❤️ in Düsseldorf
---
![CI](https://github.com/ThisIsBenny/rki-vaccination-data/workflows/CI/badge.svg)

The API provides the current covid-19 vaccination data of the 16 German federal states as JSON.
The data source is an Excel sheet provided by RKI. The data will be updated every working day by the RKI.

# API

Base-URL: `https://rki-vaccination-data.vercel.app`

## Show vaccination data

 Returns json data with the numbers for germany and every state.

### Endpoint

```
  GET https://rki-vaccination-data.vercel.app/api
```

### Response

```json
{
  "lastUpdate": "2021-01-18T00:00:00",
  "states": {
    "Baden-Württemberg": {
      "total": 11100394,
      "rs": "08",
      "vaccinated": 122057,
      "vaccinated_by_accine": {
        "biontech": 121737,
        "moderna": 320
      },
      "difference_to_the_previous_day": 7354,
      "vaccinations_per_1000_inhabitants": 11.0,
      "quote": 1.1,
      "2nd_vaccination": {
        "vaccinated": 4457,
        "difference_to_the_previous_day": 1953
      }
    },
    "Bayern": {
      "total": 13124737,
      "rs": "09",
      "vaccinated": 220318,
      "vaccinated_by_accine": {
        "biontech": 213624,
        "moderna": 6694
      },
      "difference_to_the_previous_day": 6481,
      "vaccinations_per_1000_inhabitants": 16.79,
      "quote": 1.68,
      "2nd_vaccination": {
        "vaccinated": 419,
        "difference_to_the_previous_day": 419
      }
    },
    "Berlin": {
      "total": 3669491,
      "rs": "11",
      "vaccinated": 55134,
      "vaccinated_by_accine": {
        "biontech": 54499,
        "moderna": 635
      },
      "difference_to_the_previous_day": 2512,
      "vaccinations_per_1000_inhabitants": 15.02,
      "quote": 1.5,
      "2nd_vaccination": {
        "vaccinated": 4138,
        "difference_to_the_previous_day": 2205
      }
    },
    "Brandenburg": {
      "total": 2521893,
      "rs": "12",
      "vaccinated": 41094,
      "vaccinated_by_accine": {
        "biontech": 41094,
        "moderna": 0
      },
      "difference_to_the_previous_day": 2620,
      "vaccinations_per_1000_inhabitants": 16.29,
      "quote": 1.63,
      "2nd_vaccination": {
        "vaccinated": 0,
        "difference_to_the_previous_day": 0
      }
    },
    "Bremen": {
      "total": 681202,
      "rs": "04",
      "vaccinated": 12866,
      "vaccinated_by_accine": {
        "biontech": 12433,
        "moderna": 433
      },
      "difference_to_the_previous_day": 614,
      "vaccinations_per_1000_inhabitants": 18.89,
      "quote": 1.89,
      "2nd_vaccination": {
        "vaccinated": 390,
        "difference_to_the_previous_day": 318
      }
    },
    "Hamburg": {
      "total": 1847253,
      "rs": "02",
      "vaccinated": 26517,
      "vaccinated_by_accine": {
        "biontech": 26362,
        "moderna": 155
      },
      "difference_to_the_previous_day": 1945,
      "vaccinations_per_1000_inhabitants": 14.35,
      "quote": 1.44,
      "2nd_vaccination": {
        "vaccinated": 598,
        "difference_to_the_previous_day": 174
      }
    },
    "Hessen": {
      "total": 6288080,
      "rs": "06",
      "vaccinated": 74071,
      "vaccinated_by_accine": {
        "biontech": 74071,
        "moderna": 0
      },
      "difference_to_the_previous_day": 1255,
      "vaccinations_per_1000_inhabitants": 11.78,
      "quote": 1.18,
      "2nd_vaccination": {
        "vaccinated": 3000,
        "difference_to_the_previous_day": 1264
      }
    },
    "Mecklenburg-Vorpommern": {
      "total": 1608138,
      "rs": "13",
      "vaccinated": 39116,
      "vaccinated_by_accine": {
        "biontech": 38745,
        "moderna": 371
      },
      "difference_to_the_previous_day": 1420,
      "vaccinations_per_1000_inhabitants": 24.32,
      "quote": 2.43,
      "2nd_vaccination": {
        "vaccinated": 1157,
        "difference_to_the_previous_day": 1157
      }
    },
    "Niedersachsen": {
      "total": 7993608,
      "rs": "03",
      "vaccinated": 94116,
      "vaccinated_by_accine": {
        "biontech": 92738,
        "moderna": 1378
      },
      "difference_to_the_previous_day": 3546,
      "vaccinations_per_1000_inhabitants": 11.77,
      "quote": 1.18,
      "2nd_vaccination": {
        "vaccinated": 837,
        "difference_to_the_previous_day": 473
      }
    },
    "Nordrhein-Westfalen": {
      "total": 17947221,
      "rs": "05",
      "vaccinated": 218699,
      "vaccinated_by_accine": {
        "biontech": 218699,
        "moderna": 0
      },
      "difference_to_the_previous_day": 2360,
      "vaccinations_per_1000_inhabitants": 12.19,
      "quote": 1.22,
      "2nd_vaccination": {
        "vaccinated": 4593,
        "difference_to_the_previous_day": 1722
      }
    },
    "Rheinland-Pfalz": {
      "total": 4093903,
      "rs": "07",
      "vaccinated": 91423,
      "vaccinated_by_accine": {
        "biontech": 89129,
        "moderna": 2294
      },
      "difference_to_the_previous_day": 7496,
      "vaccinations_per_1000_inhabitants": 22.33,
      "quote": 2.23,
      "2nd_vaccination": {
        "vaccinated": 1196,
        "difference_to_the_previous_day": null
      }
    },
    "Saarland": {
      "total": 986887,
      "rs": "10",
      "vaccinated": 16957,
      "vaccinated_by_accine": {
        "biontech": 16957,
        "moderna": 0
      },
      "difference_to_the_previous_day": 1246,
      "vaccinations_per_1000_inhabitants": 17.18,
      "quote": 1.72,
      "2nd_vaccination": {
        "vaccinated": 0,
        "difference_to_the_previous_day": 0
      }
    },
    "Sachsen": {
      "total": 4071971,
      "rs": "14",
      "vaccinated": 53663,
      "vaccinated_by_accine": {
        "biontech": 53663,
        "moderna": 0
      },
      "difference_to_the_previous_day": 3661,
      "vaccinations_per_1000_inhabitants": 13.18,
      "quote": 1.32,
      "2nd_vaccination": {
        "vaccinated": 368,
        "difference_to_the_previous_day": null
      }
    },
    "Sachsen-Anhalt": {
      "total": 2194782,
      "rs": "15",
      "vaccinated": 34411,
      "vaccinated_by_accine": {
        "biontech": 34411,
        "moderna": 0
      },
      "difference_to_the_previous_day": 1263,
      "vaccinations_per_1000_inhabitants": 15.68,
      "quote": 1.57,
      "2nd_vaccination": {
        "vaccinated": 2927,
        "difference_to_the_previous_day": 2248
      }
    },
    "Schleswig-Holstein": {
      "total": 2903773,
      "rs": "01",
      "vaccinated": 69126,
      "vaccinated_by_accine": {
        "biontech": 69076,
        "moderna": 50
      },
      "difference_to_the_previous_day": 3277,
      "vaccinations_per_1000_inhabitants": 23.81,
      "quote": 2.38,
      "2nd_vaccination": {
        "vaccinated": 640,
        "difference_to_the_previous_day": 640
      }
    },
    "Thüringen": {
      "total": 2133378,
      "rs": "16",
      "vaccinated": 25975,
      "vaccinated_by_accine": {
        "biontech": 25975,
        "moderna": 0
      },
      "difference_to_the_previous_day": 2239,
      "vaccinations_per_1000_inhabitants": 12.18,
      "quote": 1.22,
      "2nd_vaccination": {
        "vaccinated": 21,
        "difference_to_the_previous_day": 21
      }
    }
  },
  "vaccinated": 1195543,
  "2nd_vaccination": {
    "vaccinated": 24741,
    "difference_to_the_previous_day": 12594
  },
  "sum_vaccine_doses": 1220284,
  "difference_to_the_previous_day": 49289,
  "vaccinations_per_1000_inhabitants": 14.38,
  "total": 83166711,
  "quote": 1.44
}
```

### Sample Call

  cURL:

  ```sh
    curl -X GET 'https://rki-vaccination-data.vercel.app/api'
  ```

  jQuery:

  ```javascript
    var settings = {
      "url": "https://rki-vaccination-data.vercel.app/api",
      "method": "GET"
    };

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
  ```
  
  Scriptable App:

  ```javascript
    const req = new Request('https://rki-vaccination-data.vercel.app/api')
    const res = await req.loadJSON()
    console.log(res)
  ```

# Code

The API Code is Open-Source

## API Interface

<<< @/api/index.py

## Scrapping Data

<<< @/api/_utils/scrap_data.py

# Data-Sources

* [https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Tabellen/bevoelkerung-nichtdeutsch-laender.html](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Tabellen/bevoelkerung-nichtdeutsch-laender.html)
* [https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquoten-Tab.html](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquoten-Tab.html)

Licence: Robert Koch-Institut (RKI), dl-de/by-2-0
