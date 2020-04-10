class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

def union(llist_1, llist_2):
    # Your Solution Here
    set_1 = set()
    llist1_head = llist_1.head
    while llist1_head:
        set_1.add(llist1_head.value)
        llist1_head = llist1_head.next
    
    llist2_head = llist_2.head
    while llist2_head:
        set_1.add(llist2_head.value)
        llist2_head = llist2_head.next
        
    union_list = LinkedList()
    for n in set_1:
        union_list.append(n)
    return union_list
        
def intersection(llist_1, llist_2):
    # Your Solution Here
    set_2 = set()
    llist1_head = llist_1.head
    llist2_head = llist_2.head

    while llist1_head:
        while llist2_head:
            if llist1_head.value == llist2_head.value:
                set_2.add(llist1_head.value)
            llist2_head = llist2_head.next
        llist1_head = llist1_head.next
        llist2_head = llist_2.head

    intersection_list = LinkedList()
    for n in set_2:
        intersection_list.append(n)

    return intersection_list


##### Test Cases #####
    
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2))
# would print '32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->'
print(intersection(linked_list_1,linked_list_2))
# would print '4 -> 21 -> 6 ->' 


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4))
# would print '65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->'
print(intersection(linked_list_3,linked_list_4))
# won't print anything as there are no intersection values

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [8,1,None,6]
element_2 = [1,4,9,5,7]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5,linked_list_6))
# would print '1 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None ->'
print(intersection(linked_list_5,linked_list_6))
# would print '1 ->'