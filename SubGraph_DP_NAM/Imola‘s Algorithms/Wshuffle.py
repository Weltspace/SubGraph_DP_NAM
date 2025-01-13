# -*- coding: utf-8 -*-
import random
from scipy.optimize import fsolve
import numpy as np
import time


def create_adjacency_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = np.zeros((n, n), dtype=np.float64)

    # build adjacency matrix
    for i, neighbors in enumerate(adj_list):
        adj_matrix[i, neighbors] = 1

    return adj_matrix



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

def generate_pairs(n):
    numbers = list(range(n))
    random.shuffle(numbers)
    pairs = []
    for i in range(0, n - 1, 2):
        pairs.append((numbers[i], numbers[i + 1]))
    return pairs

def calculate_epsilon_L(n, epsilon, delta):
    def equation(epsilon_L):
        part = (np.exp(epsilon_L) - 1) / (np.exp(epsilon_L) + 1)
        term = (np.sqrt((64 * epsilon_L * np.log(4 / delta)) / n) + (8 * np.exp(epsilon_L)) / n)
        return np.log(1 + part * term) - epsilon
    epsilon_L_initial_guess = 1
    epsilon_L_solution = fsolve(equation, epsilon_L_initial_guess)
    return epsilon_L_solution[0]

def RR(bit, eps):
    probability = 1 / (1 + np.exp(eps))
    if random.random() < probability:
        return 1 - bit
    else:
        return bit

def Wshuffle(A, n, eps, delt):
    pairs = generate_pairs(n)
    pa = n / 2
    y = [[0 for _ in range(n)] for _ in range(n)]
    epsL = calculate_epsilon_L(n - 2, eps, delt)

    for node in range(n):
        neighbors = adjacency_list[node]
        for a, b in pairs:
            if a != node and b != node:
                if a in neighbors and b in neighbors:
                    y[a][b] += RR(1, epsL)
                else:
                    y[a][b] += RR(0, epsL)

    f = [[0 for _ in range(n)] for _ in range(n)]
    total = 0

    for s, t in pairs:
        z_i = RR(A[s, t], eps)
        z_j = RR(A[t, s], eps)
        q_L = 1 / (1 + np.exp(epsL))
        q = 1 / (1 + np.exp(eps))
        f[s][t] = (z_i + z_j - 2 * q) * (y[s][t] - (n - 2) * q_L) / (2 * (1 - 2 * q) * (1 - 2 * q_L))
        total += f[s][t]

    ans = n * (n - 1) / (6 * pa) * total
    return ans






file_path = 'D:/PYCHARM/PyCharm Community Edition 2023.3.1/文件/SubGraph_DP_NAM/datasets/facebook_combined.txt'
adjacency_list,n = read_graph_from_file(file_path)
epsilon_list = [0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]





MSE1 = []
MRE1 = []
true_tri = count_triangles(adjacency_list)
print("True Triangle：", true_tri)







A = create_adjacency_matrix(adjacency_list)

start_time = time.time()

for eps in epsilon_list:
    print("epsilon:", eps, ":")
    list1 = []
    list2 = []
    for k in range(10):
        delt = 1 / (100 * n)
        guss_tri = Wshuffle(A, n, eps, delt)
        print("Wshuffle:", guss_tri)
        list1.append(abs(guss_tri - true_tri))
        list2.append((guss_tri - true_tri) ** 2)
    se = sum(list2) / len(list2)
    re = sum(list1) / len(list1) / true_tri
    MSE1.append(se)
    MRE1.append(re)
    print("Wshuffle:", 'MSE:', se, '     MRE:', re)
    print('\n')

print(epsilon_list)
print("Relative Err:", [float(x) for x in MRE1])
print("Mean Square Err:", [float(x) for x in MSE1])

end_time = time.time()
print("Total Running Time：", end_time - start_time, "Seconds")
