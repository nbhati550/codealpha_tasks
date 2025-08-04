stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 300
}

portfolio = {}
total_value = 0

n = int(input("How many stocks do you want to add? "))

for _ in range(n):
    name = input("Enter stock name (e.g., AAPL): ").upper()
    quantity = int(input(f"Enter quantity of {name}: "))
    if name in stock_prices:
        investment = quantity * stock_prices[name]
        portfolio[name] = investment
        total_value += investment
    else:
        print(f"{name} not found in price list.")

print("\n--- Investment Summary ---")
for stock, value in portfolio.items():
    print(f"{stock}: ${value}")
print(f"Total Investment: ${total_value}")