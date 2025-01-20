import numpy as np

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








def graph_projection(adj_list, epsilon_0, alpha):
    n = len(adj_list)
    a_prime = [ [] for _ in range(n) ]  # Initialize the processed adjacency list
    d_tilde = np.zeros(n)  # Initialize the noisy degree array
    degrees = [0] * len(adj_list)
    for i, neighbors in enumerate(adj_list):
        degrees[i] = len(neighbors)

    for i in range(n):
        # Step 1: Calculate the noisy degree
        d_tilde[i] = alpha + max(degrees[i] + np.random.laplace(0, 1/epsilon_0), 0)

        # Step 2: Adjust the adjacency list based on the noisy degree
        if d_tilde[i] < degrees[i]:
            num_to_remove = degrees[i] - int(d_tilde[i])
            neighbors = list(adj_list[i])
            np.random.shuffle(neighbors)  # Shuffle to randomize which neighbors to remove
            a_prime[i] = neighbors[:-num_to_remove]  # Keep only the top d_tilde[i] neighbors
        else:
            a_prime[i] = adj_list[i]

    return a_prime, d_tilde









def GNAM_Lap(adj_list, epsilon_1):
    n = len(adj_list)
    adj_matrix = np.zeros((n, n), dtype=float)

    # build adjacency matrix
    for i, neighbors in enumerate(adj_list):
        adj_matrix[i, neighbors] = 1

    # add Laplace noise
    upper_tri = np.triu_indices(n, k=1)
    noise = np.random.laplace(loc=0, scale=1/epsilon_1, size=upper_tri[0].size)
    adj_matrix[upper_tri] += noise
    adj_matrix[upper_tri[::-1]] = adj_matrix[upper_tri]

    # set diagonal to zero
    np.fill_diagonal(adj_matrix, 0)

    return adj_matrix



def GNAM_RR(adj_list, epsilon_1):
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

    # Estimate algorithm
    exp_epsilon_1 = np.exp(epsilon_1)
    adj_matrix *= (exp_epsilon_1 + 1)
    adj_matrix -= 1
    adj_matrix /= (exp_epsilon_1 - 1)

    # Setting diagonal to zero
    np.fill_diagonal(adj_matrix, 0)

    return adj_matrix