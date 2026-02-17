def analyze_survey(data):
    counts = {}

    for item in data:
        counts[item] = counts.get(item, 0) + 1

    return counts


def print_summary(counts, total):
    print("\n--- Market Share Summary ---")

    for product in sorted(counts):
        percentage = (counts[product] / total) * 100
        print(f"{product}: {percentage:.0f}%")


def main():
    survey_data = ["coffee", "tea", "coffee", "soda"]

    counts = analyze_survey(survey_data)
    total = len(survey_data)

    print_summary(counts, total)


if __name__ == "__main__":
    main()
