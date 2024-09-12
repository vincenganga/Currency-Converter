# CURRENCY CONVERTER
A simple Currency Converter developed using Python with 180 currencies available

## Table Of Contents:
* [About The Program](#about-the-program)
* [Requirements](#requirements)
* [Setup](#setup)
* [Usage Examples](#usage-examples)
* [Reference](#reference)

## About The Program

**API Key**: 
The program will prompt the user to insert an API key, which will be validated before proceeding, to enable access of the features. Users are required to have valid API key, which they can aquire for free from "free.currencyconverterapi.com".

**List**: 
Users can view a list of the available currencies in detail when they input the command "list" when prompted. Each currency has its own ID, name and symbol shown as "USD - United States Dollar - $". If the currency symbol is not available, it will be returned as blank like this "TRY - Turkish New Lira - ".

**Exchange Rates**:
By inputting the command "rate" when prompted, the program  will then ask the user to insert the IDs of the currencies which they would wish to get the exchange rate from and to. The latest rates are automatically fetched, by the API, before the user makes the conversion hence variations may occur depending on time of input.

**Convertions**:
When the command "convert" is inputted when prompted, the program  will ask the user to insert the ID of the currency from which they want to convert from, amount to be converted and the ID of currency to which they want to convert to. The program will then convert the amount from one currency to the other displaying the results.

**Testing**:
If the user wishes to test the program, they could go to the 'test_project.py' file and insert thier API key where required and update the currency IDs to their preferred choice. After that they could run the program by using 'pytest test_project.py' to see if the program runs succesfully.

## Requirements
- API key - free.currencyconverterapi.com
- Install requests 
- Install pytest

## Setup
To run this project write the following in terminal:

```
$ cd projectP
$ python project.py
$ pytest test_project.py
```

## Usage Examples
- To list the available currencies:
```
$ python project.py
Enter your API key from freecurrencyconverter.com: YOUR_API_KEY
Enter a command (q to quit): list
```

- To get the exchange rates:
```
$ python project.py
Enter your API key from freecurrencyconverter.com: YOUR_API_KEY
Enter a command (q to quit): rate
``` 

- To get currency conversion:
```
$ python project.py
Enter your API key from freecurrencyconverter.com: YOUR_API_KEY
Enter a command (q to quit): convert
```

## Reference
* Requests Documentation
* Currency Converter API Documentation# Currency-Converter
