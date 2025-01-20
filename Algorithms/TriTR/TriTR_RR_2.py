import math
import numpy as np
import time
from scipy.stats import norm
import Init

# read graph
file_path = 'D:/PYCHARM/PyCharm Community Edition 2023.3.1/文件/SubGraph_DP_NAM/datasets/facebook_combined.txt'
adj_list, n = Init.read_graph_from_file(file_path)

# calculate true number of triangles
true_tri = Init.count_triangles(adj_list)

print(n, true_tri)

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
        # get epsilons
        epsilon_0, epsilon_1, epsilon_2 = eps * ratio[0], eps * ratio[1], eps * ratio[2]
        sigma = math.sqrt(math.exp(epsilon_1) / ((math.exp(epsilon_1) - 1) ** 2))

        # GraphProjection
        prime_adj_list, tilde_d = Init.graph_projection(adj_list, epsilon_0, alpha)
        tilde_d_max = max(tilde_d)

        # get Noisy Adjacency Matrix
        hat_A_RR = Init.GNAM_RR(prime_adj_list, epsilon_1)

        # get resut
        total_sum = 0
        for node in range(0, n):
            # set the Delt_f
            Delt_f = norm.ppf(1 - beta) * np.sqrt(tilde_d[node] * sigma ** 2) + tilde_d[node]

            # Record the neighbors of node
            neighbors = adj_list[node]
            d_i = len(neighbors)
            sumu = 0
            for i in range(d_i):
                small_sum = 0
                for j in range(i):
                    small_sum += hat_A_RR[neighbors[i], neighbors[j]]
                sumu += min(max(small_sum, -Delt_f), Delt_f)

            total_sum += 2 * (sumu + np.random.laplace(loc=0, scale=Delt_f / epsilon_2))

        guss_tri_RR = total_sum / 6

        print("TriTR_RR:", guss_tri_RR)

        list_RR.append(guss_tri_RR)

    # calculate MSE and ReE
    vector = np.full(rounds, true_tri)
    MSE_RR = np.mean((list_RR - vector) ** 2)
    ReE_RR = np.mean(abs(list_RR - vector)) / true_tri

    # show results
    print('\n')
    print('epsilon=', eps, ':')
    print("TriTR_RR:", [float(x) for x in list_RR], ', MSE:', MSE_RR, '     MRE:', ReE_RR)
    print('\n')

    # save results
    ReE_list_RR.append(ReE_RR)
    MSE_list_RR.append(MSE_RR)

# Final results
print(epsilon_list)
print("TriTR_RR:")
print("Relative Err:", [float(x) for x in ReE_list_RR])
print("Mean Square Err:", [float(x) for x in MSE_list_RR])

# End timing
end_time = time.time()
print("Total running time:", end_time - start_time, "seconds")