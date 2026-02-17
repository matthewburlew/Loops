def get_prices():
    prices = []

    while True:
        try:
            price = float(input("Enter item price (0 to finish): $"))

            if price == 0:
                break

            if price < 0:
                print("Price cannot be negative.")
                continue

            prices.append(price)

        except ValueError:
            print("Please enter a valid price.")

    return prices


def print_summary(prices):
    total = sum(prices)
    count = len(prices)
    average = total / count if count > 0 else 0

    print("\n--- Checkout Summary ---")
    print(f"Number of items: {count}")
    print(f"Total purchases: ${round(total, 2)}")
    print(f"Average price per item: ${round(average, 2)}")


def main():
    prices = get_prices()
    print_summary(prices)


if __name__ == "__main__":
    main()
