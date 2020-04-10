#### Problem 5: Blockchain

In this problem, it was clearly mentioned that the blocked contain the reference of previous block(s) so I created the previous node using Linked List to refer to the previous block's details and each point stores its and previous hash. The time complexity for this approach is O(1) because linked list has constant time complexity for append method. As for the space complexity it is O(n) which is space consumption in our blocks and number of nodes in linked lists.

Time Complexity: O(1)
Space Complexity: O(n)