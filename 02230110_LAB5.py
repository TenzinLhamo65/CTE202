def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# Main program
sorted_list = [12, 23, 34, 45, 56, 67, 89]
target = 67

index, comparisons = binary_search(sorted_list, target)

print("Sorted List:", sorted_list)
print("\nSearching for", target, "using Binary Search\n")

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comparisons)