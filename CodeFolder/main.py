#Comments is reccomended.
#This is your starter code. For coders, copy this code and code at your own risk.

import random
import collections
import matplotlib.pyplot as plt

# User enters number of rolls. Must only be 100, 1000, 10000. 
# No negative numbers, letters, and positive numbers that aren't in the given must be inputted.
while True:
    input_rolls = input("Enter number of rolls (100, 1000, 10000): ")
    
    if input_rolls.isdigit():
        n = int(input_rolls)
        
        if n in [100, 1000, 10000]:
            break
        else:
            print("Please enter a valid number of rolls (100, 1000, or 10000).")
    else:
        print("No negative numbers or letters. Please enter a valid number.")

    
def simulate_dice(n):     # Number of rolls
    rolls = [random.randint(1,6) for _ in range(n)]     # Roll dice based on how many rolls is given
    counts = collections.Counter(rolls)
    faces = list (range(1,7))       # Possible outcome face of the die per roll. 7 is not included.
    exp_prob = [counts[f] / n for f in faces]       # Total number of face divided by total rolls

# For bar charts, experiment vs. theoretical (set to 1/6 = 16.67%)
    plt.figure(figsize=(8,5))
    plt.bar(faces, exp_prob, label=f"Experimental (n={n})", alpha=0.7)
    plt.axhline(1/6, color="red", linestyle="--", label="Theoretical (1/6)")
    plt.xlabel("Die Face")
    plt.ylabel("Probability")
    plt.title(f"Dice Roll Probability (n={n})")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
simulate_dice(n) #Changed to n because the user will input number of rolls.