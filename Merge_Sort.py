def merge_sort(array, low, high):
    if low >= high:
        return  # Base case: If one or no elements, it's already sorted.

    mid = low + (high - low) // 2  
    merge_sort(array, low, mid)  # Sort left half
    merge_sort(array, mid + 1, high)  # Sort right half
    merge(array, low, mid, high)  # Merge sorted halves

def merge(array, low, mid, high):
    left_part = array[low:mid + 1]  # Left half
    right_part = array[mid + 1:high + 1]  # Right half

    i = j = 0  # Pointers for left and right halves
    index = low  # Start position in original list

    # Merge left and right halves
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            array[index] = left_part[i]
            i += 1
        else:
            array[index] = right_part[j]
            j += 1
        index += 1  # Move to the next position

    # Add remaining elements (if any)
    while i < len(left_part):
        array[index] = left_part[i]
        i += 1
        index += 1

    while j < len(right_part):
        array[index] = right_part[j]
        j += 1
        index += 1

# Example usage
array = [5, 2, 9, 1, 6, 3]
merge_sort(array, 0, len(array) - 1)
print("Sorted List:", array)
