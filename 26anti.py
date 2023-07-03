# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'

cdna = ''
rdna = ''


for i in range(len(dna)):
	if dna[i] == 'A': cdna += 'T'
	elif dna[i] == 'G': cdna += 'C'
	elif dna[i] == 'C': cdna += 'G'
	else: cdna += 'A'
print(f'{cdna}')

for i in range(len(dna)):
	i += 1
	rdna += cdna[-i] # -i makes u start from the backmost term -> front
print(f'{rdna}')
	
'''
python3 26anti.py
TTTTTTTTTTTCAGT
'''