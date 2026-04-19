# Bandong John Matthew C.
# BSIT SE 1A

# 1. INPUT WITH ERROR HANDLING
while True:
    studentNameInput = input("Student name: ")
    if studentNameInput.replace(" ", "").isalpha():
        studentName = studentNameInput.strip().title()
        break
    print("Please try again! Any special character or numbers are not allowed.")

while True:
    weeklyBudget = input("Weekly budget: ")
    if weeklyBudget.replace(".", "", 1).isdigit():
        setWeeklyBudget = float(weeklyBudget)
        if setWeeklyBudget > 0:
            break
        else:
            print("Error: Budget must be greater than zero.")
    else:
        print("Error: Please enter a valid number for the budget.")

# CATEGORIES LIST
categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

category_examples = [
    "Lunch, snacks, coffee",
    "Bus, jeepney, ride-share",
    "Load, data plan, WiFi top-up",
    "Notebook, pen, bond paper",
    "Games, movies, hangout"
]

print("\n" + "=" * 55)
print("         WEEKLY EXPENSE -- CATEGORIES")
print("=" * 55)
for i in range(len(categories)):
    print(f" {i + 1}. {categories[i]:<20} [e.g. {category_examples[i]}]")
print("=" * 55 + "\n")

expensesList = []
totalSpent = 0.0

# 2. EXPENSE ENTRY LOOP
for i in range(1, 5):
    print(f"--- EXPENSE {i} ---")

    while True:
        selectCategory = input("Category (0 to skip): ")
        if selectCategory.isdigit():
            categoryChoice = int(selectCategory)
            if 0 <= categoryChoice <= 5:
                break
            else:
                print("Error: Selection must be between 0 and 5.")
        else:
            print("Error: Enter a valid numeric category.")

    if categoryChoice == 0:
        print(f"Expense slot {i} skipped.\n")
        continue

    while True:
        descriptionCategory = input("Description: ")
        if descriptionCategory.strip() == "":
            print("Error: Description is required.")
        elif descriptionCategory.strip().replace(" ", "").isdigit():  
            print("Error: Description cannot be numbers only.")        #
        else:
            description = descriptionCategory.strip()
            break

    while True:
        amountInput = input("Amount: ")
        if amountInput.replace(".", "", 1).isdigit():
            setAmount = float(amountInput)
            if setAmount >= 0:
                break
            else:
                print("Error: Amount cannot be negative.")
        else:
            print("Error: Enter a valid number for the amount.")

    is_high = setAmount > (setWeeklyBudget * 0.25)
    category_name = categories[categoryChoice - 1]
    expensesList.append([i, category_name, description, setAmount, is_high])

    totalSpent = totalSpent + setAmount
    print("")

# 3. CALCULATIONS
remainingBalance = setWeeklyBudget - totalSpent
if remainingBalance >= 0:
    budgetStatus = "Budget OK! Keep it up."
else:
    budgetStatus = "Overspent! Reduce spending."

# 4. PRINTING THE EXPENSE LOG
print("=" * 54)
print(f"     {studentName.title()} -- WEEKLY EXPENSE LOG")
print("=" * 54)
print(f"  Weekly Budget  : P{setWeeklyBudget}")

for item in expensesList:
    number = item[0]
    category = item[1]
    description = item[2]
    amount = item[3]
    isHighAmount = item[4]

    alert = ""
    if isHighAmount:
        alert = " ! High Expense Alert!"

    print(f"  [{number}] {category}")
    print(f"      {description}      P{amount}{alert}")

print("-" * 54)
print(f"  Total Spent    : P{totalSpent}")
print(f"  Remaining      : P{remainingBalance}")
print(f"  Status         : {budgetStatus}")
print("=" * 54)
