# dnd1-elementaladept.py

import random

# You are a mage with the Fire Bolt spell. This does 1d10 damage, or 5.5
# points of damage on average. If you have the Elemental Adept feat, damage
# rolls of 1 become 2. How much more damage do you do on average if you are
# an Elemental Adept? Simulate by rolling dice a million times.

fb = 0
trials = 10000
for i in range(trials):
	fb += random.randint(1, 10)
		
ea = 0
for j in range(trials):
	roll = random.randint(1,10)
	if roll == 1: roll = 2
	ea += roll

k = fb / trials
l = ea / trials
m = l - k
print(f'{m:.1f}')

"""
python3 dnd1-elementaladept.py
0.1
"""
