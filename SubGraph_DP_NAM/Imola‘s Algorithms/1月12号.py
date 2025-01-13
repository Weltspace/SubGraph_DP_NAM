# -*- coding: utf-8 -*-
import numpy as np
import time


def read_graph_from_file(file_path):
    adjacency_list = []
    max_node = 0
    node_hash = {}
    with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding as UTF-8
        for line in file:
            line = line.strip()
            if line.startswith('#') or line == '':
                continue

            node1, node2 = map(int, line.split())
            if node1 not in node_hash:
                node_hash[node1] = max_node
                if max_node + 1 > len(adjacency_list):
                    adjacency_list.extend([[] for _ in range(max_node + 1 - len(adjacency_list))])
                max_node += 1
            if node2 not in node_hash:
                node_hash[node2] = max_node
                if max_node + 1 > len(adjacency_list):
                    adjacency_list.extend([[] for _ in range(max_node + 1 - len(adjacency_list))])
                max_node += 1

            new_node1 = node_hash[node1]
            new_node2 = node_hash[node2]

            if new_node2 not in adjacency_list[new_node1]:
                adjacency_list[new_node1].append(new_node2)
            if new_node1 not in adjacency_list[new_node2]:
                adjacency_list[new_node2].append(new_node1)

    for i in range(len(adjacency_list)):
        adjacency_list[i] = list(set(adjacency_list[i]))

    for i in range(len(adjacency_list)):
        adjacency_list[i] = sorted(adjacency_list[i])

    return adjacency_list, len(node_hash)







def count_triangles(adjacency_list):
    triangle_count = 0
    for i in range(len(adjacency_list)):
        neighbors = adjacency_list[i]
        for j in range(len(neighbors)):
            for k in range(j + 1, len(neighbors)):
                if neighbors[k] in adjacency_list[neighbors[j]]:
                    triangle_count += 1
    return triangle_count // 3






def RR_clipping(adj_list, epsilon_1):
    n = len(adj_list)
    adj_matrix = np.zeros((n, n), dtype=float)

    # Getting adjacency matrix
    for i in range(n):
        adj_matrix[i, [j for j in adj_list[i]]] = 1

    # Adding noise
    p = 1 / (1 + np.exp(-epsilon_1))
    upper_tri = np.triu_indices(n, k=1)  # Upper triangular indices excluding diagonal
    noise = np.random.rand(upper_tri[0].size) > p
    adj_matrix[upper_tri] = (noise+adj_matrix[upper_tri])%2
    adj_matrix[upper_tri[::-1]]=adj_matrix[upper_tri]

    # Setting diagonal to zero
    np.fill_diagonal(adj_matrix, 0)

    return adj_matrix


def graph_projection(adj_list, epsilon_0, alpha):
    n = len(adj_list)
    a_prime = [ [] for _ in range(n) ]  # Initialize the processed adjacency list
    d_tilde = np.zeros(n)  # Initialize the noisy degree array
    degrees = [0] * len(adj_list)
    for i, neighbors in enumerate(adj_list):
        degrees[i] = len(neighbors)

    for i in range(n):
        # Step 1: Calculate the noisy degree
        d_tilde[i] = max(alpha +  degrees[i] + np.random.laplace(0, 1/epsilon_0), 0)

        # Step 2: Adjust the adjacency list based on the noisy degree
        if d_tilde[i] < degrees[i]:
            num_to_remove = degrees[i] - int(d_tilde[i])
            neighbors = list(adj_list[i])
            np.random.shuffle(neighbors)  # Shuffle to randomize which neighbors to remove
            a_prime[i] = neighbors[:-num_to_remove]  # Keep only the top d_tilde[i] neighbors
        else:
            a_prime[i] = adj_list[i]

    return a_prime, d_tilde








#--------------------------------------------------------------------------

def jacob(matrix, miu, eps1, eps2, tilde_d):
    ans=0
    n = matrix.shape[0]

    for i in range(n):
        d_i=len(adjacency_list[i])

        ti=0
        si=0

        Nei=adjacency_list[i]

        for j in range(d_i):
            if Nei[j]<i:
                tij=0
                for k in range(d_i):
                    if Nei[j] < Nei[k] < i:
                        if(matrix[Nei[j]][Nei[k]]==1):
                            tij=tij+1
                ti+=min(tij,tilde_d[i])

        for j in range(d_i):
            if Nei[j] < i:
                for k in range(d_i):
                    if Nei[j] < Nei[k] < i:
                        si=si+1

        wi=ti-miu*np.exp(-eps1)*si

        hat_wi=wi

        ans+=hat_wi

    for i in range(n):
        ans+=np.random.laplace(loc=0, scale=tilde_d[i]/eps2)

    return 1/(miu*(1-np.exp(-eps1)))*ans







# Usage
file_path = 'D:/PYCHARM/PyCharm Community Edition 2023.3.1/文件/SubGraph_DP_NAM/datasets/CA-AstroPh.txt'
adjacency_list,n = read_graph_from_file(file_path)




epsilon_list=[0.1,0.2,0.4,0.5,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0]
alpha=150
MSE=[]
MRE=[]


true_tri=count_triangles(adjacency_list)
print("True Triangle：",true_tri)


d_max=0
for i in range(n):
    d_max=max(d_max,len(adjacency_list[i]))







start_time = time.time()

for eps in epsilon_list:
    epsilon_0, epsilon_1, epsilon_2 = eps * 0.1, eps * 0.45, eps * 0.45
    print("epsilon:",eps,":")

    list1 = []
    list2 = []
    #上面两个分别用于存每次循环中二轮算法的绝对误差，误差的平方


    for k in range(20):
        eps1 = eps

        miu = np.exp(eps1) / (1 + np.exp(eps1))

        # GraphProjection
        prime_adj_list, tilde_d = graph_projection(adjacency_list, epsilon_0, alpha)

        for l in range(10):
            print(tilde_d[l])

        B = RR_clipping(prime_adj_list,epsilon_1)

        guss_tri = jacob(B, miu, epsilon_1, epsilon_2, tilde_d)
        print(guss_tri)

        list1.append(abs(guss_tri - true_tri))
        list2.append((guss_tri - true_tri)*(guss_tri - true_tri))
        #记录数据到列表中



    se=sum(list2) / len(list2)

    re=sum(list1) / len(list1) / true_tri

    print('MSE:',se,'     MRE:',re)

    MSE.append(se)

    MRE.append(re)
    print('\n')


print(epsilon_list)
print("Relative Err:", [float(x) for x in MRE])
print("Mean Square Err:", [float(x) for x in MSE])
end_time = time.time()
print("Total Running Time：", end_time - start_time, "Seconds")