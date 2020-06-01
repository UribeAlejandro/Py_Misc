def matrixElementsSum(matrix):
    haunted = set()
    cost = 0
    print(matrix)
    if len(matrix) > 1:
        print("")
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    haunted.add((i, j))
        for rooms in haunted:
            i = rooms[0] + 1
            j = rooms[1]
            if i < len(matrix):
                matrix[i][j] = 0
                k=i+1
                if k < len(matrix):
                    for k in range(k, len(matrix)):
                        matrix[k][j] = 0
        print(matrix)
        for i in range(0, len(matrix)):
             cost += sum(matrix[i])
        return cost
    else:
        return sum(matrix[0])


matrix=[[4,0,0,0],
 [8,4,0,1],
 [5,0,0,4],
 [0,0,1,2]]

matrixElementsSum(matrix)