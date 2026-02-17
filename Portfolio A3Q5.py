import random


def calculate_total(portfolio):
    total_value = 0

    for stock, data in portfolio.items():
        stock_value = data["shares"] * data["price"]
        total_value += stock_value

    return total_value


def simulate_week(portfolio):
    print("\n--- Weekly Simulation ---")

    for day in range(1, 6):
        for stock in portfolio:
            change_percent = random.uniform(-0.05, 0.05)
            portfolio[stock]["price"] *= (1 + change_percent)

        total = calculate_total(portfolio)
        print(f"Day {day} total value: ${round(total, 2)}")


def main():
    portfolio = {
        "AAPL": {"shares": 10, "price": 170},
        "TSLA": {"shares": 4, "price": 250},
        "AMZN": {"shares": 2, "price": 130}
    }

    total = calculate_total(portfolio)
    print("--- Current Portfolio Value ---")
    print(f"Total value: ${total: .2f}")

    simulate_week(portfolio)


if __name__ == "__main__":
    main()
