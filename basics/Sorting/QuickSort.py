def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  # Choosing the first element as pivot
    left = [x for x in arr[1:] if x <= pivot]  # Elements smaller than or equal to pivot
    right = [x for x in arr[1:] if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Sorted array:", quick_sort(arr))
