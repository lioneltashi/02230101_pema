# LAB 9: Selection Sort + Indexed Search

# 🔹 Task 1 & 2: Selection Sort with count
def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    print("Original List:", arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

        print(f"After Pass {i+1}: {arr}")

    print("\nFinal Sorted List:", arr)
    print("Total Comparisons:", comparisons)
    print("Total Swaps:", swaps)

    return arr


# 🔹 Task 3: Create Index Table
def create_index_table(arr, block_size):
    index_table = []

    print("\nCreating Index Table...")

    for i in range(0, len(arr), block_size):
        index_table.append((arr[i], i))
        print(f"Index Entry -> Value: {arr[i]}, Position: {i}")

    return index_table


# 🔹 Task 4 & 5: Indexed Search
def indexed_search(arr, index_table, key):
    print(f"\nSearching for: {key}")

    start = 0
    end = len(arr) - 1

    for i in range(len(index_table)):
        if key < index_table[i][0]:
            end = index_table[i][1] - 1
            break
        start = index_table[i][1]

    print(f"Search Range: index {start} to {end}")

    # Step 2: linear search in range
    for i in range(start, end + 1):
        print(f"Checking index {i} -> {arr[i]}")
        if arr[i] == key:
            print(f"Found {key} at index {i}")
            return i

    print(f"{key} not found in list")
    return -1

# Input list
arr = [29, 10, 14, 37, 13]

# Sorting
sorted_arr = selection_sort(arr)

# Create index table
block_size = 3
index_table = create_index_table(sorted_arr, block_size)

# Search (found case)
indexed_search(sorted_arr, index_table, 14)

# Search (not found case)
indexed_search(sorted_arr, index_table, 50)