# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 320
}

total_investment = 0

print(" Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print(f"Added {stock}: ${investment}")
    else:
        print("Stock not found!")

print("\n Total Investment Value: $", total_investment)

# Optional: Save to file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: ${total_investment}")

print("Portfolio saved to portfolio.txt")
