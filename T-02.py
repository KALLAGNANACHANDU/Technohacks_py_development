import requests

def get_exchange_rates(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200 or data['result'] != 'success':
        raise Exception("Error fetching exchange rates")
    return data['conversion_rates']

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Invalid currency code")
    from_rate = exchange_rates[from_currency]
    to_rate = exchange_rates[to_currency]
    return amount * (to_rate / from_rate)

def main():
    api_key = 'fff93193c3c6fe954be7cdb5'
    
    try:
        # Fetch the latest exchange rates
        exchange_rates = get_exchange_rates(api_key)
        print("Exchange rates successfully fetched.")
        
        # User input
        amount = float(input("Enter amount: "))
        from_currency = input("Enter from currency (e.g., USD): ").upper()
        to_currency = input("Enter to currency (e.g., EUR): ").upper()
        
        # Convert currency
        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
