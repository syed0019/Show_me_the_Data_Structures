#### Problem 2: File Recursion

In this problem, I used the recursion approach to call function in order to find file in each directory if it's not available in the current path. Morever, I used slicing to extract '.' extension files in the current path and printed their names with path. The time complexity, for this approach is O(n) as we need to call function recursively to find file(s). Consequently, the space complexity with each recursion may grow exponentially.

Time Complexity: O(n)
Space Complexity: O(n log n)
