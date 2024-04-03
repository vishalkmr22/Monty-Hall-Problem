import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def monty_hall_simulation(n, k, num_trials):
    switch_wins = 0
    stick_wins = 0
    
    for _ in range(num_trials):
        doors = ['goat'] * (n - k) + ['car'] * k
        np.random.shuffle(doors)
        
        player_choice = np.random.randint(0, n)
        
        # Find available doors with goats to be opened by the host
        available_doors = [i for i in range(n) if i != player_choice and doors[i] == 'goat']
        
        # Ensure there are available doors with goats
        if available_doors:
            opened_door = np.random.choice(available_doors)
            
            # Switching strategy
            switch_choice = next(i for i in range(n) if i != player_choice and i != opened_door)
            if doors[switch_choice] == 'car':
                switch_wins += 1
                
            # Sticking strategy
            if doors[player_choice] == 'car':
                stick_wins += 1
            
    switch_win_prob = switch_wins / num_trials
    stick_win_prob = stick_wins / num_trials
    
    return switch_win_prob, stick_win_prob


# Define the range of values for n and k
n_values = np.arange(3, 20)
k_values = np.arange(1, 15)

# Number of simulation trials
num_trials = 10000
doors_n = int(input("Enter the number of doors: "))
cars_k = int(input("Enter the number of cars: "))
switch_win_prob, stick_win_prob = monty_hall_simulation(doors_n, cars_k, num_trials)
print(f"Winning probability with switching: {switch_win_prob}")
print(f"Winning probability with sticking: {stick_win_prob}")
# Initialize arrays to store the ratios
ratios = np.zeros((len(n_values), len(k_values)))

# Calculate the ratio for each combination of n and k
for i, n in enumerate(n_values):
    for j, k in enumerate(k_values):
        switch_win_prob, stick_win_prob = monty_hall_simulation(n, k, num_trials)
        if stick_win_prob != 0:
            ratios[i, j] = switch_win_prob / stick_win_prob
        else:
            ratios[i, j] = np.nan  # Set to NaN if stick_win_prob is zero

# Create a meshgrid for n and k
K, N = np.meshgrid(k_values, n_values)  # Switched order of K and N

# Create the surface plot
fig = plt.figure(figsize=(20, 15))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(N, K, ratios, cmap='viridis')

# Set labels and title
ax.set_xlabel('Number of Doors (n)')
ax.set_ylabel('Number of Doors with Cars (k)')
ax.set_zlabel('Ratio: switch_win_prob / stick_win_prob')
ax.set_title('Surface Plot of n, k versus (switch_win_prob/stick_win_prob)')

plt.show()
