def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    prim_diag = sum(arr[i][i] for i in range(0,n))
    sec_diag = sum(arr[i][n-i-1] for i in range(0,n))
    return abs(prim_diag-sec_diag)

arr = [[1, 2, 3],
        [4, 5, 6],
        [9, 8, 9 ]]
print(diagonalDifference(arr))