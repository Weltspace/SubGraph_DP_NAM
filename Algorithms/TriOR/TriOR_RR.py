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

        #get resut
        guss_tri_RR = np.trace(np.linalg.matrix_power(hat_A_RR, 3)) / 6

        print("TriOR_RR:", guss_tri_RR)

        list_RR.append(guss_tri_RR)

    #calculate MSE and ReE
    vector = np.full(rounds, true_tri)
    MSE_RR = np.mean((list_RR - vector) ** 2)
    ReE_RR = np.mean(abs(list_RR - vector))/true_tri

    #show results
    print('\n')
    print('epsilon=',eps,':')
    print("TriOR_RR:",[float(x) for x in list_RR] ,', MSE:', MSE_RR, '     MRE:', ReE_RR)
    print('\n')

    #save results
    ReE_list_RR.append(ReE_RR)
    MSE_list_RR.append(MSE_RR)

#Final results
print(epsilon_list)
print("TriOR_RR:")
print("Relative Err:",[float(x) for x in ReE_list_RR])
print("Mean Square Err:",[float(x) for x in MSE_list_RR])

# End timing
end_time = time.time()
print("Total running time:", end_time - start_time, "seconds")