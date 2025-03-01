rows, cols = 3, 3
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter value for element ({i}, {j}): "))
        row.append(value)
    matrix.append(row)

# Printing the matrix
for row in matrix:
    print(row)
