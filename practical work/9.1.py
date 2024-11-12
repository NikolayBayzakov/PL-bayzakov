def sorted_ascending(row):
    return all(row[i] <= row[i + 1] for i in range(len(row) - 1))

def sorted_descending(row):
     return all(row[i] >= row[i + 1] for i in range(len(row) - 1))


def max_sorted_item(matrix):
    max_item = float('-inf')
    for row in matrix:
        if sorted_ascending(row) or sorted_descending(row):
            max_item = max(max_item, max(row))
            
    return max_item if max_item != float('-inf') else None

matrix = [
    [1, 2, 3],
    [5, 4, 3],
    [7, 8, 9],
    [10, 9, 8]
]
result = max_sorted_item(matrix)

print("Максимальный элемент среди упорядоченных строк:", result)