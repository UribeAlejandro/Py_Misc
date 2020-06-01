def plusMinus(arr):
    n_p = 0
    n_n = 0
    n_z = 0
    for i in arr:
        if i >0:
            n_p += 1
        elif i<0:
            n_n += 1
        else:
            n_z += 1
    n_p/=len(arr)
    n_n/=len(arr)
    n_z/=len(arr)
    print(n_p)
    print(n_n)
    print(n_z)

arr =[9, 0, -9 ]
print(plusMinus(arr))