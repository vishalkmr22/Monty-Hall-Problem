# Monty Hall Simulation

This Python script simulates the famous Monty Hall problem and visualizes the results using a surface plot. The Monty Hall problem is a probability puzzle inspired by the American television game show "Let's Make a Deal" and is named after its original host, Monty Hall.

## Dependencies
- NumPy
- Matplotlib

## Usage
1. Install the required dependencies if you haven't already:
2. Run the script.
3. Enter the number of doors and the number of doors containing cars when prompted.
4. The script will output the winning probability with switching and with sticking.
5. A surface plot will be displayed showing how the ratio of winning probabilities varies with different values of the total number of doors and the number of doors containing cars.

## Script Overview
- The script defines a function `monty_hall_simulation` to simulate the Monty Hall problem for a given number of doors, doors with cars, and number of trials.
- It prompts the user to input the number of doors and the number of doors containing cars.
- Simulation trials are run to calculate the winning probabilities with switching and sticking strategies.
- A surface plot is generated to visualize how the ratio of winning probabilities varies with different combinations of total doors and doors with cars.