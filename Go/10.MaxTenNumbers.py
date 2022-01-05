def maxTen(arr):
    arr = sorted(arr,reversed = True)
    res = arr[:10]
    return res

valueArray = list(map(int,input().split()))
print(maxTen(valueArray))
