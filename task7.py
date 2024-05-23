import numpy as np
import matplotlib.pyplot as plt

num_simulations = 100000

def roll_dice(num_simulations):
    die1 = np.random.randint(1, 7, num_simulations)
    die2 = np.random.randint(1, 7, num_simulations)
    return die1 + die2

sums = roll_dice(num_simulations)

sum_counts = np.bincount(sums)[2:]

probabilities = sum_counts / num_simulations

analytical_probabilities = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) / 36

print("Сума\tМонте-Карло\tАналітична")
for i, (mc_prob, an_prob) in enumerate(zip(probabilities, analytical_probabilities)):
    print(f"{i+2}\t{mc_prob:.5f}\t\t{an_prob:.5f}")

sums_range = np.arange(2, 13)
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(sums_range - width/2, probabilities, width, label='Монте-Карло')
rects2 = ax.bar(sums_range + width/2, analytical_probabilities, width, label='Аналітичні')

ax.set_xlabel('Сума')
ax.set_ylabel('Ймовірність')
ax.set_title('Ймовірності сум при киданні двох кубиків')
ax.set_xticks(sums_range)
ax.legend()
plt.show()