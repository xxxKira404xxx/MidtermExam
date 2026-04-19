# FINAL Midterm Exam Solution - BSIT 1A Software Engineering
# Using f-strings but NO .2f formatting.

# 1. SETUP AND INPUT WITH ERROR HANDLING
while True:
    name_input = input("Student name: ")
    if name_input.strip() != "":
        student_name = name_input.strip().title()
        break
    print("Error: Student name cannot be empty.")

while True:
    budget_raw = input("Weekly budget: ")
    if budget_raw.replace(".", "", 1).isdigit():
        weekly_budget = float(budget_raw)
        if weekly_budget > 0:
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

print("\n" + "=" * 42)
print("   WEEKLY EXPENSE -- CATEGORIES")
print("=" * 42)

for i in range(len(categories)):
    print(f" {i + 1}. {categories[i]}")

print("=" * 42 + "\n")

expenses_list = []
total_spent = 0.0

# 2. EXPENSE ENTRY LOOP
for i in range(1, 5):
    print(f"--- EXPENSE {i} ---")
    
    while True:
        cat_in = input("Category (1-5, or 0 to skip): ")
        if cat_in.isdigit():
            cat_choice = int(cat_in)
            if 0 <= cat_choice <= 5:
                break
            else:
                print("Error: Selection must be between 0 and 5.")
        else:
            print("Error: Enter a valid numeric category.")
            
    if cat_choice == 0:
        print(f"Expense slot {i} skipped.\n")
        continue

    while True:
        desc_in = input("Description: ")
        if desc_in.strip() != "":
            description = desc_in.strip()
            break
        print("Error: Description is required.")

    while True:
        amt_raw = input("Amount: ")
        if amt_raw.replace(".", "", 1).isdigit():
            amount = float(amt_raw)
            if amount >= 0:
                break
            else:
                print("Error: Amount cannot be negative.")
        else:
            print("Error: Enter a valid number for the amount.")

    is_high = amount > (weekly_budget * 0.25)
    category_name = categories[cat_choice - 1]
    expenses_list.append([i, category_name, description, amount, is_high])
    
    total_spent = total_spent + amount
    print("")

# 3. CALCULATIONS AND STATUS
remaining_bal = weekly_budget - total_spent

if remaining_bal >= 0:
    budget_status = "Budget OK! Keep it up."
else:
    budget_status = "Overspent! Reduce spending."

# 4. FINAL REPORT (Using f-strings but NO .2f formatting)
print("=" * 54)
print(f"     {student_name.upper()} -- WEEKLY EXPENSE LOG")
print("=" * 54)
print(f"  Weekly Budget  : P{weekly_budget}")

for item in expenses_list:
    num = item[0]
    cat = item[1]
    desc = item[2]
    amt = item[3]
    is_high = item[4]
    
    alert = ""
    if is_high:
        alert = " ! High Expense Alert!"
        
    print(f"  [{num}] {cat}")
    print(f"      {desc}      P{amt}{alert}")

print("-" * 54)
print(f"  Total Spent    : P{total_spent}")
print(f"  Remaining      : P{remaining_bal}")
print(f"  Status         : {budget_status}")
print("=" * 54)
