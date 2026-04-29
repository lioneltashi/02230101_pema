#  QUICK SORT 
def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def partition(low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(arr) - 1)
    return arr, comparisons, swaps


#  MERGE SORT 
def merge_sort(arr):
    comparisons = 0
    accesses = 0

    def merge(left, right):
        nonlocal comparisons, accesses
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            accesses += 2  # accessing elements

        # remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        return merge(left, right)

    sorted_arr = merge_sort_recursive(arr)
    return sorted_arr, comparisons, accesses


# MAIN PROGRAM 
if __name__ == "__main__":
    data = [45, 12, 78, 34, 23, 89, 1]

    print("Original List:", data)

    # Quick Sort
    qs_sorted, qs_comp, qs_swaps = quick_sort(data.copy())
    print("\n Quick Sort ")
    print("Sorted List:", qs_sorted)
    print("Comparisons:", qs_comp)
    print("Swaps:", qs_swaps)

    # Merge Sort
    ms_sorted, ms_comp, ms_access = merge_sort(data.copy())
    print("\n Merge Sort ")
    print("Sorted List:", ms_sorted)
    print("Comparisons:", ms_comp)
    print("Array Accesses:", ms_access)