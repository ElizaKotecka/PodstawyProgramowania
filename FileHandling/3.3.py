# Find all dates in the format "month day, year" (e.g., "March 12, 1992")
# [A-Za-z]+ \d{1,2}, \d{4}

# Locate all phone numbers in the format "XXX-XXX-XXXX" (e.g., "555-123-4567")
# \d{3}-\d{3}-\d{3}

# Find all numbers written with commas as thousand separators (e.g., "1,234")
# \d+,\d+

# Identify all fragments containing names starting with a capital letter (e.g., "Alice", "John", "Mike")
# [AJM]\w+[^n][en]

# Find whole numbers in the text (e.g., "30")