import numpy as np
def multMatrx(matrixA, matrixB):
    rows_A = len(matrixA)
    columns_A = len(matrixA[0])
    rows_B = len(matrixB)
    columns_B = len(matrixB[0])
    matrixC = [[0 for x in range(rows_A)] for y in range(columns_B)]

    if columns_A == rows_B:
        for row_A in range(0, rows_A):
            for column_B in range(0, columns_B):
                for row_B in range(0, rows_B):
                    print(matrixA[row_A][row_B]*matrixB[row_B][column_B])
                    matrixC[row_A][column_B] += matrixA[row_A][row_B]*matrixB[row_B][column_B]
    else:
        matrixC = "Dimensions mismatch"
    return matrixC


matrixA = [[1, 2, 3], [4, 5, 6], [1, 2, 3]]
matrixB = [[7, 8], [9, 10], [11, 12]]
print(multMatrx(matrixA, matrixB))
