from random import randint
from collections import Counter


def roll_dice(*dice, num_trials = 1000000):
    counts = Counter()
    for roll in range(num_trials):
        counts[sum(randint(1, sides) for sides in dice)]+=1

    for outcome in range(len(dice), sum(dice)+1):
        print(f"{outcome}\t{counts[outcome]/num_trials*100}%")


roll_dice(4,6,6,5,7)