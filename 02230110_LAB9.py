# LAB 9: Indexed Search and Selection Sort

# Task 1 & 2: Selection Sort
def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    print("Original list:", arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap only if needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

        print(f"Pass {i+1}: {arr}")

    print("Sorted list:", arr)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)

    return arr


# Task 3: Create Index Table
def create_index_table(arr, block_size):
    index_table = []

    print("\nIndex table created:")

    for i in range(0, len(arr), block_size):
        index_table.append((arr[i], i))
        print(f"{arr[i]} -> {i}")

    return index_table


# Task 4: Indexed Search

def indexed_search(arr, index_table, key, block_size):
    print(f"\nSearch key: {key}")

    imin = 0
    imax = 0

    # Step 1: Find range using index table
    for i in range(len(index_table)):
        if i == len(index_table) - 1 or key < index_table[i + 1][0]:
            imin = index_table[i][1]
            if i == len(index_table) - 1:
                imax = len(arr) - 1
            else:
                imax = index_table[i + 1][1] - 1
            break

    print("Index range found:")
    print(f"{arr[imin]} <= {key} < {arr[imax] if imax+1 < len(arr) else 'end'}")

    print(f"Searching from index {imin} to index {imax}:")

    # Step 2: Linear search in range
    for i in range(imin, imax + 1):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == key:
            print(f"{key} found at index {i}")
            return i

    print(f"{key} not found")
    return -1

# Main Program (Testing)

if __name__ == "__main__":

    # Task 1 & 2 Test
    arr = [29, 10, 14, 37, 13]
    sorted_arr = selection_sort(arr.copy())

    # Task 3 Test
    arr2 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
    block_size = 3
    index_table = create_index_table(arr2, block_size)

    # Task 4 Test (Key Found)
    indexed_search(arr2, index_table, 45, block_size)

    # Task 5 Test (Key Not Found)
    indexed_search(arr2, index_table, 43, block_size)