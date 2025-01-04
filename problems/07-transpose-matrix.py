# The matrix is currently in the structure of `columns`. The function should
# return the matrix in the structure of `rows`.

# Bonus 1: This can be solved in a single line of code.

# Bonus 2: Try changing the matrix from rows back into

# Write your function here.
def matrix_rows(columns):
    return [list(row) for row in zip(*columns)]

print(matrix_rows([[8, 2], [6, 3], [3, 7], [1, 2]]))  #> [[8, 6, 3, 1], [2, 3, 7, 2]]
print(matrix_rows([[1, 4], [3, 2], [1, 0], [9, 7]]))  #> [[1, 3, 1, 9], [4, 2, 0, 7]]
print(matrix_rows([[5, 6], [2, 8], [5, 2], [1, 0]]))  #> [[5, 2, 5, 1], [6, 8, 2, 0]]

# column = {
#   [8, 2],
#   [6, 3],
#   [3, 7],
#   [1, 2]
# }

# row = {
#   [8, 6, 3, 1],
#   [2, 3, 7, 2]
# }

def matrix_columns(rows):
    return [list(column) for column in zip(*rows)]

print(matrix_columns([[8, 6, 3, 1],[2, 3, 7, 2]] ))