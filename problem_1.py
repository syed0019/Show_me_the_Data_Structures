import collections

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        # keeping in view the requirement of question to pop item using FIFO approach, OrderedDict() is used here
        self.cache = collections.OrderedDict()                                 
        self.capacity = capacity

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if len(self.cache) < self.capacity:
            self.cache[key] = value
            
        elif self.capacity == 0:
            print('Cache has zero capacity! Cannot perform operation')
        
        elif len(self.cache) == self.capacity:
            if key in self.cache:
                self.cache.pop(key)
                self.cache[key] = value
            else:
                self.cache.popitem(last=False)
                self.cache[key] = value    
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

                

##### TESTING CASES ######

our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
# returns 1
print(our_cache.get(2))
# returns 2
print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3)) # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# Edge Cases:

our_cache = LRU_Cache(0)
our_cache.set(1, 2)
# would print message 'Cache has zero capacity! Cannot perform operation'
print(our_cache.get(1))
# would return -1

our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(2, 8)
print(our_cache.get(1))
# would return 1
print(our_cache.get(2))
# would return 8

our_cache.set(None, 13)
our_cache.set(9, "key is above cache capacity")
print(our_cache.get(9))
# would return 'key is above cache capacity'
print(our_cache.get(None))
# would return 13