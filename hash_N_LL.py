class HashTableHeaders:
    def __init__(self,size_of_hash_table) -> None:
        self.size_of_hash_table = size_of_hash_table
        self.hash_table_array = [None for _ in range(self.size_of_hash_table)]

    def generate_hash(self,key):
        h=0
        for char in key:
            h += ord(char)
        return h % self.size_of_hash_table
    
    def add_header(self,key):

        # when we enter the value of 'value', it is passed to 'node_value'
        node = Node(key) 
        h = self.generate_hash(key)

        # a pointer node that traverses through the linked-list(s)
        pointer_node_traversel = Node(None)  

        if self.hash_table_array[h] == None:
            self.hash_table_array[h] = node
        else:
            pointer_node_traversel = self.hash_table_array[h]

        while ( pointer_node_traversel.next_node_ptr == None ) :
            if pointer_node_traversel.next_node_ptr == None:
                pointer_node_traversel.next_node_ptr = node
            else:
                pointer_node_traversel = pointer_node_traversel.next_node_ptr            

    def get_header(self,key):
        h = self.generate_hash(key)
        return self.hash_table_array[h]
    
    def verify_key(self,key) -> bool : 
        # this function checks if my key is in the HashMap or not
        # which key you want to check
        # for that we will take in KEY to get its _hash_value_
        h = self.generate_hash(key)
        pointer_node_traversel = self.hash_table_array[h]

        while pointer_node_traversel:
            if pointer_node_traversel.node_value == key:
                return True
            pointer_node_traversel = pointer_node_traversel.next_node_ptr
        return False

class Node:
    def __init__(self,node_value,next_node_ptr = None) -> None:
        self.node_value = node_value
        self.next_node_ptr = next_node_ptr

obj = HashTableHeaders(10)
'''
print(obj.size_of_hash_table) # to check the size of the hash table array
print(obj.hash_table_array) # check if the array is initilized properly 
'''

obj.add_header("Jhon")
obj.add_header("Jacob")
obj.add_header("Charles")
obj.add_header("Hamilton")
obj.add_header("Max")
obj.add_header("Lando")
obj.add_header("Carlos")
obj.add_header("Oscar")

value1 = obj.verify_key("Oscar")
print(value1)

print(obj.size_of_hash_table) # to check the size of the hash table array
print(obj.hash_table_array) 