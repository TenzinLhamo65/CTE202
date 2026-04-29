def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def median_of_three(a, low, high):
        mid = (low + high) // 2

        if a[low] > a[mid]:
            a[low], a[mid] = a[mid], a[low]
        if a[low] > a[high]:
            a[low], a[high] = a[high], a[low]
        if a[mid] > a[high]:
            a[mid], a[high] = a[high], a[mid]

        return mid

    def partition(a, low, high):
        nonlocal comparisons, swaps

        pivot_index = median_of_three(a, low, high)
        pivot = a[pivot_index]

        a[pivot_index], a[high] = a[high], a[pivot_index]
        swaps += 1

        i = low - 1

        for j in range(low, high):
            comparisons += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swaps += 1

        a[i + 1], a[high] = a[high], a[i + 1]
        swaps += 1

        return i + 1

    def quick_sort_recursive(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            quick_sort_recursive(a, low, pi - 1)
            quick_sort_recursive(a, pi + 1, high)

    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr, comparisons, swaps


data = [38, 27, 43, 3, 9, 82, 10]

print("Original List:", data)

sorted_list, comparisons, swaps = quick_sort(data.copy())

print("Sorted using Quick Sort:", sorted_list)
print("Number of comparisons:", comparisons)
print("Number of swaps:", swaps)