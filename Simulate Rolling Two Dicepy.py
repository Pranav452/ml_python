# Simulate Rolling Two Dice 10,000 Times and Estimate Probabilities

import random

# Number of simulations
num_trials = 10000

# Counters for each event
count_sum_7 = 0
count_sum_2 = 0
count_sum_gt_10 = 0

for _ in range(num_trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    if total == 7:
        count_sum_7 += 1
    if total == 2:
        count_sum_2 += 1
    if total > 10:
        count_sum_gt_10 += 1

# Calculate probabilities
prob_sum_7 = count_sum_7 / num_trials
prob_sum_2 = count_sum_2 / num_trials
prob_sum_gt_10 = count_sum_gt_10 / num_trials

# Print results
print(f"P(Sum = 7): {prob_sum_7:.4f}")
print(f"P(Sum = 2): {prob_sum_2:.4f}")
print(f"P(Sum > 10): {prob_sum_gt_10:.4f}")
