from requests import get
from pprint import PrettyPrinter

# Base URL for currency converter
Base_URL = "https://free.currconv.com/"

# Get nicely formatted output for JSON
printer = PrettyPrinter()

def main():
    print("Welcome to the currency converter")
    print()

    # Ensure API key from freecurrencyconverter.com
    user_api = input("Enter your API key from freecurrencyconverter.com: ").strip()
    if not user_api:
        print("API key is Missing.")
        return

    if not validate_api_key(user_api):
        print("Invalid API key.")
        return

    # User Commands
    print()
    print("List - Lists the different currencies available")
    print("Rate - Get currencies from freecurrencyconverter.com")
    print("Convert - Convert amount from one currency to another")
    print()

    while True:
        command = input("Enter a command (q to quit): ").casefold()

        if command == "q":
            break
        elif command == "list":
            print()
            show_currencies(get_currencies(user_api))
            print()
        elif command == "rate":
            print()
            curr1 = input("Enter currency to convert from: ").upper()
            curr2 = input("Enter currency to convert to: ").upper()
            exchange_rate(user_api, curr1, curr2)
            print()
        elif command == "convert":
            print()
            curr1 = input("Enter currency to convert from: ").upper()
            amount = input(f"Enter amount in {curr1}: ")
            curr2 = input("Enter currency to convert to: ").upper()
            convert(user_api, curr1, curr2, amount)
            print()
        else:
            print("Unkown Command.")


def validate_api_key(api_key):
    """ Validation of API Key using '/api/v7/convert' endpoint """

    currency = f"api/v7/convert?q=USD_PHP&compact=ultra&apiKey={api_key}"
    url = Base_URL + currency
    response = get(url)

    if response.status_code == 200:
        data = response.json()
        if 'USD_PHP' in data:
            return True

    return False


def get_currencies(user_api):
    """ Get currencies from freecurrencyconverter.com """

    try:
        # Endpoint to access list of currencies
        currency = f"api/v7/currencies?apiKey={user_api}"
        url = Base_URL + currency

        # Ensure data is a list to allow sorting
        data = get(url).json()['results']
        data = list(data.items())
        data.sort()
        return data

    except Exception as e:
        print("Error while fetching data:", e)


def show_currencies(currencies):
    """ Dislpay currencies in a 'id - name - symbol' format """

    for name, currency in currencies:
        name = currency["currencyName"]
        _id = currency["id"]
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")


def exchange_rate(user_api, curr1, curr2):
    """ Get exchange rate between two currencies """

    # Endpoint to access the ids of the  two currencies
    endpoint = f"api/v7/convert?q={curr1}_{curr2}&compact=ultra&apiKey={user_api}"
    url = Base_URL + endpoint
    data = get(url).json()

    # Invalid pairing
    if len(data) == 0:
        return("Invalid Currencies.")

    # Convert value into a list, return the exchange rate
    rate = list(data.values())[0]
    print()
    print(f"{curr1} to {curr2} = {rate}")
    return rate


def convert(user_api, curr1, curr2, amount):
    """ Converting given amount from curr1 to curr2 """

    rate = exchange_rate(user_api, curr1, curr2)
    # Invalid Currencies
    if rate is None:
        return

    try:
        # Ensure amount is a float
        amount = float(amount)
    except:
        return("Invalid Amount.")

    # Convert the amount
    convertedAmount = rate * amount
    print()
    print(f"{amount} {curr1} is equal to {convertedAmount} {curr2}")
    return convertedAmount


if __name__ == "__main__":
    main()