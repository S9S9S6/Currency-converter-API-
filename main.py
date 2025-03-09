import requests  
API_KEY = "f6f710f6f1d65c0ce24f3ba2"  
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest"

def convert_currency(amount, from_currency, to_currency):
    url = BASE_URL + "/" + from_currency  
    response = requests.get(url)

    if response.status_code == 200:  
        data = response.json()

        exchange_rate = data["conversion_rates"].get(to_currency)

        if exchange_rate:
            return amount * exchange_rate
        else:
            return None  
    else:
        print("Error: API request failed with status code", response.status_code)
        return None  

# User Input
amount = float(input("Enter amount: "))
from_currency = input("Enter source currency (e.g., USD, EUR, GBP): ").upper()
to_currency = input("Enter target currency (e.g., USD, EUR, GBP): ").upper()

# Convert
converted_amount = convert_currency(amount, from_currency, to_currency)

# Show Result
if converted_amount is not None:
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
else:
    print("Error: Unable to fetch exchange rate. Check currency codes or try again.")






