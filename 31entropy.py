# 31entropy.py
import math
import sys

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()open

# Hint: try breaking your program with erroneous input

print(sys.argv)

inside = []
for i in sys.argv[1:]:
	flo = float(i)
	mat = (flo) * math.log2(flo)
	inside.append(mat)
print(inside)

print(-sum(inside))

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
