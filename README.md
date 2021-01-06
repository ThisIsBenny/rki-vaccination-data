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
  "lastUpdate": "2021-01-04T00:00:00",
  "states": {
    "Baden-Württemberg": {
      "total": 11069533,
      "vaccinated": 32182,
      "difference": 4758,
      "vaccinations_per_1000_inhabitants": 2.8991763715774415,
      "quote": 0.29
    },
    "Bayern": {
      "total": 13076721,
      "vaccinated": 77876,
      "difference": 11618,
      "vaccinations_per_1000_inhabitants": 5.933528420417111,
      "quote": 0.6
    },
    "Berlin": {
      "total": 3644826,
      "vaccinated": 19389,
      "difference": 1631,
      "vaccinations_per_1000_inhabitants": 5.28383909375987,
      "quote": 0.53
    },
    "Brandenburg": {
      "total": 2511917,
      "vaccinated": 3334,
      "difference": 25,
      "vaccinations_per_1000_inhabitants": 1.3220227820926582,
      "quote": 0.13
    },
    "Bremen": {
      "total": 682986,
      "vaccinated": 2653,
      "difference": 700,
      "vaccinations_per_1000_inhabitants": 3.894586334156388,
      "quote": 0.39
    },
    "Hamburg": {
      "total": 1841179,
      "vaccinated": 4756,
      "difference": 616,
      "vaccinations_per_1000_inhabitants": 2.5746337940715214,
      "quote": 0.26
    },
    "Hessen": {
      "total": 6265809,
      "vaccinated": 37795,
      "difference": 4390,
      "vaccinations_per_1000_inhabitants": 6.010578745817483,
      "quote": 0.6
    },
    "Mecklenburg-Vorpommern": {
      "total": 1609675,
      "vaccinated": 13832,
      "difference": 1773,
      "vaccinations_per_1000_inhabitants": 8.601251882612065,
      "quote": 0.86
    },
    "Niedersachsen": {
      "total": 7982448,
      "vaccinated": 8665,
      "difference": 3271,
      "vaccinations_per_1000_inhabitants": 1.083991108896008,
      "quote": 0.11
    },
    "Nordrhein-Westfalen": {
      "total": 17932651,
      "vaccinated": 62692,
      "difference": 4435,
      "vaccinations_per_1000_inhabitants": 3.4931313321432884,
      "quote": 0.35
    },
    "Rheinland-Pfalz": {
      "total": 4084844,
      "vaccinated": 9891,
      "difference": 1609,
      "vaccinations_per_1000_inhabitants": 2.4160318405199144,
      "quote": 0.24
    },
    "Saarland": {
      "total": 990509,
      "vaccinated": 4836,
      "difference": 687,
      "vaccinations_per_1000_inhabitants": 4.9002570709716515,
      "quote": 0.49
    },
    "Sachsen": {
      "total": 4077937,
      "vaccinated": 7740,
      "difference": 2874,
      "vaccinations_per_1000_inhabitants": 1.9007993917441948,
      "quote": 0.19
    },
    "Sachsen-Anhalt": {
      "total": 2208321,
      "vaccinated": 15628,
      "difference": 2262,
      "vaccinations_per_1000_inhabitants": 7.120524954186794,
      "quote": 0.71
    },
    "Schleswig-Holstein": {
      "total": 2896712,
      "vaccinated": 12978,
      "difference": 3421,
      "vaccinations_per_1000_inhabitants": 4.469357625406669,
      "quote": 0.45
    },
    "Thüringen": {
      "total": 2143145,
      "vaccinated": 2715,
      "difference": 493,
      "vaccinations_per_1000_inhabitants": 1.2726296043176597,
      "quote": 0.13
    }
  },
  "vaccinated": 316962,
  "difference": 44563,
  "vaccinations_per_1000_inhabitants": 3.8111643010627176,
  "total": 83019213,
  "quote": 0.38
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

* [http://www.statistikportal.de/de/bevoelkerung/flaeche-und-bevoelkerung](http://www.statistikportal.de/de/bevoelkerung/flaeche-und-bevoelkerung)
* [https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquoten-Tab.html](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquoten-Tab.html)
