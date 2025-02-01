import numpy as np
import time
import Init

#read graph
file_path = '/datasets/facebook_combined.txt'
adj_list, n = Init.read_graph_from_file(file_path)

#calculate true number of triangles
true_tri= Init.count_triangles(adj_list)

print(n,true_tri)

#setting data points
epsilon_list = [0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

#setting the ratios of the epsilon, apha, beta
ratio=[0.1,0.8,0.1]
alpha=20
beta=0.01

# Start timing
start_time = time.time()

#prepare list to save MSE and Relative err
ReE_list_Lap=[]
MSE_list_Lap=[]

#main algorithm
for eps in epsilon_list:
    #prepare result list
    list_Lap = []

    #run 20 times for each data point
    rounds=20
    for k in range(rounds):
        #get epsilons
        epsilon_0,epsilon_1,epsilon_2=eps*ratio[0],eps*ratio[1],eps*ratio[2]

        #GraphProjection
        prime_adj_list, tilde_d = Init.graph_projection(adj_list, epsilon_0, alpha)

        #get Noisy Adjacency Matrix
        hat_A_Lap = Init.GNAM_Lap(prime_adj_list, epsilon_1)

        #get Noisy Two step Matrix
        hat_B_Lap = hat_A_Lap@hat_A_Lap

        #get resut
        total_sum = 0
        for node in range(0, n):
            # Record the neighbors of node
            neighbors = adj_list[node]
            d_i=len(neighbors)
            for j in adj_list[node]:
                if j != node:
                    total_sum += hat_B_Lap[j,node]
        guss_tri_Lap = total_sum / 6

        print("TriMTR_Lap:", guss_tri_Lap)

        list_Lap.append(guss_tri_Lap)

    #calculate MSE and ReE
    vector = np.full(rounds, true_tri)
    MSE_Lap = np.mean((list_Lap - vector) ** 2)
    ReE_Lap = np.mean(abs(list_Lap - vector)) / true_tri

    #show results
    print('\n')
    print('epsilon=',eps,':')
    print("TriMTR_Lap:",[float(x) for x in list_Lap] ,', MSE:', MSE_Lap, '     MRE:', ReE_Lap)
    print('\n')

    #save results
    ReE_list_Lap.append(ReE_Lap)
    MSE_list_Lap.append(MSE_Lap)

#Final results
print(epsilon_list)
print("TriMTR_Lap:")
print("Relative Err:",[float(x) for x in ReE_list_Lap])
print("Mean Square Err:",[float(x) for x in MSE_list_Lap])

# End timing
end_time = time.time()
print("Total running time:", end_time - start_time, "seconds")