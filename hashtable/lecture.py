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