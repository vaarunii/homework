# dnd3-savingthrow.py

import random 

# One of the core mechanics of D&D is the "saving throw". When certain
# events happen, you need to roll a d20 to figure out if you succeed or not.
# For example, you are walking across a frozen lake and it begins to crack
# underfoot. If you make a saving throw, you step aside. If you fail, you
# fall in. Some saving throws are more difficult than others. If the ice
# is very thick, the "difficulty class" (DC) may be only 5. This means you
# only need to roll a 5 or higher to succeed. However, if the ice is thin
# and has a DC of 15, you will need a roll of 15 or higher to succeed.
# Certain events may give you "advantage" or "disadvantage". For example,
# if you have a rope tied around your waist and a friend is instructed to
# pull you aside if anything bad happens, you could have "advantage". This
# allows you to roll two d20s and take the larger value. You may also have
# disadvantage, for example another "friend" pushes you from behind, causing
# you to stumble forward. In this case, you have "disadvantage" and must take
# the lower of two d20 rolls.

# Write a program that simulates saving throws against DCs of 5, 10, and 15.
# What is the probability of success normally or with advantage/disadvantage?
# Make a table showing the results.

#regular d20 roll with diff margins of success
#advantage with two d20s, take bigger value
#disadvantage with two d20s, take smaller value

trials = 10000

for threshold in range(5, 16, 5):
	norm = 0
	adv = 0
	disadv = 0
	for j in range(trials):
		roll = random.randint(1, 20)
		roll2 = random.randint(1, 20)
		if roll >= threshold: norm += 1
		if max(roll, roll2) >= threshold: adv += 1
		if min(roll, roll2) >= threshold: disadv += 1
	print(f'{threshold} {norm / trials:.3f} {adv / trials:.3f} {disadv / trials:.3f}')

"""
python3 dnd3-savingthrow.py
5  0.800 0.960 0.640
10 0.550 0.797 0.302
15 0.300 0.510 0.090
"""
