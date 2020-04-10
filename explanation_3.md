#### Problem 3: Huffman Coding

In this problem, I counted the occurences of alphabets/characters in the string to pile up a binary tree considering the Huffman approach. I have also used python sorted function to sort the dictionary values (counts) in ascending order.

Collectively, this approach takes Time Complexity of O(n log n) due to iterating through dictionary and string and the use of built-in sorted function. However, in respects to the space complexity, it is related to the length of alphabets in the string provided, hence resulting in O(k).

Time Complexity: O(n log n)
Space Complexity: O(k)