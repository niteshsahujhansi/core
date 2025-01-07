

rows, cols = (3, 3)
arr = [[0]*cols]*rows
# print(arr)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] += 1
    print(arr[j])

print(arr)