function reverseArrayRecursive(arr, start = 0, end = arr.length - 1) {
    if (start >= end) return arr; // Base case: stop when pointers meet or cross

    // Swap elements
    [arr[start], arr[end]] = [arr[end], arr[start]];

    // Recursive call with updated indices
    return reverseArrayRecursive(arr, start + 1, end - 1);
}

let arr = [1, 2, 3, 4, 5];
console.log(reverseArrayRecursive(arr)); // Output: [5, 4, 3, 2, 1]
