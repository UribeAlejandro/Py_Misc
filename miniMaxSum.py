def miniMaxSum(arr):
    arr_sorted = sorted(arr)
    print(sum(arr_sorted[:4]), sum(arr_sorted[-4:]))


arr = [769082435, 210437958, 673982045, 375809214, 380564127]
miniMaxSum(arr)