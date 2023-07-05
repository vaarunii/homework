# dnd4-deathsaves.py

import random

# Death saves are a little different than normal saving throws. If your
# health drops to 0 or below, you are unconscious and may die. Each time it
# is your turn, roll a d20 to determine if you get closer to life or fall
# deeper into death. If the number is less than 10, you record a "failure".
# If the number is 10 or greater, you record a "success". If you collect 3
# failures, you "die". If you collect 3 successes, you are "stable" but
# unconscious. If you are unlucky and roll a 1, it counts as 2 failures.
# If you're lucky and roll a 20, you gain 1 health and have "revived".
# Write a program that simulates death saves. What is the probability one
# dies, stabilizes, or revives?

#d20 rolls
#record fails = <10 -> 3 fails = death
#record successes = >10 -> 3 successes = stable
#if 1 = 2 fails
#if 20 = revival!

threshold = 10
trials = 10
rev = 0
stab = 0
die = 0

for i in range(trials):
	#does this character die/stabilize/revive
	s = 0
	f = 0
	for j in range(5):
		roll = random.randint(1, 20)
		if roll == 20: rev += 1
			break
		
		if roll == 1: f += 2
		elif roll >= threshold: s += 1
		elif roll <= threshold: f += 1
		
		if s == 3: stab += 1 
			break
		
		if f >= 3: die +=1 
			break
		

print(f'die: {die / trials:.3f}, stabilize: {stab / trials:.3f}, revive: {rev / trials:.3f}')

"""
python3 dnd4-deathsaves.py
die: 0.405
stabilize: 0.414
revive: 0.181
"""
