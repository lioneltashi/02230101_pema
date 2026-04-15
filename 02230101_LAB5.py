# -------------------------------
# Part 1: Sequential Search
# -------------------------------
def sequential_search(arr, target):
    comparisons = 0
    
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    
    return -1, comparisons


# -------------------------------
# Part 2: Binary Search (Iterative)
# -------------------------------
def binary_search_iterative(arr, target):
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


# -------------------------------
# Part 2: Binary Search (Recursive)
# -------------------------------
def binary_search_recursive(arr, target, low, high, comparisons=0):
    if low > high:
        return -1, comparisons

    mid = (low + high) // 2
    comparisons += 1

    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, comparisons)


if __name__ == "__main__":
    
    data = [55, 13, 45, 67, 20, 90, 80]
    target = 67

    print("Original List:", data)
    print("Searching for:", target)

    # Sequential Search
    index, comp = sequential_search(data, target)
    print("\nSequential Search:")
    if index != -1:
        print("Found at index:", index)
    else:
        print("Not found")
    print("Number of comparisons:", comp)

    # Binary Search (needs sorted list)
    sorted_data = sorted(data)
    print("\nSorted List:", sorted_data)

    # Iterative Binary Search
    index, comp = binary_search_iterative(sorted_data, target)
    print("\nBinary Search (Iterative):")
    if index != -1:
        print("Found at index:", index)
    else:
        print("Not found")
    print("Number of comparisons:", comp)

    # Recursive Binary Search
    index, comp = binary_search_recursive(sorted_data, target, 0, len(sorted_data)-1)
    print("\nBinary Search (Recursive):")
    if index != -1:
        print("Found at index:", index)
    else:
        print("Not found")
    print("Number of comparisons:", comp)