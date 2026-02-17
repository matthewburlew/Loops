def main():
    customers = {
        "Alice": 800,
        "Bob": 3200,
        "Carol": 7500,
        "David": 1200,
        "Emma": 5400
    }

    tiers = { "Bronze": 0, "Silver": 0, "Gold":0}

    for name, total in customers.items():
        if total < 1000:
            tiers["Bronze"] += 1
        elif total < 5000:
            tiers["Silver"] += 1
        else:
            tiers["Gold"] += 1

    print("\n--- Customer Loyalty Tiers ---")
    for tier, count in tiers.items():
        print(f"{tier}: {count} customers")

if __name__ == "__main__":
    main() 