def project_growth(initial_revenue, growth_rate):
    projections = []

    revenue = initial_revenue

    for year in range(1, 11):
        revenue *= (1 + growth_rate)
        projections.append((year, revenue))

    return projections


def main():
    initial_revenue = float(input("Enter initial revenue: $"))
    growth_rate = float(input("Enter annual growth rate (%): ")) / 100

    projections = project_growth(initial_revenue, growth_rate)

    print("\n--- 10-Year Revenue Projection ---")
    print("Year | Revenue")
    print("------------------------")

    for year, revenue in projections:
        print(f"{year:>4} | ${revenue:,.2f}")


if __name__ == "__main__":
    main()
