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


        while(pointer_node_traversel.next_node_ptr == None):
            if pointer_node_traversel.next_node_ptr == None:
                pointer_node_traversel.next_node_ptr = node
            else:
                pointer_node_traversel = pointer_node_traversel.next_node_ptr
            

        # self.hash_table_array[h] = node

    def get_header(self,key):
        h = self.generate_hash(key)
        return self.hash_table_array[h]
    
    def verify_key(self,key):
        h = self.generate_hash(key)


class Node:
    def __init__(self,node_value,next_node_ptr = None) -> None:
        self.node_value = node_value
        self.next_node_ptr = next_node_ptr

class LinkedList:
    def __init__(self) -> None:
        pass


obj = HashTableHeaders(10)

print(obj.size_of_hash_table) # to check the size of the hash table array
print(obj.hash_table_array) # check if the array is initilized properly 

#obj.add_header("Niraj")
#obj.add_header("Kumar")
obj.add_header("Aniket")
obj.add_header("Rhea")
#obj.add_header("Adhish")

print((obj.get_header("Rhea")).node_value) # this prints aniket but not the next currosponding 
# values of the object like "Rhea"

print(obj.size_of_hash_table) # to check the size of the hash table array
print(obj.hash_table_array) 