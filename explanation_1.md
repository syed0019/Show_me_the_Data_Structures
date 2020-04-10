#### Problem 1: LRU Cache

Keeping in view the requirement of the question to pop item using FIFO approach, I tried using OrderedDict() from collections module. It preserves the order in which the key(s) are entered and therefore helpful in popping item using FIFO method/approach if parameter set to False. Moreover, it helps in retrieving values really quick. Both get and set operations are constant time, and therefore our Big O Notation for time complexity is O(1). Space complexity consists of a node list and a cache dictionary, so our Big O there is O(2n) simplified to O(n).

Time Complexity: O(1)
Space Complexity: O(n)