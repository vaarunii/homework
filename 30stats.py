# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

print(sys.argv)

count = 0
for math in sys.argv[1:]:
	count += 1
	print(float(math))

sum = 0
for i in sys.argv[1:]:
	sum += float(i)

mean = sum / count
sdtop = 0
for a in sys.argv[1:]:
	sdtop += (float(a) - mean) ** 2
sd = (sdtop / count) ** 0.5

sys.argv.sort()
sys.argv.remove('30stats.py')
midind = ((len(sys.argv) -1)/ 2)
print(midind)
median = float(sys.argv[2])
	
print(f'Count: {count}')
print(f'Minimum: {float(min(sys.argv[1:]))}')
print(f'Maximum: {float(max(sys.argv[1:]))}')
print(f'Mean: {mean:.3f}')
print(f'Std. dev: {sd:.3f}')
print(f'Median: {median:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
