import numpy as np
import time
import Init

#read graph
file_path = 'D:/PYCHARM/PyCharm Community Edition 2023.3.1/文件/SubGraph_DP_NAM/datasets/facebook_combined.txt'
adj_list, n = Init.read_graph_from_file(file_path)

#calculate true number of quadrangles
true_qua= Init.count_quadrangles(adj_list)

print(n,true_qua)

#setting data points
epsilon_list = [0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

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
        #get Noisy Adjacency Matrix
        hat_A_RR = Init.GNAM_RR(adj_list, eps)

        # get Noisy Two step Matrix
        hat_B_RR = hat_A_RR @ hat_A_RR

        np.fill_diagonal(hat_B_RR, 0)

        #get resut
        total_sum = 0
        for node in range(0, n):
            # Record the neighbors of node
            neighbors = adj_list[node]
            d_i=len(neighbors)
            for i in range(d_i):
                for j in range(d_i):
                    total_sum += hat_B_RR[neighbors[i], neighbors[j]]-1
        guss_qua_RR = total_sum / 8

        print("QuaTR_RR:", guss_qua_RR)

        list_RR.append(guss_qua_RR)

    #calculate MSE and ReE
    vector = np.full(rounds, true_qua)
    MSE_RR = np.mean((list_RR - vector) ** 2)
    ReE_RR = np.mean(abs(list_RR - vector)) / true_qua

    #show results
    print('\n')
    print('epsilon=',eps,':')
    print("QuaTR_RR:",[float(x) for x in list_RR] ,', MSE:', MSE_RR, '     MRE:', ReE_RR)
    print('\n')

    #save results
    ReE_list_RR.append(ReE_RR)
    MSE_list_RR.append(MSE_RR)

#Final results
print(epsilon_list)
print("QuaTR_RR:")
print("Relative Err:",[float(x) for x in ReE_list_RR])
print("Mean Square Err:",[float(x) for x in MSE_list_RR])

# End timing
end_time = time.time()
print("Total running time:", end_time - start_time, "seconds")