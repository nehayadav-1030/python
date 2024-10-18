for i in range(len(arr)):
    if sum(arr[:i])==sum(arr[i+1:]):
return i+1
return -1