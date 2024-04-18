def maxWater(arr):
    n = len(arr)
    sum = 0
    # For every element of the array
    for i in range(1, n - 1):
        # Find the maximum element on its left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
        # Find the maximum element on its right
        right = arr[i]
        for j in range(i + 1, n):
            right = max (right, arr[j])
        # Update the maximum water
        sum = sum + (min (left, right) - arr[i])
    return sum
    

print(maxWater([0,1,0,2,1,0,1,3,2,1,2,1]))
print(maxWater([1,1,1,1,1,1,1,1,1,1,1,1]))
print(maxWater([10,1,1,1,1,1,1,1,1,1,1,10]))