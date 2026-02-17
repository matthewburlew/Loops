def calculate_commissions(sales):
    commissions = {}

    for employee, amount in sales.items():
        commissions[employee] = amount * 0.10

    return commissions


def print_leaderboard(commissions):
    print("\n--- Commission Leaderboard ---")

    sorted_commissions = sorted(
        commissions.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for name, commission in sorted_commissions:
        print(f"{name}: ${commission: .2f}")


def main():
    sales = {
        "Alice": 5000,
        "Bob": 7000,
        "Carol": 3000
    }

    commissions = calculate_commissions(sales)
    print_leaderboard(commissions)


if __name__ == "__main__":
    main()
