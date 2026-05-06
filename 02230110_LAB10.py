def counting_sort(arr):
    if len(arr) == 0:
        return []

    # Find maximum value to define range
    max_val = max(arr)

    # Create count array
    count = [0] * (max_val + 1)

    # Store frequency of each element
    for num in arr:
        count[num] += 1

    # Build sorted array
    sorted_arr = []
    for i in range(len(count)):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1

    return sorted_arr


# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
print("Counting Sort Output:", counting_sort(arr))

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0–9

    # Count occurrences of digits
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Convert count to actual position
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (stable sorting)
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy output
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr


# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Radix Sort Output:", radix_sort(arr))