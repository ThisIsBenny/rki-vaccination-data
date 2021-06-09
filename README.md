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
    "2nd_vaccination": {
        "difference_to_the_previous_day": 686432,
        "vaccinated": 18925419
    },
    "difference_to_the_previous_day": 369160,
    "lastUpdate": "2021-06-08T00:00:00",
    "quote": 46.46,
    "states": {
        "Baden-Württemberg": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 93977,
                "quote": 22.07,
                "vaccinated": 2450018,
                "vaccinated_by_accine": {
                    "astrazeneca": 156539,
                    "biontech": 1984153,
                    "janssen": 114950,
                    "moderna": 194376
                }
            },
            "difference_to_the_previous_day": 46226,
            "quote": 45.44,
            "rs": "08",
            "total": 11100394,
            "vaccinated": 5043780,
            "vaccinated_by_accine": {
                "astrazeneca": 1123971,
                "biontech": 3367902,
                "moderna": 436957
            },
            "vaccinations_per_1000_inhabitants": 454.38
        },
        "Bayern": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 112924,
                "quote": 22.77,
                "vaccinated": 2988266,
                "vaccinated_by_accine": {
                    "astrazeneca": 175837,
                    "biontech": 2457264,
                    "janssen": 116866,
                    "moderna": 238299
                }
            },
            "difference_to_the_previous_day": 39595,
            "quote": 44.86,
            "rs": "09",
            "total": 13124737,
            "vaccinated": 5887137,
            "vaccinated_by_accine": {
                "astrazeneca": 1282647,
                "biontech": 4085133,
                "moderna": 402491
            },
            "vaccinations_per_1000_inhabitants": 448.55
        },
        "Berlin": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 25355,
                "quote": 21.82,
                "vaccinated": 800831,
                "vaccinated_by_accine": {
                    "astrazeneca": 29917,
                    "biontech": 664969,
                    "janssen": 37226,
                    "moderna": 68719
                }
            },
            "difference_to_the_previous_day": 20437,
            "quote": 46.44,
            "rs": "11",
            "total": 3669491,
            "vaccinated": 1703976,
            "vaccinated_by_accine": {
                "astrazeneca": 345866,
                "biontech": 1141865,
                "moderna": 179019
            },
            "vaccinations_per_1000_inhabitants": 464.36
        },
        "Brandenburg": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 17943,
                "quote": 22.34,
                "vaccinated": 563361,
                "vaccinated_by_accine": {
                    "astrazeneca": 33127,
                    "biontech": 444996,
                    "janssen": 33569,
                    "moderna": 51669
                }
            },
            "difference_to_the_previous_day": 20690,
            "quote": 43.67,
            "rs": "12",
            "total": 2521893,
            "vaccinated": 1101293,
            "vaccinated_by_accine": {
                "astrazeneca": 241615,
                "biontech": 733946,
                "moderna": 92163
            },
            "vaccinations_per_1000_inhabitants": 436.69
        },
        "Bremen": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 5042,
                "quote": 25.71,
                "vaccinated": 175113,
                "vaccinated_by_accine": {
                    "astrazeneca": 8449,
                    "biontech": 140137,
                    "janssen": 13409,
                    "moderna": 13118
                }
            },
            "difference_to_the_previous_day": 3558,
            "quote": 50.44,
            "rs": "04",
            "total": 681202,
            "vaccinated": 343575,
            "vaccinated_by_accine": {
                "astrazeneca": 94011,
                "biontech": 215276,
                "moderna": 20879
            },
            "vaccinations_per_1000_inhabitants": 504.37
        },
        "Hamburg": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 13583,
                "quote": 22.11,
                "vaccinated": 408494,
                "vaccinated_by_accine": {
                    "astrazeneca": 9680,
                    "biontech": 331859,
                    "janssen": 21875,
                    "moderna": 45080
                }
            },
            "difference_to_the_previous_day": 6805,
            "quote": 43.8,
            "rs": "02",
            "total": 1847253,
            "vaccinated": 809087,
            "vaccinated_by_accine": {
                "astrazeneca": 174560,
                "biontech": 532005,
                "moderna": 80647
            },
            "vaccinations_per_1000_inhabitants": 437.99
        },
        "Hessen": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 51687,
                "quote": 20.09,
                "vaccinated": 1263355,
                "vaccinated_by_accine": {
                    "astrazeneca": 102484,
                    "biontech": 1027066,
                    "janssen": 53212,
                    "moderna": 80593
                }
            },
            "difference_to_the_previous_day": 26101,
            "quote": 46.13,
            "rs": "06",
            "total": 6288080,
            "vaccinated": 2900838,
            "vaccinated_by_accine": {
                "astrazeneca": 683245,
                "biontech": 1935174,
                "moderna": 229207
            },
            "vaccinations_per_1000_inhabitants": 461.32
        },
        "Mecklenburg-Vorpommern": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 16047,
                "quote": 24.1,
                "vaccinated": 387517,
                "vaccinated_by_accine": {
                    "astrazeneca": 15860,
                    "biontech": 327520,
                    "janssen": 16854,
                    "moderna": 27283
                }
            },
            "difference_to_the_previous_day": 7145,
            "quote": 47.81,
            "rs": "13",
            "total": 1608138,
            "vaccinated": 768833,
            "vaccinated_by_accine": {
                "astrazeneca": 141623,
                "biontech": 547819,
                "moderna": 62537
            },
            "vaccinations_per_1000_inhabitants": 478.09
        },
        "Niedersachsen": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 73396,
                "quote": 21.49,
                "vaccinated": 1717612,
                "vaccinated_by_accine": {
                    "astrazeneca": 71641,
                    "biontech": 1356977,
                    "janssen": 140822,
                    "moderna": 148172
                }
            },
            "difference_to_the_previous_day": 34591,
            "quote": 47.19,
            "rs": "03",
            "total": 7993608,
            "vaccinated": 3771792,
            "vaccinated_by_accine": {
                "astrazeneca": 1052128,
                "biontech": 2350736,
                "moderna": 228106
            },
            "vaccinations_per_1000_inhabitants": 471.85
        },
        "Nordrhein-Westfalen": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 151554,
                "quote": 23.37,
                "vaccinated": 4193619,
                "vaccinated_by_accine": {
                    "astrazeneca": 172843,
                    "biontech": 3541798,
                    "janssen": 240833,
                    "moderna": 238145
                }
            },
            "difference_to_the_previous_day": 66669,
            "quote": 49.06,
            "rs": "05",
            "total": 17947221,
            "vaccinated": 8805580,
            "vaccinated_by_accine": {
                "astrazeneca": 2125478,
                "biontech": 5792321,
                "moderna": 646948
            },
            "vaccinations_per_1000_inhabitants": 490.64
        },
        "Rheinland-Pfalz": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 31718,
                "quote": 23.0,
                "vaccinated": 941483,
                "vaccinated_by_accine": {
                    "astrazeneca": 50564,
                    "biontech": 799669,
                    "janssen": 39175,
                    "moderna": 52075
                }
            },
            "difference_to_the_previous_day": 26976,
            "quote": 45.22,
            "rs": "07",
            "total": 4093903,
            "vaccinated": 1851385,
            "vaccinated_by_accine": {
                "astrazeneca": 406217,
                "biontech": 1248976,
                "moderna": 157017
            },
            "vaccinations_per_1000_inhabitants": 452.23
        },
        "Saarland": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 10204,
                "quote": 26.91,
                "vaccinated": 265556,
                "vaccinated_by_accine": {
                    "astrazeneca": 10334,
                    "biontech": 230457,
                    "janssen": 9647,
                    "moderna": 15118
                }
            },
            "difference_to_the_previous_day": 5565,
            "quote": 49.65,
            "rs": "10",
            "total": 986887,
            "vaccinated": 490009,
            "vaccinated_by_accine": {
                "astrazeneca": 77975,
                "biontech": 366481,
                "moderna": 35906
            },
            "vaccinations_per_1000_inhabitants": 496.52
        },
        "Sachsen": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 21149,
                "quote": 24.86,
                "vaccinated": 1012261,
                "vaccinated_by_accine": {
                    "astrazeneca": 36808,
                    "biontech": 862374,
                    "janssen": 37545,
                    "moderna": 75534
                }
            },
            "difference_to_the_previous_day": 18812,
            "quote": 41.45,
            "rs": "14",
            "total": 4071971,
            "vaccinated": 1687997,
            "vaccinated_by_accine": {
                "astrazeneca": 333593,
                "biontech": 1156595,
                "moderna": 160264
            },
            "vaccinations_per_1000_inhabitants": 414.54
        },
        "Sachsen-Anhalt": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 21606,
                "quote": 22.58,
                "vaccinated": 495627,
                "vaccinated_by_accine": {
                    "astrazeneca": 23136,
                    "biontech": 395940,
                    "janssen": 31180,
                    "moderna": 45371
                }
            },
            "difference_to_the_previous_day": 10256,
            "quote": 44.98,
            "rs": "15",
            "total": 2194782,
            "vaccinated": 987279,
            "vaccinated_by_accine": {
                "astrazeneca": 190517,
                "biontech": 683933,
                "moderna": 81649
            },
            "vaccinations_per_1000_inhabitants": 449.83
        },
        "Schleswig-Holstein": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 23464,
                "quote": 24.2,
                "vaccinated": 702581,
                "vaccinated_by_accine": {
                    "astrazeneca": 41476,
                    "biontech": 568145,
                    "janssen": 36970,
                    "moderna": 55990
                }
            },
            "difference_to_the_previous_day": 22948,
            "quote": 48.41,
            "rs": "01",
            "total": 2903773,
            "vaccinated": 1405772,
            "vaccinated_by_accine": {
                "astrazeneca": 318780,
                "biontech": 952378,
                "moderna": 97644
            },
            "vaccinations_per_1000_inhabitants": 484.12
        },
        "Thüringen": {
            "2nd_vaccination": {
                "difference_to_the_previous_day": 14472,
                "quote": 23.55,
                "vaccinated": 502460,
                "vaccinated_by_accine": {
                    "astrazeneca": 29705,
                    "biontech": 422669,
                    "janssen": 18191,
                    "moderna": 31895
                }
            },
            "difference_to_the_previous_day": 10055,
            "quote": 44.79,
            "rs": "16",
            "total": 2133378,
            "vaccinated": 955588,
            "vaccinated_by_accine": {
                "astrazeneca": 160442,
                "biontech": 664981,
                "moderna": 111974
            },
            "vaccinations_per_1000_inhabitants": 447.92
        }
    },
    "sum_vaccine_doses": 57563348,
    "total": 83166711,
    "vaccinated": 38637929,
    "vaccinations_per_1000_inhabitants": 464.58
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

# Apps / websites that use the API

* [Number of Covid 19 vaccinations](https://widget-hub.app/widget/5fec48637b99ef0008e8a27d/number-of-covid-19-vaccinations) (iOS Scriptable Widget)
* [Impf-Status in Deutschland](https://play.google.com/store/apps/details?id=de.dschlapa.vaccination) (Android)
* [Hotspot or not?](https://hotspotornot.de/)
