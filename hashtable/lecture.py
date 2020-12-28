def my_hash(inputStr):
    sb = inputStr.encode()
    total = 0
    for b in sb:
        total += b
    return total

print(my_hash("foo"))

my_table = [None] * 8

#create
hash_index = my_hash("foo") % len(my_table)
my_table[hash_index] = "bar"
print(my_table)

#read
another_hash_index = my_hash("foo") % len(my_table)
print(my_table[another_hash_index])

#update
yet_ANOTHER_hash_index = my_hash("foo") % len(my_table)
my_table[yet_ANOTHER_hash_index] = "foobar"
print(my_table[yet_ANOTHER_hash_index])

#delete
yet_another_hash_index = my_hash("foo") % len(my_table)
my_table[yet_another_hash_index] = None
print(my_table[yet_another_hash_index])




class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr != None:
            currStr += f'{str(curr.value)} ->'
            curr = curr.next
        return currStr

    def find(self, value):
        #return node w/value
        #runtime: O(n) where n = number of nodes
        curr = self.head
        while curr != None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    def delete(self, value):
        #deletes node w/given value
        #runtime: O(n) where n = number of nodes
        curr = self.head

        #if head needs to be deleted
        if curr.value == value:
            self.head = curr.next
            curr.next = None
            return curr

        prev = None

        while curr != None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next

        return None

    def insert(self, node):
        #insert node at head of list
        #runtime: O(1)
        node.next = self.head
        self.head = node

    def insert_at_head_or_overwrite(self, node):
        #overwrite node or insert node at head
        #runtime: O(n) where n = number of nodes
        existingNode = self.find(node.value)
        if existingNode != None:
            existingNode.value = node.value
        else:
            self.insert(node)