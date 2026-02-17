def main():
    warehouses = [
        {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
        {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
    ]

    total_inventory = {}

    # Loop through each warehouse
    for warehouse in warehouses:
        inventory = warehouse["inventory"]

        # Loop through each product in that warehouse
        for product, quantity in inventory.items():
            total_inventory[product] = total_inventory.get(product, 0) + quantity

    print("\n--- Total Supply Chain Stock ---")
    for product, total in total_inventory.items():
        print(f"{product}: {total}")


if __name__ == "__main__":
    main()
