# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'

for i in dna:
	if i == 'A': print('T', end='')
	elif i == 'G': print('C', end='')
	elif i == 'C': print('G', end='')
	else: print('A', end='')

print()

for i in range(len(dna)):
	if dna[i] == 'A': print('T', end='')
	elif dna[i] == 'G': print('C', end='')
	elif dna[i] == 'C': print('G', end='')
	else: print('A', end='')

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
