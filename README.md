---
home: true
lang: en-EN
footer: Made with ❤️ in Düsseldorf
---
![CI](https://github.com/ThisIsBenny/rki-vaccination-data/workflows/CI/badge.svg)

The API provides the current covid-19 vaccination data of the 16 German federal states as JSON.
The data source is an Excel sheet provided by RKI. The data will be updated every working day by the RKI.

# API

_Note: v2 of the API was introduced and the documentation was adapted to the new version. v1 of the API is still available._

Base-URL: `https://rki-vaccination-data.vercel.app`

## Show vaccination data

 Returns json data with the numbers for germany and every state.

### Endpoint

```
  GET https://rki-vaccination-data.vercel.app/api/v2
```

### Response

```json
{
  "lastUpdate": "2021-06-10T00:00:00",
  "data": [{
    "name": "Baden-Württemberg",
    "inhabitants": 11100394,
    "isState": true,
    "rs": "08",
    "vaccinatedAtLeastOnce": {
      "doses": 5162993,
      "quote": 46.51,
      "differenceToThePreviousDay": 54493,
      "vaccine": [{
        "name": "biontech",
        "doses": 3458328
      }, {
        "name": "moderna",
        "doses": 443518
      }, {
        "name": "astrazeneca",
        "doses": 1129631
      }, {
        "name": "janssen",
        "doses": 131516
      }]
    },
    "fullyVaccinated": {
      "doses": 2679782,
      "quote": 24.14,
      "differenceToThePreviousDay": 105744,
      "vaccine": [{
        "name": "biontech",
        "doses": 2171831
      }, {
        "name": "moderna",
        "doses": 211981
      }, {
        "name": "astrazeneca",
        "doses": 164454
      }, {
        "name": "janssen",
        "doses": 131516
      }]
    }
  }, {
    "name": "Bayern",
    "inhabitants": 13124737,
    "isState": true,
    "rs": "09",
    "vaccinatedAtLeastOnce": {
      "doses": 5997556,
      "quote": 45.7,
      "differenceToThePreviousDay": 50791,
      "vaccine": [{
        "name": "biontech",
        "doses": 4160449
      }, {
        "name": "moderna",
        "doses": 406212
      }, {
        "name": "astrazeneca",
        "doses": 1288901
      }, {
        "name": "janssen",
        "doses": 141994
      }]
    },
    "fullyVaccinated": {
      "doses": 3266743,
      "quote": 24.89,
      "differenceToThePreviousDay": 123492,
      "vaccine": [{
        "name": "biontech",
        "doses": 2683410
      }, {
        "name": "moderna",
        "doses": 257641
      }, {
        "name": "astrazeneca",
        "doses": 183698
      }, {
        "name": "janssen",
        "doses": 141994
      }]
    }
  }, {
    "name": "Berlin",
    "inhabitants": 3669491,
    "isState": true,
    "rs": "11",
    "vaccinatedAtLeastOnce": {
      "doses": 1748925,
      "quote": 47.66,
      "differenceToThePreviousDay": 21612,
      "vaccine": [{
        "name": "biontech",
        "doses": 1173163
      }, {
        "name": "moderna",
        "doses": 184189
      }, {
        "name": "astrazeneca",
        "doses": 348119
      }, {
        "name": "janssen",
        "doses": 43454
      }]
    },
    "fullyVaccinated": {
      "doses": 863354,
      "quote": 23.53,
      "differenceToThePreviousDay": 29028,
      "vaccine": [{
        "name": "biontech",
        "doses": 714850
      }, {
        "name": "moderna",
        "doses": 71379
      }, {
        "name": "astrazeneca",
        "doses": 33671
      }, {
        "name": "janssen",
        "doses": 43454
      }]
    }
  }, {
    "name": "Brandenburg",
    "inhabitants": 2521893,
    "isState": true,
    "rs": "12",
    "vaccinatedAtLeastOnce": {
      "doses": 1148445,
      "quote": 45.54,
      "differenceToThePreviousDay": 23288,
      "vaccine": [{
        "name": "biontech",
        "doses": 766860
      }, {
        "name": "moderna",
        "doses": 98322
      }, {
        "name": "astrazeneca",
        "doses": 243246
      }, {
        "name": "janssen",
        "doses": 40017
      }]
    },
    "fullyVaccinated": {
      "doses": 605625,
      "quote": 24.01,
      "differenceToThePreviousDay": 19476,
      "vaccine": [{
        "name": "biontech",
        "doses": 477478
      }, {
        "name": "moderna",
        "doses": 53359
      }, {
        "name": "astrazeneca",
        "doses": 34771
      }, {
        "name": "janssen",
        "doses": 40017
      }]
    }
  }, {
    "name": "Bremen",
    "inhabitants": 681202,
    "isState": true,
    "rs": "04",
    "vaccinatedAtLeastOnce": {
      "doses": 354840,
      "quote": 52.09,
      "differenceToThePreviousDay": 5815,
      "vaccine": [{
        "name": "biontech",
        "doses": 224174
      }, {
        "name": "moderna",
        "doses": 21549
      }, {
        "name": "astrazeneca",
        "doses": 94450
      }, {
        "name": "janssen",
        "doses": 14667
      }]
    },
    "fullyVaccinated": {
      "doses": 187163,
      "quote": 27.48,
      "differenceToThePreviousDay": 5294,
      "vaccine": [{
        "name": "biontech",
        "doses": 149527
      }, {
        "name": "moderna",
        "doses": 13728
      }, {
        "name": "astrazeneca",
        "doses": 9241
      }, {
        "name": "janssen",
        "doses": 14667
      }]
    }
  }, {
    "name": "Hamburg",
    "inhabitants": 1847253,
    "isState": true,
    "rs": "02",
    "vaccinatedAtLeastOnce": {
      "doses": 825353,
      "quote": 44.68,
      "differenceToThePreviousDay": 8959,
      "vaccine": [{
        "name": "biontech",
        "doses": 542067
      }, {
        "name": "moderna",
        "doses": 80893
      }, {
        "name": "astrazeneca",
        "doses": 176029
      }, {
        "name": "janssen",
        "doses": 26364
      }]
    },
    "fullyVaccinated": {
      "doses": 437952,
      "quote": 23.71,
      "differenceToThePreviousDay": 17014,
      "vaccine": [{
        "name": "biontech",
        "doses": 353002
      }, {
        "name": "moderna",
        "doses": 48522
      }, {
        "name": "astrazeneca",
        "doses": 10064
      }, {
        "name": "janssen",
        "doses": 26364
      }]
    }
  }, {
    "name": "Hessen",
    "inhabitants": 6288080,
    "isState": true,
    "rs": "06",
    "vaccinatedAtLeastOnce": {
      "doses": 2967688,
      "quote": 47.2,
      "differenceToThePreviousDay": 26924,
      "vaccine": [{
        "name": "biontech",
        "doses": 1982634
      }, {
        "name": "moderna",
        "doses": 231673
      }, {
        "name": "astrazeneca",
        "doses": 688018
      }, {
        "name": "janssen",
        "doses": 65363
      }]
    },
    "fullyVaccinated": {
      "doses": 1395446,
      "quote": 22.19,
      "differenceToThePreviousDay": 56931,
      "vaccine": [{
        "name": "biontech",
        "doses": 1132737
      }, {
        "name": "moderna",
        "doses": 91533
      }, {
        "name": "astrazeneca",
        "doses": 105813
      }, {
        "name": "janssen",
        "doses": 65363
      }]
    }
  }, {
    "name": "Mecklenburg-Vorpommern",
    "inhabitants": 1608138,
    "isState": true,
    "rs": "13",
    "vaccinatedAtLeastOnce": {
      "doses": 785489,
      "quote": 48.84,
      "differenceToThePreviousDay": 8589,
      "vaccine": [{
        "name": "biontech",
        "doses": 560146
      }, {
        "name": "moderna",
        "doses": 63599
      }, {
        "name": "astrazeneca",
        "doses": 142080
      }, {
        "name": "janssen",
        "doses": 19664
      }]
    },
    "fullyVaccinated": {
      "doses": 429517,
      "quote": 26.71,
      "differenceToThePreviousDay": 20498,
      "vaccine": [{
        "name": "biontech",
        "doses": 364389
      }, {
        "name": "moderna",
        "doses": 28337
      }, {
        "name": "astrazeneca",
        "doses": 17127
      }, {
        "name": "janssen",
        "doses": 19664
      }]
    }
  }, {
    "name": "Niedersachsen",
    "inhabitants": 7993608,
    "isState": true,
    "rs": "03",
    "vaccinatedAtLeastOnce": {
      "doses": 3865057,
      "quote": 48.35,
      "differenceToThePreviousDay": 41865,
      "vaccine": [{
        "name": "biontech",
        "doses": 2403169
      }, {
        "name": "moderna",
        "doses": 236562
      }, {
        "name": "astrazeneca",
        "doses": 1059786
      }, {
        "name": "janssen",
        "doses": 165540
      }]
    },
    "fullyVaccinated": {
      "doses": 1911217,
      "quote": 23.91,
      "differenceToThePreviousDay": 83860,
      "vaccine": [{
        "name": "biontech",
        "doses": 1513838
      }, {
        "name": "moderna",
        "doses": 156927
      }, {
        "name": "astrazeneca",
        "doses": 74912
      }, {
        "name": "janssen",
        "doses": 165540
      }]
    }
  }, {
    "name": "Nordrhein-Westfalen",
    "inhabitants": 17947221,
    "isState": true,
    "rs": "05",
    "vaccinatedAtLeastOnce": {
      "doses": 8981678,
      "quote": 50.04,
      "differenceToThePreviousDay": 75307,
      "vaccine": [{
        "name": "biontech",
        "doses": 5900753
      }, {
        "name": "moderna",
        "doses": 649639
      }, {
        "name": "astrazeneca",
        "doses": 2142432
      }, {
        "name": "janssen",
        "doses": 288854
      }]
    },
    "fullyVaccinated": {
      "doses": 4603066,
      "quote": 25.65,
      "differenceToThePreviousDay": 167665,
      "vaccine": [{
        "name": "biontech",
        "doses": 3860158
      }, {
        "name": "moderna",
        "doses": 263053
      }, {
        "name": "astrazeneca",
        "doses": 191001
      }, {
        "name": "janssen",
        "doses": 288854
      }]
    }
  }, {
    "name": "Rheinland-Pfalz",
    "inhabitants": 4093903,
    "isState": true,
    "rs": "07",
    "vaccinatedAtLeastOnce": {
      "doses": 1912371,
      "quote": 46.71,
      "differenceToThePreviousDay": 26711,
      "vaccine": [{
        "name": "biontech",
        "doses": 1286009
      }, {
        "name": "moderna",
        "doses": 168833
      }, {
        "name": "astrazeneca",
        "doses": 408676
      }, {
        "name": "janssen",
        "doses": 48853
      }]
    },
    "fullyVaccinated": {
      "doses": 1016635,
      "quote": 24.83,
      "differenceToThePreviousDay": 29445,
      "vaccine": [{
        "name": "biontech",
        "doses": 858066
      }, {
        "name": "moderna",
        "doses": 55760
      }, {
        "name": "astrazeneca",
        "doses": 53956
      }, {
        "name": "janssen",
        "doses": 48853
      }]
    }
  }, {
    "name": "Saarland",
    "inhabitants": 986887,
    "isState": true,
    "rs": "10",
    "vaccinatedAtLeastOnce": {
      "doses": 502948,
      "quote": 50.96,
      "differenceToThePreviousDay": 5962,
      "vaccine": [{
        "name": "biontech",
        "doses": 376290
      }, {
        "name": "moderna",
        "doses": 36157
      }, {
        "name": "astrazeneca",
        "doses": 78632
      }, {
        "name": "janssen",
        "doses": 11869
      }]
    },
    "fullyVaccinated": {
      "doses": 289544,
      "quote": 29.34,
      "differenceToThePreviousDay": 10794,
      "vaccine": [{
        "name": "biontech",
        "doses": 250920
      }, {
        "name": "moderna",
        "doses": 16011
      }, {
        "name": "astrazeneca",
        "doses": 10744
      }, {
        "name": "janssen",
        "doses": 11869
      }]
    }
  }, {
    "name": "Sachsen",
    "inhabitants": 4071971,
    "isState": true,
    "rs": "14",
    "vaccinatedAtLeastOnce": {
      "doses": 1736798,
      "quote": 42.65,
      "differenceToThePreviousDay": 23409,
      "vaccine": [{
        "name": "biontech",
        "doses": 1194663
      }, {
        "name": "moderna",
        "doses": 161736
      }, {
        "name": "astrazeneca",
        "doses": 336326
      }, {
        "name": "janssen",
        "doses": 44073
      }]
    },
    "fullyVaccinated": {
      "doses": 1067551,
      "quote": 26.22,
      "differenceToThePreviousDay": 25766,
      "vaccine": [{
        "name": "biontech",
        "doses": 898957
      }, {
        "name": "moderna",
        "doses": 81087
      }, {
        "name": "astrazeneca",
        "doses": 43434
      }, {
        "name": "janssen",
        "doses": 44073
      }]
    }
  }, {
    "name": "Sachsen-Anhalt",
    "inhabitants": 2194782,
    "isState": true,
    "rs": "15",
    "vaccinatedAtLeastOnce": {
      "doses": 985654,
      "quote": 44.91,
      "differenceToThePreviousDay": 13588,
      "vaccine": [{
        "name": "biontech",
        "doses": 677695
      }, {
        "name": "moderna",
        "doses": 85185
      }, {
        "name": "astrazeneca",
        "doses": 184491
      }, {
        "name": "janssen",
        "doses": 38283
      }]
    },
    "fullyVaccinated": {
      "doses": 540620,
      "quote": 24.63,
      "differenceToThePreviousDay": 19655,
      "vaccine": [{
        "name": "biontech",
        "doses": 430185
      }, {
        "name": "moderna",
        "doses": 46119
      }, {
        "name": "astrazeneca",
        "doses": 26033
      }, {
        "name": "janssen",
        "doses": 38283
      }]
    }
  }, {
    "name": "Schleswig-Holstein",
    "inhabitants": 2903773,
    "isState": true,
    "rs": "01",
    "vaccinatedAtLeastOnce": {
      "doses": 1453333,
      "quote": 50.05,
      "differenceToThePreviousDay": 21580,
      "vaccine": [{
        "name": "biontech",
        "doses": 984112
      }, {
        "name": "moderna",
        "doses": 101284
      }, {
        "name": "astrazeneca",
        "doses": 324245
      }, {
        "name": "janssen",
        "doses": 43692
      }]
    },
    "fullyVaccinated": {
      "doses": 757298,
      "quote": 26.08,
      "differenceToThePreviousDay": 22415,
      "vaccine": [{
        "name": "biontech",
        "doses": 612893
      }, {
        "name": "moderna",
        "doses": 57750
      }, {
        "name": "astrazeneca",
        "doses": 42963
      }, {
        "name": "janssen",
        "doses": 43692
      }]
    }
  }, {
    "name": "Thüringen",
    "inhabitants": 2133378,
    "isState": true,
    "rs": "16",
    "vaccinatedAtLeastOnce": {
      "doses": 974457,
      "quote": 45.68,
      "differenceToThePreviousDay": 10321,
      "vaccine": [{
        "name": "biontech",
        "doses": 679316
      }, {
        "name": "moderna",
        "doses": 112873
      }, {
        "name": "astrazeneca",
        "doses": 161076
      }, {
        "name": "janssen",
        "doses": 21192
      }]
    },
    "fullyVaccinated": {
      "doses": 534526,
      "quote": 25.06,
      "differenceToThePreviousDay": 17225,
      "vaccine": [{
        "name": "biontech",
        "doses": 448856
      }, {
        "name": "moderna",
        "doses": 32616
      }, {
        "name": "astrazeneca",
        "doses": 31862
      }, {
        "name": "janssen",
        "doses": 21192
      }]
    }
  }, {
    "name": "Bundesressorts",
    "inhabitants": 0,
    "isState": false,
    "rs": "",
    "vaccinatedAtLeastOnce": {
      "doses": 135585,
      "quote": 0,
      "differenceToThePreviousDay": 6622,
      "vaccine": [{
        "name": "biontech",
        "doses": 39751
      }, {
        "name": "moderna",
        "doses": 73836
      }, {
        "name": "astrazeneca",
        "doses": 18293
      }, {
        "name": "janssen",
        "doses": 3705
      }]
    },
    "fullyVaccinated": {
      "doses": 62422,
      "quote": 0,
      "differenceToThePreviousDay": 2140,
      "vaccine": [{
        "name": "biontech",
        "doses": 2038
      }, {
        "name": "moderna",
        "doses": 50093
      }, {
        "name": "astrazeneca",
        "doses": 6586
      }, {
        "name": "janssen",
        "doses": 3705
      }]
    }
  }, {
    "name": "Deutschland",
    "inhabitants": 83166711,
    "isState": false,
    "rs": "",
    "vaccinatedAtLeastOnce": {
      "doses": 39539170,
      "quote": 47.54,
      "differenceToThePreviousDay": 425836,
      "vaccine": [{
        "name": "biontech",
        "doses": 26409579
      }, {
        "name": "moderna",
        "doses": 3156060
      }, {
        "name": "astrazeneca",
        "doses": 8824431
      }, {
        "name": "janssen",
        "doses": 1149100
      }]
    },
    "fullyVaccinated": {
      "doses": 20648461,
      "quote": 24.83,
      "differenceToThePreviousDay": 756442,
      "vaccine": [{
        "name": "biontech",
        "doses": 16923135
      }, {
        "name": "moderna",
        "doses": 1535896
      }, {
        "name": "astrazeneca",
        "doses": 1040330
      }, {
        "name": "janssen",
        "doses": 1149100
      }]
    }
  }]
}
```

### Sample Call

  cURL:

  ```sh
    curl -X GET 'https://rki-vaccination-data.vercel.app/api/v2'
  ```

  jQuery:

  ```javascript
    var settings = {
      "url": "https://rki-vaccination-data.vercel.app/api/v2",
      "method": "GET"
    };

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
  ```
  
  Scriptable App:

  ```javascript
    const req = new Request('https://rki-vaccination-data.vercel.app/api/v2')
    const res = await req.loadJSON()
    console.log(res)
  ```

# Code

The API Code is Open-Source

## API Interface

<<< @/api/v2.py

## Scrapping Data

<<< @/api/_utils/scrap_data_v2.py

# Data-Sources

* [https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Tabellen/bevoelkerung-nichtdeutsch-laender.html](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Tabellen/bevoelkerung-nichtdeutsch-laender.html)
* [https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquoten-Tab.html](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquoten-Tab.html)

Licence: Robert Koch-Institut (RKI), dl-de/by-2-0

# Apps / websites that use the API

* [Number of Covid 19 vaccinations](https://widget-hub.app/widget/5fec48637b99ef0008e8a27d/number-of-covid-19-vaccinations) (iOS Scriptable Widget)
* [Impf-Status in Deutschland](https://play.google.com/store/apps/details?id=de.dschlapa.vaccination) (Android)
* [Hotspot or not?](https://hotspotornot.de/)
