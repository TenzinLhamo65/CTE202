def merge_sort(arr):
    comparisons = 0
    array_accesses = 0

    # Internal recursive function
    def merge_sort_recursive(arr):
        nonlocal comparisons, array_accesses

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        nonlocal comparisons, array_accesses

        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            array_accesses += 2 

            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

            array_accesses += 1  

        # Remaining elements
        while i < len(left):
            merged.append(left[i])
            i += 1
            array_accesses += 2

        while j < len(right):
            merged.append(right[j])
            j += 1
            array_accesses += 2

        return merged

    sorted_arr = merge_sort_recursive(arr)
    return sorted_arr, comparisons, array_accesses


# Example test
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]

    print("Original List:", data)

    sorted_list, comparisons, accesses = merge_sort(data)

    print("Sorted using Merge Sort:", sorted_list)
    print("Number of comparisons:", comparisons)
    print("Number of array accesses:", accesses)