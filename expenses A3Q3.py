def main ():
    expenses = {
        "Travel":[500,200],
        "Meals":[40,60,30],
        "Supplies": [100]
  }
    grand_total = 0
    print("\n--- Expense Summary ---")

    for category, amounts in expenses.items():
        category_total = sum(amounts)
        grand_total += category_total
        print(f" {category}: ${category_total: .2f}")
        print("-----------------------------")
    print(f"Grand Total: ${grand_total: .2f}")
if __name__ == "__main__":
    main()
    