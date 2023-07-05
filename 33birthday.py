# 33birthday.py

import sys

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

print(sys.argv)

'''sys.argv.remove('33birthday.py')
print(sys.argv)

sys.argv = list(map(float, sys.argv))
print(sys.argv)

for i in range(0, len(sys.argv)):
	sys.argv[i] = float(sys.argv[i])

fac365 = 1
for i in range(1, 365 +1):{want for i in range(1, sys.argv[0] +1):}
	fac365 *= i

fac23 = 1
for i in range(1, 342 +1):
	fac23 *= i

vnr = fac365 / fac23
print(vnr)

vt = sys.argv[0] ** sys.argv[1]
print(vt)

pa = vnr / vt
print(pa)

pb = 1 - pa
print(pb)'''

"""
python3 33birthday.py 365 23
0.571
"""