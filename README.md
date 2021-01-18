---
home: true
lang: en-EN
footer: Made with ❤️ in Düsseldorf
---

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
  "lastUpdate": "2021-01-17T00:00:00",
  "states": {
    "Baden-Württemberg": {
      "total": 11100394,
      "rs": "08",
      "vaccinated": 114954,
      "vaccinated_by_accine": {
        "biontech": 114954,
        "moderna": 0
      },
      "difference_to_the_previous_day": 5352,
      "vaccinations_per_1000_inhabitants": 10.36,
      "quote": 1.04,
      "2nd-vaccination": {
        "vaccinated": 0,
        "difference_to_the_previous_day": 0
      }
    },
    "Bayern": {
      "total": 13124737,
      "rs": "09",
      "vaccinated": 213837,
      "vaccinated_by_accine": {
        "biontech": 213837,
        "moderna": 0
      },
      "difference_to_the_previous_day": 5296,
      "vaccinations_per_1000_inhabitants": 16.29,
      "quote": 1.63,
      "2nd-vaccination": {
        "vaccinated": 0,
        "difference_to_the_previous_day": 0
      }
    },
    "Berlin": {
      "total": 3669491,
      "rs": "11",
      "vaccinated": 52622,
      "vaccinated_by_accine": {
        "biontech": 52162,
        "moderna": 460
      },
      "difference_to_the_previous_day": 1571,
      "vaccinations_per_1000_inhabitants": 14.34,
      "quote": 1.43,
      "2nd-vaccination": {
        "vaccinated": 1933,
        "difference_to_the_previous_day": 1933
      }
    },
    "Brandenburg": {
      "total": 2521893,
      "rs": "12",
      "vaccinated": 38474,
      "vaccinated_by_accine": {
        "biontech": 38474,
        "moderna": 0
      },
      "difference_to_the_previous_day": 0,
      "vaccinations_per_1000_inhabitants": 15.26,
      "quote": 1.53,
      "2nd-vaccination": {
        "vaccinated": 0,
        "difference_to_the_previous_day": 0
      }
    },
    "Bremen": {
      "total": 681202,
      "rs": "04",
      "vaccinated": 11845,
      "vaccinated_by_accine": {
        "biontech": 11845,
        "moderna": 0
      },
      "difference_to_the_previous_day": 394,
      "vaccinations_per_1000_inhabitants": 17.39,
      "quote": 1.74,
      "2nd-vaccination": {
        "vaccinated": 0,
        "difference_to_the_previous_day": 0
      }
    },
    "Hamburg": {
      "total": 1847253,
      "rs": "02",
      "vaccinated": 24468,
      "vaccinated_by_accine": {
        "biontech": 24468,
        "moderna": 0
      },
      "difference_to_the_previous_day": 1184,
      "vaccinations_per_1000_inhabitants": 13.25,
      "quote": 1.32,
      "2nd-vaccination": {
        "vaccinated": 425,
        "difference_to_the_previous_day": 425
      }
    },
    "Hessen": {
      "total": 6288080,
      "rs": "06",
      "vaccinated": 72816,
      "vaccinated_by_accine": {
        "biontech": 72816,
        "moderna": 0
      },
      "difference_to_the_previous_day": 926,
      "vaccinations_per_1000_inhabitants": 11.58,
      "quote": 1.16,
      "2nd-vaccination": {
        "vaccinated": 1736,
        "difference_to_the_previous_day": 1736
      }
    },
    "Mecklenburg-Vorpommern": {
      "total": 1608138,
      "rs": "13",
      "vaccinated": 37564,
      "vaccinated_by_accine": {
        "biontech": 37444,
        "moderna": 120
      },
      "difference_to_the_previous_day": 0,
      "vaccinations_per_1000_inhabitants": 23.36,
      "quote": 2.34,
      "2nd-vaccination": {
        "vaccinated": 0,
        "difference_to_the_previous_day": 0
      }
    },
    "Niedersachsen": {
      "total": 7993608,
      "rs": "03",
      "vaccinated": 90005,
      "vaccinated_by_accine": {
        "biontech": 88766,
        "moderna": 1239
      },
      "difference_to_the_previous_day": 813,
      "vaccinations_per_1000_inhabitants": 11.26,
      "quote": 1.13,
      "2nd-vaccination": {
        "vaccinated": 335,
        "difference_to_the_previous_day": 335
      }
    },
    "Nordrhein-Westfalen": {
      "total": 17947221,
      "rs": "05",
      "vaccinated": 211779,
      "vaccinated_by_accine": {
        "biontech": 211779,
        "moderna": 0
      },
      "difference_to_the_previous_day": 5728,
      "vaccinations_per_1000_inhabitants": 11.8,
      "quote": 1.18,
      "2nd-vaccination": {
        "vaccinated": 968,
        "difference_to_the_previous_day": 906
      }
    },
    "Rheinland-Pfalz": {
      "total": 4093903,
      "rs": "07",
      "vaccinated": 82810,
      "vaccinated_by_accine": {
        "biontech": 81905,
        "moderna": 905
      },
      "difference_to_the_previous_day": 2879,
      "vaccinations_per_1000_inhabitants": 20.23,
      "quote": 2.02,
      "2nd-vaccination": {
        "vaccinated": 350,
        "difference_to_the_previous_day": 350
      }
    },
    "Saarland": {
      "total": 986887,
      "rs": "10",
      "vaccinated": 15711,
      "vaccinated_by_accine": {
        "biontech": 15711,
        "moderna": 0
      },
      "difference_to_the_previous_day": 250,
      "vaccinations_per_1000_inhabitants": 15.92,
      "quote": 1.59,
      "2nd-vaccination": {
        "vaccinated": 0,
        "difference_to_the_previous_day": 0
      }
    },
    "Sachsen": {
      "total": 4071971,
      "rs": "14",
      "vaccinated": 50002,
      "vaccinated_by_accine": {
        "biontech": 50002,
        "moderna": 0
      },
      "difference_to_the_previous_day": 3019,
      "vaccinations_per_1000_inhabitants": 12.28,
      "quote": 1.23,
      "2nd-vaccination": {
        "vaccinated": 155,
        "difference_to_the_previous_day": 155
      }
    },
    "Sachsen-Anhalt": {
      "total": 2194782,
      "rs": "15",
      "vaccinated": 33148,
      "vaccinated_by_accine": {
        "biontech": 33148,
        "moderna": 0
      },
      "difference_to_the_previous_day": 21,
      "vaccinations_per_1000_inhabitants": 15.1,
      "quote": 1.51,
      "2nd-vaccination": {
        "vaccinated": 679,
        "difference_to_the_previous_day": 624
      }
    },
    "Schleswig-Holstein": {
      "total": 2903773,
      "rs": "01",
      "vaccinated": 65849,
      "vaccinated_by_accine": {
        "biontech": 65849,
        "moderna": 0
      },
      "difference_to_the_previous_day": 3524,
      "vaccinations_per_1000_inhabitants": 22.68,
      "quote": 2.27,
      "2nd-vaccination": {
        "vaccinated": 0,
        "difference_to_the_previous_day": 0
      }
    },
    "Thüringen": {
      "total": 2133378,
      "rs": "16",
      "vaccinated": 23413,
      "vaccinated_by_accine": {
        "biontech": 23413,
        "moderna": 0
      },
      "difference_to_the_previous_day": 195,
      "vaccinations_per_1000_inhabitants": 10.97,
      "quote": 1.1,
      "2nd-vaccination": {
        "vaccinated": 0,
        "difference_to_the_previous_day": 0
      }
    }
  },
  "vaccinated": 1139297,
  "difference_to_the_previous_day": 31152,
  "vaccinations_per_1000_inhabitants": 13.7,
  "total": 83166711,
  "quote": 1.37
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

<<< @/api/index.py

# Data-Sources

* [https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Tabellen/bevoelkerung-nichtdeutsch-laender.html](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Tabellen/bevoelkerung-nichtdeutsch-laender.html)
* [https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquoten-Tab.html](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquoten-Tab.html)

Licence: Robert Koch-Institut (RKI), dl-de/by-2-0
