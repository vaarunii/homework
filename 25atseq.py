# 25atseq.py

import random

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers
dna = ''

r = random.random()
print(r)

for i in range(30):
	r = random.random()
	if r <= 0.6:
		dna += random.choice ('AT')
	else:
		dna += random.choice('GC')
print(dna)

num = 0

for i in dna:
	if i == 'A' or i == 'T': num += 1

print(f'{num / len(dna):.3f}')

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
