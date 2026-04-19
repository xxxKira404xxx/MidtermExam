# Weekly Expense Logger
**BSIT 1A — Software Engineering | Final Midterm Exam Solution**

A beginner-friendly Python console application that helps students track and summarize their weekly expenses across common spending categories.

---

## Features

- Input validation with descriptive error messages for all user entries
- Five predefined expense categories (Food, Transportation, Mobile/Internet, School Supplies, Entertainment)
- Up to 4 expense entries per session, with the option to skip any slot
- Automatic **High Expense Alert** flag when a single expense exceeds 25% of the weekly budget
- Clean formatted report showing itemized expenses, total spent, remaining balance, and budget status
- Uses **f-strings** for output formatting (no `.2f` decimal formatting)

---

## Requirements

- Python 3.6 or higher (f-string support required)
- No external libraries needed — uses only Python built-ins

---

## How to Run

```bash
python MidtermExam.py
```

---

## Usage Walkthrough

**Step 1 — Enter your name and weekly budget**
```
Student name: juan dela cruz
Weekly budget: 1000
```

**Step 2 — View the category menu**
```
==========================================
   WEEKLY EXPENSE -- CATEGORIES
==========================================
 1. Food & Drinks
 2. Transportation
 3. Mobile / Internet
 4. School Supplies
 5. Entertainment
==========================================
```

**Step 3 — Log up to 4 expenses**

For each expense slot, you will be prompted to enter:
- A category number (1–5), or `0` to skip the slot
- A short description
- The amount spent

**Step 4 — View the summary report**

The program prints a formatted report with all logged expenses, total spending, remaining balance, and a budget status message.

---

## Sample Output

```
======================================================
     JUAN DELA CRUZ -- WEEKLY EXPENSE LOG
======================================================
  Weekly Budget  : P1000.0
  [1] Food & Drinks
      Jollibee lunch      P350.0 ! High Expense Alert!
  [2] Transportation
      Jeepney fare        P50.0
  [3] School Supplies
      Notebook and pen    P120.0
------------------------------------------------------
  Total Spent    : P520.0
  Remaining      : P480.0
  Status         : Budget OK! Keep it up.
======================================================
```

---

## Input Validation Rules

| Field | Rule |
|---|---|
| Student Name | Cannot be empty; leading/trailing spaces are stripped |
| Weekly Budget | Must be a valid number greater than zero |
| Category | Must be a digit between 0 and 5 |
| Description | Cannot be empty |
| Amount | Must be a valid number of zero or greater |

---

## High Expense Alert Logic

An expense is flagged with `! High Expense Alert!` if:

```
expense amount > weekly_budget × 0.25
```

For example, with a P1,000 budget, any single expense above P250 triggers the alert.

---

## Budget Status Messages

| Condition | Message |
|---|---|
| `remaining >= 0` | `Budget OK! Keep it up.` |
| `remaining < 0` | `Overspent! Reduce spending.` |

---

## Project Notes

- Output uses **f-strings** throughout; `.2f` float formatting is intentionally excluded per exam requirements.
- Student name is stored in `.title()` case (e.g., `Juan Dela Cruz`) and displayed in `.upper()` in the report header.
- Expenses are stored in a list of lists: `[slot_number, category, description, amount, is_high]`.

---

## Author
Bandong, John Matthew C.
BSIT 1A — Software Engineering Student
Final Midterm Examination
