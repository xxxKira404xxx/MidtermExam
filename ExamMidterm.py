ExpenseCategories = [
    ["Food & Drinks"],
    ["Transportation"],
    ["Mobile / Internet"],
    ["School Supplies"],
    ["Entertainment"], 
]

StudentName = input("Student Name: ")
if StudentName == "":
    StudentName = "Unknown Student"
    print("No name entered. Setting name to: Unknown Student")

# Ask for Weekly Budget with basic validation
WeeklyBudget = int(input("Weekly Budget: "))
if WeeklyBudget <= 0:
    print("Invalid budget! Setting budget to P1 as a default to avoid errors.")
    WeeklyBudget = 1
else:
    print("Budget set to P" + str(WeeklyBudget))

print("=====================================")
print("     WEEKLY EXPENSE - CATEGORIES     ")
print("=====================================")
print("1. " + ExpenseCategories[0][0] + "         [e.g. Lunch, snacks, coffee]")
print("2. " + ExpenseCategories[1][0] + "        [e.g. Bus, jeepney, ride-share]")
print("3. " + ExpenseCategories[2][0] + "     [e.g. Load, data plan, WiFi top-up]")
print("4. " + ExpenseCategories[3][0] + "       [e.g. Notebook, pen, bond paper]")
print("5. " + ExpenseCategories[4][0] + "         [e.g. Games, movies, hangout]")
print("=====================================")

logged_descriptions = []
logged_amounts = []
logged_categories = []
logged_alerts = []

total_spent = 0
threshold = WeeklyBudget * 0.25

for i in range(1, 5):
    print("\n--- EXPENSE " + str(i) + " ---")
    CategoryNumber = int(input("Category (0 to skip): "))
    
    # ERROR HANDLING: Check if the number is within 0-5
    if CategoryNumber < 0 or CategoryNumber > 5:
        print("Invalid Category! Please choose 1-5 or 0 to skip.")
        # We don't append anything, so this slot is effectively skipped/wasted
    elif CategoryNumber == 0:
        print("Expense skipped.")
        continue
    else:
        # If the code reaches here, CategoryNumber is definitely 1, 2, 3, 4, or 5
        description = input("Description: ")
        amount = int(input("Amount: "))
        
        alert = ""
        if amount > threshold:
            alert = "! High Expense Alert!"
        
        logged_categories.append(ExpenseCategories[CategoryNumber - 1][0])
        logged_descriptions.append(description)
        logged_amounts.append(amount)
        logged_alerts.append(alert)
        
        total_spent = total_spent + amount

remaining = WeeklyBudget - total_spent
if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

print("\n======================================================")
print("     " + StudentName.upper() + " -- WEEKLY EXPENSE LOG")
print("======================================================")
print("  Weekly Budget  : P" + str(WeeklyBudget))

for i in range(len(logged_amounts)):
    print("  [" + str(i+1) + "] " + logged_categories[i])
    print("      " + logged_descriptions[i] + "      P" + str(logged_amounts[i]) + " " + logged_alerts[i])

print("------------------------------------------------------")
print("  Total Spent    : P" + str(total_spent))
print("  Remaining      : P" + str(remaining))
print("  Status         : " + status)
print("======================================================")
