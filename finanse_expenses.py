print("CANNY CONTROLS - EXPENSE CALCULATOR")

categories = {
    "1": "Raw Material",
    "2": "Salary",
    "3": "Electricity",
    "4": "Maintenance",
    "5": "Transport",
    "6": "Other"
}

expenses = []


def get_amount(message):
    while True:
        try:
            amount = float(input(message))

            if 0 <= amount < float("inf"):
                return round(amount, 2)

            print("Enter a valid positive amount or zero.")
        except ValueError:
            print("Enter numbers only, for example: 15000")


budget = get_amount("Enter budget for this period (Rs): ")

while True:
    print("\nEXPENSE CATEGORIES")

    for number, category in categories.items():
        print(number, "-", category)

    choice = input("Choose category (1-6): ").strip()

    if choice not in categories:
        print("Invalid category. Please try again.")
        continue

    description = input("Enter expense description: ")
    amount = get_amount("Enter expense amount (Rs): ")

    expenses.append({
        "category": categories[choice],
        "description": description,
        "amount": amount
    })

    more = input("Add another expense? (yes/no): ").strip().lower()

    if more != "yes":
        break

print("\nEXPENSE REPORT")
print("-" * 55)

for expense in expenses:
    print(
        f"{expense['category']} | "
        f"{expense['description']} | "
        f"Rs {expense['amount']:,.2f}"
    )

print("\nCATEGORY TOTALS")

for category in categories.values():
    category_total = sum(
        expense["amount"]
        for expense in expenses
        if expense["category"] == category
    )

    print(f"{category}: Rs {category_total:,.2f}")

total = round(sum(expense["amount"] for expense in expenses), 2)
balance = round(budget - total, 2)

print("\nBudget: Rs", f"{budget:,.2f}")
print("Total expenses: Rs", f"{total:,.2f}")

if balance >= 0:
    print("Remaining budget: Rs", f"{balance:,.2f}")
else:
    print("Over budget by: Rs", f"{abs(balance):,.2f}")