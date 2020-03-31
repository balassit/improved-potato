def delete_dups(arr):
    cur = 1
    for i in range(1, len(arr)):
        if arr[cur - 1] != arr[i]:
            arr[cur] = arr[i]
            cur += 1
    print(arr[:cur])
    return cur


arr = [2, 3, 5, 7, 11, 11, 11, 13]
print(delete_dups(arr))
