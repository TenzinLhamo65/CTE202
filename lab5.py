#implemented by chador
def sequential_search(arr, target):
    comparisons = 0  # Counter for comparisons
    for index, value in enumerate(arr):
        comparisons += 1
        if value == target:
            return index, comparisons  # Target found
    return -1, comparisons  # Target not found

# Example usage
my_list = [23, 45, 12, 67, 89, 34, 56]
target_value = 67

print(f"List: {my_list}")
print(f"Searching for {target_value} using Sequential Search")

index, num_comparisons = sequential_search(my_list, target_value)

if index != -1:
    print(f"Found at index {index}")
else:
    print("Target not found")
print(f"Number of comparisons: {num_comparisons}")