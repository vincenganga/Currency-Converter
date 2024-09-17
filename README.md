# CURRENCY CONVERTER
A simple Currency Converter developed using Python with 180 currencies available. 

## Table Of Contents:
* [About The Program](#about-the-program)
* [Requirements](#requirements)
* [Setup](#setup)
* [Usage Examples](#usage-examples)
* [Reference](#reference)

## About The Program
The program enables users to convert between various global currencies using real-time exchange rates.

**API Key**: 
Users are required to input a valid API key, which can be acquired from [free.currencyconverterapi.com](https://free.currencyconverterapi.com/). This key allows the program to fetch the latest exchange rates.

**List**: 
Enter the command `list` to view all available currencies, each presented with its ID, name, and symbol (e.g. `USD - United States Dollar - $`). If a currency symbol is not available, it will be displayed as blank.

**Exchange Rates**:
Use the `rate` command to fetch the exchange rate between two currencies. The program will ask for the currency IDs and retrieve the latest rates from the API.

**Conversions**:
To perform a currency conversion, use the `convert` command. The program will prompt you to enter the currency IDs and the amount you wish to convert. The converted amount will be displayed.

**Testing**:
To test the program, edit the `test_project.py` file with your API key and currency IDs, then run the program with `pytest test_project.py`.

## Requirements
- API key from [free.currencyconverterapi.com](https://free.currencyconverterapi.com/)
- Install python libraries
  ```
  pip install requests
  pip install pytest
  ```

## Setup
To run this project:

```
$ cd projectP
$ python project.py
$ pytest test_project.py
```

## Usage Examples
List available currencies:
```
$ python project.py
Enter your API key from freecurrencyconverter.com: YOUR_API_KEY
Enter a command (q to quit): list
```

Fetch exchange rates:
```
$ python project.py
Enter your API key from freecurrencyconverter.com: YOUR_API_KEY
Enter a command (q to quit): rate
``` 

Convert between currencies:
```
$ python project.py
Enter your API key from freecurrencyconverter.com: YOUR_API_KEY
Enter a command (q to quit): convert
```

## Reference
* [Requests Documentation](https://docs.python-requests.org/en/latest/).
* [Currency Converter API Documentation](https://free.currencyconverterapi.com/).
