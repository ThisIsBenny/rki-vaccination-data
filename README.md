---
home: true
lang: en-EN
footer: Made with ❤️ in Düsseldorf
---

The API provides the current covid-19 vaccination data of the 16 German federal states as JSON.
The data source is an Excel sheet provided by RKI. The data will be updated every working day by the RKI.

# API

Base-URL: [https://rki-vaccination-data.vercel.app](https://rki-vaccination-data.vercel.app)

## Show vaccination data

 Returns json data with the numbers for germany and every state.

### Endpoint

```sh
  GET https://rki-vaccination-data.vercel.app/api
```

### Response

```json
{
  "lastUpdate": "2020-12-30T00:00:00",
  "total": 83019213,
  "vaccinated": 78109,
  "quote": 0.09,
  "states": {
      "Baden-Württemberg": {
          "quote": 0.07,
          "total": 11069533,
          "vaccinated": 8242
      },
      "Bayern": {
          "quote": 0.1,
          "total": 13076721,
          "vaccinated": 12935
      },
      "Berlin": {
          "quote": 0.17,
          "total": 3644826,
          "vaccinated": 6296
      },
      "Brandenburg": {
          "quote": 0.06,
          "total": 2511917,
          "vaccinated": 1553
      },
      "Bremen": {
          "quote": 0.16,
          "total": 682986,
          "vaccinated": 1059
      },
      "Hamburg": {
          "quote": 0.08,
          "total": 1841179,
          "vaccinated": 1499
      },
      "Hessen": {
          "quote": 0.15,
          "total": 6265809,
          "vaccinated": 9448
      },
      "Mecklenburg-Vorpommern": {
          "quote": 0.46,
          "total": 1609675,
          "vaccinated": 7338
      },
      "Niedersachsen": {
          "quote": 0.02,
          "total": 7982448,
          "vaccinated": 1527
      },
      "Nordrhein-Westfalen": {
          "quote": 0.06,
          "total": 17932651,
          "vaccinated": 11385
      },
      "Rheinland-Pfalz": {
          "quote": 0.06,
          "total": 4084844,
          "vaccinated": 2284
      },
      "Saarland": {
          "quote": 0.15,
          "total": 990509,
          "vaccinated": 1518
      },
      "Sachsen": {
          "quote": 0.04,
          "total": 4077937,
          "vaccinated": 1487
      },
      "Sachsen-Anhalt": {
          "quote": 0.33,
          "total": 2208321,
          "vaccinated": 7287
      },
      "Schleswig-Holstein": {
          "quote": 0.12,
          "total": 2896712,
          "vaccinated": 3579
      },
      "Thüringen": {
          "quote": 0.03,
          "total": 2143145,
          "vaccinated": 672
      }
  }
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
