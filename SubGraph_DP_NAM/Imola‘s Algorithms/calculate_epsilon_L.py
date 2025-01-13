import numpy as np
from scipy.optimize import fsolve

def calculate_epsilon_L(n, epsilon, delta):
    def equation(epsilon_L):
        part = (np.exp(epsilon_L) - 1) / (np.exp(epsilon_L) + 1)
        term = (np.sqrt((64 * epsilon_L * np.log(4 / delta)) / n) + (8 * np.exp(epsilon_L)) / n)
        return np.log(1 + part * term) - epsilon
    epsilon_L_initial_guess = 1
    epsilon_L_solution = fsolve(equation, epsilon_L_initial_guess)
    return epsilon_L_solution[0]

epsilon_list = [0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
n=107614
delta = 1 / (100 * n)

epsilon_L_list=[]

for i in range(12):
    epsilon_L_list.append(calculate_epsilon_L(n, epsilon_list[i], delta))

print([float(x) for x in epsilon_L_list])