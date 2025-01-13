import Init

#read graph
file_path = 'D:/PYCHARM\PyCharm Community Edition 2023.3.1/文件/SubGraph_DP_NAM/datasets/facebook_combined.txt'
adj_list, n = Init.read_graph_from_file(file_path)

eps=10000

hat_A_Lap = Init.GNAM_Lap(adj_list, eps)

print(hat_A_Lap[0:5, 0:5])
print('\n\n\n\n\n')

B=hat_A_Lap@hat_A_Lap
print(B[0:5, 0:5])






print('\n\n\n\n\n')

eps=1

hat_A_Lap = Init.GNAM_Lap(adj_list, eps)

print(hat_A_Lap[0:5, 0:5])
print('\n\n\n\n\n')

B=hat_A_Lap@hat_A_Lap
print(B[0:5, 0:5])


