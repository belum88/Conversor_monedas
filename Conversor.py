def get_exchange_rate(currency_from, currency_to):
    # Tasas de cambio predeterminadas (1 unidad de currency_from a currency_to)
    exchange_rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.00},
        'EUR': {'USD': 1.18, 'GBP': 0.88, 'JPY': 129.53},
        'GBP': {'USD': 1.34, 'EUR': 1.14, 'JPY': 147.34},
        'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0068}
    }
    
    if currency_from in exchange_rates and currency_to in exchange_rates[currency_from]:
        return exchange_rates[currency_from][currency_to]
    else:
        return None

def convert_currency(amount, currency_from, currency_to):
    rate = get_exchange_rate(currency_from, currency_to)
    if rate:
        return amount * rate
    else:
        print(f"No se puede convertir de {currency_from} a {currency_to}.")
        return None

def main():
    print("Bienvenido al conversor de monedas")
    amount = float(input("Ingrese la cantidad que desea convertir: "))
    currency_from = input("Ingrese la moneda de origen (USD, EUR, GBP, JPY): ").upper()
    currency_to = input("Ingrese la moneda de destino (USD, EUR, GBP, JPY): ").upper()
    
    result = convert_currency(amount, currency_from, currency_to)
    
    if result is not None:
        print(f"{amount} {currency_from} es igual a {result:.2f} {currency_to}")

if __name__ == "__main__":
    main()
