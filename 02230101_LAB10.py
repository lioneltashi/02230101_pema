# Part 1: Counting Sort

def counting_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Count frequency
    for num in arr:
        count[num] += 1

    # Construct sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

# Part 2: Radix Sort

def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of digits
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    return output


def radix_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        arr = counting_sort_radix(arr, exp)
        exp *= 10

    return arr

# Main Execution (Testing)

if __name__ == "__main__":

    # Example for Counting Sort
    arr1 = [9, 4, 1, 7, 4, 3, 2]
    print("Original Array (Counting Sort):", arr1)
    print("Sorted Array (Counting Sort):", counting_sort(arr1))

    print()

    # Example for Radix Sort
    arr2 = [329, 457, 657, 839, 436, 720, 355]
    print("Original Array (Radix Sort):", arr2)
    print("Sorted Array (Radix Sort):", radix_sort(arr2))
