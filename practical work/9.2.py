def sort_k(matrix, k):
    k_row = matrix[k - 1]
    
    sorted_index = sorted(range(len(k_row)), key=lambda i: k_row[i])

    sorted_matrix = []
    for row in matrix:
        sorted_row = [row[i] for i in sorted_index]
        sorted_matrix.append(sorted_row)
        
    return sorted_matrix

D = [
    [3, 1, 2],
    [6, 5, 4],
    [9, 7, 8]
]
k = 2 

sorted_D = sort_k(D, k)
print("Матрица с отсортированными столбцами:")
for row in sorted_D:
    print(row)