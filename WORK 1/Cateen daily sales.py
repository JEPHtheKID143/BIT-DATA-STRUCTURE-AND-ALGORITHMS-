# canteen_integers.py
sales = [120, 95, 130, 110, 75, 140, 100]   # example integer daily sales for a week

total = sum(sales)
count = len(sales)
average = total / count if count else 0
minimum = min(sales) if sales else None
maximum = max(sales) if sales else None

# Print results in a neat format
print("Canteen Daily Sales (integers):", sales)
print("Total sales:", total)
print("Number of days:", count)
print("Average daily sales:", average)
print("Minimum daily sales:", minimum)
print("Maximum daily sales:", maximum)
# canteen_strings.py
sales = [120, 95, 130, 110, 75, 140, 100]

total = sum(sales)
average = total / len(sales)

report_header = "CANTEEN DAILY SALES REPORT"
divider = "-" * len(report_header)

# Two f-strings summarizing totals and averages
summary_total = f"Total sales for the period: {total} units"
summary_average = f"Average daily sales: {average:.2f} units/day"

# Compose a formatted multi-line report
report = f"""
{report_header}
{divider}

Days: {len(sales)}
Sales data: {sales}

{summary_total}
{summary_average}

Status: {'Good' if average >= 100 else 'Needs Improvement'}
"""

print(report.strip())
# canteen_booleans.py
sales = [120, 95, 130, 110, 75, 140, 100]   # sample sales

total = sum(sales)                           # compute total
average = total / len(sales)                 # compute average

threshold = 100                              # performance threshold

# boolean sub-conditions
avg_above_threshold = average > threshold   # True if average exceeds threshold
has_peak = max(sales) > threshold * 1.2     # True if there's a strong single-day peak
min_ok = min(sales) >= threshold * 0.5      # True if minimum isn't extremely low

# compound condition (use OR and AND)
# Decide "Above Standard" if average is above threshold OR (average near threshold AND strong peak),
# but ensure minimum isn't catastrophically low.
status_condition = (avg_above_threshold or (average >= threshold * 0.95 and has_peak)) and min_ok

# Output with reasoning
if status_condition:
    print("Above Standard")
else:
    print("Below Standard")

print(f"Details -> average: {average:.2f}, avg_above_threshold: {avg_above_threshold}, has_peak: {has_peak}, min_ok: {min_ok}")
# canteen_lists.py
sales = [120, 95, 130, 110, 75, 140, 100]   # original sales list

print("Original list (before):", sales)      # show before

# 1) Add a new day's sales
new_day_sale = 85
sales.append(new_day_sale)                   # append new element
print("After append:", sales)

# 2) Remove the first sales value below a condition (e.g., < 80)
# find index of first element < 80, if any
to_remove_index = None
for i, v in enumerate(sales):
    if v < 80:
        to_remove_index = i
        break

if to_remove_index is not None:
    removed = sales.pop(to_remove_index)    # remove by index
    print(f"Removed first value below 80: {removed}")
else:
    print("No value below 80 found to remove.")

# 3) Sort the list and show before/after sorted
# (if needed keep a copy of the current order)
before_sort = sales.copy()
sales.sort()                                 # in-place sort
print("Before sort:", before_sort)
print("After sort:", sales)
