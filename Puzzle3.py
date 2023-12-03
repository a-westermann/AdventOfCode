import file_ops


input_lines = file_ops.read_input(3)
# Compare the indices of numbers & symbols which are 0-1 lines apart
# for multi-digit numbers, include all corresponding indices

# Loop once to collect Numbers and Symbols, then loop through numbers to check symbol indices

# Try to parse each char as an int
# If int, continue parsing following chars as int until hit a None
# Collect those indices
# To find symbols, if parsing as int fails, check if period

for line in input_lines:
