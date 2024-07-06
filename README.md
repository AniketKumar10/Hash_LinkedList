# Hash Table with Headers to Linked List
This repository contains a Python implementation of a hash table with headers to respective indexed to Linked List Nodes. The HashTableHeaders class allows you to store headers associated with specific keys using a hash table. To overcome the hashcollision we use Single Linked List concept.

## Features
- ▶️Efficient hash table implementation.
- ▶️Handles collisions using linked lists.
- ▶️Supports adding headers and verifying keys.

## Usage
1. Clone the Repository:
To get started, clone this repository to your local machine:

```
git clone https://github.com/AniketKumar10/Hash_LinkedList.git
```
---

2. Create an Instance of HashTableHeaders:
In your Python code, create an instance of the HashTableHeaders class with a specified hash table size (e.g., 10):
Python
```
from hash_table_headers import HashTableHeaders

obj = HashTableHeaders(10)  # Specify the hash table size
```
---

3. Add Headers:
Use the add_header method to add headers for specific keys:
```
obj.add_header("Jhon")
obj.add_header("Jacob")
obj.add_header("Charles")
obj.add_header("Hamilton")
obj.add_header("Max")
obj.add_header("Lando")
obj.add_header("Carlos")
```
---

4. Verify Keys:
- Check if a key exists in the hash table using the verify_key method:
```
key_to_verify = "Max"
exists = obj.verify_key(key_to_verify)
print(f"Does '{key_to_verify}' exist in the hash table? {exists}")
```
- If the key is not int the _hash_table_ then returns *FALSE*
- The Word _Oscar_ is not in the table with the following above implementations
- The Keys in the table are case sensitive due to generate_hash's implementation over ASCII values
    
```
key_to_verify = "Oscar"
exists = obj.verify_key(key_to_verify)
print(f"Does '{key_to_verify}' exist in the hash table? {exists}")
```
## Contributing
Contributions are welcome! If you find any issues or want to enhance the implementation, feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
