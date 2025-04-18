import math
import numpy as np
import time
from scipy.stats import norm
import Init

# read graph
file_path = 'C:/Users/Dell/Desktop/Subgraph-DP-2025.4.9/Datasets/CA-AstroPh.txt'
adj_list, n = Init.read_graph_from_file(file_path)

# calculate true number of triangles
true_2_star = 0
for i in range(n):
    d_i = len(adj_list[i])
    true_2_star += d_i * (d_i - 1)

print(n, true_2_star)

# setting data points
epsilon_list = [0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

# setting the ratios of the epsilon, apha, beta
ratio = [0.1, 0.8, 0.1]
alpha = 30
beta = 0.01

# Start timing
start_time = time.time()

# prepare list to save MSE and Relative err
ReE_list_RR = []
MSE_list_RR = []

# main algorithm
for eps in epsilon_list:
    # prepare result list
    list_RR = []

    # run 20 times for each data point
    rounds = 20
    for k in range(rounds):

        # GraphProjection
        prime_adj_list, tilde_d = Init.graph_projection(adj_list, eps, alpha)

        guss_2_star = 0

        for i in range(n):
            guss_2_star += (tilde_d[i] - alpha) * (tilde_d[i] - alpha - 1) - 2 / (eps ** 2)

        print("2STAR:", guss_2_star)

        list_RR.append(guss_2_star)

    # calculate MSE and ReE
    vector = np.full(rounds, true_2_star)
    MSE_RR = np.mean((list_RR - vector) ** 2)
    ReE_RR = np.mean(abs(list_RR - vector)) / true_2_star

    # show results
    print('\n')
    print('epsilon=', eps, ':')
    print("2STAR:", [float(x) for x in list_RR], ', MSE:', MSE_RR, '     MRE:', ReE_RR)
    print('\n')

    # save results
    ReE_list_RR.append(ReE_RR)
    MSE_list_RR.append(MSE_RR)

# Final results
print(epsilon_list)
print("2STAR:")
print("Relative Err:", [float(x) for x in ReE_list_RR])
print("Mean Square Err:", [float(x) for x in MSE_list_RR])

# End timing
end_time = time.time()
print("Total running time:", end_time - start_time, "seconds")