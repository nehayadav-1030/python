total = sum(arr)
left_sum=0
for i in range(len(arr)):
    total-: arr[i]
    if left_sum==total:
        return i+1
    left_sum+=arr[i]:
return -1 