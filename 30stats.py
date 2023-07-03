# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

print(sys.argv)

count = sys.argv
print(tuple)

count = 0
for math in sys.argv[1:]:
	count += 1
	print(float(math))

print(f'Count: {count}')
print(f'Minimum: {min(sys.argv[1:])}')
print(f'Maximum: {max(sys.argv[1:])}')
print(f'Mean: {float(sum(sys.argv[1:])} / {count}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
