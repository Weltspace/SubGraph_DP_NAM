import math
import numpy as np
import time
from scipy.stats import norm
import Init

#read graph
file_path = '/datasets/facebook_combined.txt'
adj_list, n = Init.read_graph_from_file(file_path)

#calculate true number of quadrangles
true_qua= Init.count_quadrangles(adj_list)

print(n,true_qua)

#setting data points
epsilon_list = [0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

#setting the ratios of the epsilon, apha, beta
ratio=[0.1,0.8,0.1]
alpha=20
beta=0.01

# Start timing
start_time = time.time()

#prepare list to save MSE and Relative err
ReE_list_RR=[]
MSE_list_RR=[]

#main algorithm
for eps in epsilon_list:
    #prepare result list
    list_RR = []

    #run 20 times for each data point
    rounds=20
    for k in range(rounds):
        # get epsilons
        epsilon_0, epsilon_1, epsilon_2 = eps * ratio[0], eps * ratio[1], eps * ratio[2]
        sigma=math.sqrt(2)/epsilon_1

        # GraphProjection
        prime_adj_list, tilde_d = Init.graph_projection(adj_list, epsilon_0, alpha)
        tilde_d_max = max(tilde_d)

        # get Noisy Adjacency Matrix
        hat_A_Lap = Init.GNAM_Lap(prime_adj_list, epsilon_1)

        # get Noisy Two step Matrix
        hat_B_Lap = hat_A_Lap @ hat_A_Lap

        np.fill_diagonal(hat_B_Lap, 0)

        #get resut
        total_sum = 0
        for node in range(0, n):
            # set the Delt_f
            Delt_f = norm.ppf(1 - beta) * np.sqrt( tilde_d[node] * ((n - 2) * sigma ** 4 + 2 * tilde_d_max* sigma ** 2 ))  + (tilde_d_max-1)*tilde_d[node]

            # Record the neighbors of node
            neighbors = adj_list[node]
            d_i = len(neighbors)
            sumu = 0
            for i in range(d_i):
                small_sum = 0
                for j in range(i):
                    small_sum += hat_B_Lap[neighbors[i], neighbors[j]]
                sumu += min(max(small_sum, -Delt_f), Delt_f)

            total_sum += 2 * (sumu + np.random.laplace(loc=0, scale=Delt_f / epsilon_2))

        guss_qua_Lap = total_sum / 8

        print("QuaTR_Lap :", guss_qua_Lap)

        list_RR.append(guss_qua_Lap)

    #calculate MSE and ReE
    vector = np.full(rounds, true_qua)
    MSE_RR = np.mean((list_RR - vector) ** 2)
    ReE_RR = np.mean(abs(list_RR - vector)) / true_qua

    #show results
    print('\n')
    print('epsilon=',eps,':')
    print("QuaTR_Lap :",[float(x) for x in list_RR] ,', MSE:', MSE_RR, '     MRE:', ReE_RR)
    print('\n')

    #save results
    ReE_list_RR.append(ReE_RR)
    MSE_list_RR.append(MSE_RR)

#Final results
print(epsilon_list)
print("QuaTR_Lap :")
print("Relative Err:",[float(x) for x in ReE_list_RR])
print("Mean Square Err:",[float(x) for x in MSE_list_RR])

# End timing
end_time = time.time()
print("Total running time:", end_time - start_time, "seconds")