def main():
    revenue = float(input("Enter starting revenue: "))
    growth_rate = float(input("Enter annual growth rate (%): ")) / 100

    print("\n--- Revenue Projection ---")

    for year in range(1, 6):
        revenue *= (1 + growth_rate)

        # Scale revenue down so bars aren't huge
        bar_length = int(revenue / 10000)
        bar = "#" * bar_length 
        
        print(f"Year {year}: {bar}")

if __name__ == "__main__":
    main()