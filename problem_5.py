import hashlib
import datetime
                              
        
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.previous = None
    
    def append(self, value):
        if self.head is None:
            self.head = Block(datetime.datetime.now(), value, None)
            self.previous = self.head
        else:
            node = self.previous
            self.previous = Block(datetime.datetime.now(), value, node)
            self.previous.previous_hash = node

##### Test Cases #####

first_block = Block(datetime.datetime.now(), 'Financial Transaction A', 0)
second_block = Block(datetime.datetime.now(), 'Financial Transaction B', first_block)
third_block = Block(datetime.datetime.now(), 'Financial Transaction C', second_block)
ll = LinkedList()
ll.append('Cash Made to Receivable A')
ll.append('Cash Received from Payable D')
ll.append('Bank Charges for Standing order')


print(first_block.data)
# Expected output: Financial Transaction A
print(first_block.hash)
# Expected output: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
print(first_block.timestamp)
# Expected output: current time
print(second_block.previous_hash.data)
# Expected output: Financial Transaction A
print(ll.head.data)
# Expected output: Cash Made to Receivable A
print(ll.previous.data)
# Expected output: Bank Charges for Standing order
print(ll.previous.previous_hash.data)
# Expected output: Cash Received from Payable D