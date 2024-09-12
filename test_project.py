from project import exchange_rate, convert, show_currencies
from io import StringIO
import sys


def main():
    test_exchange_rate()
    test_convert()
    test_show_currencies()

def test_exchange_rate():
    # Insert a valid api key below
    user_api = "YOUR_VALID_API_KEY"
    # Replace the 'USD' and 'KES' to your preferred currency IDs
    rate = exchange_rate(user_api, "USD", "KES")
    # Replace the rate with the confirmed rate of your preferred IDs 
    assert rate == 143.650086


def test_convert():
    # Insert a valid api key below
    user_api = "YOUR_VALID_API_KEY"
    # Replace the 'USD', 'KES' and amount to your preferred choice
    convertedAmount = convert(user_api, "USD", "KES", 100)
    # Replace the amount with the confirmed convertedAmount from your preferred choice above
    assert convertedAmount == 14365.0086


def test_show_currencies():
    # Capture the standard output as StringIO
    captured_output = StringIO()
    # Redirect standard output to the StringIO object
    sys.stdout = captured_output

    # Sample list of currencies to test
    currencies = [
        ("USD", {"id": "USD", "currencyName": "United States Dollar", "currencySymbol": "$"}),
        ("KES", {"id": "KES", "currencyName": "Kenyan Shilling", "currencySymbol": "KSh"})
        # Add more currencies as needed
    ]

    # Call function
    show_currencies(currencies)
    # Reset stdout to its original state
    sys.stdout = sys.__stdout__
    # Expected output base on the sample currencies
    expected_output = """\
USD - United States Dollar - $
KES - Kenyan Shilling - KSh
"""
    assert captured_output.getvalue() == expected_output


if __name__ == "__main__":
    main()