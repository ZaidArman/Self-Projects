from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

if __name__ == "__main__":
    amount = float(input("Enter amount: "))
    from_currency = input("Enter from currency: ").upper()
    to_currency = input("Enter to currency: ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
