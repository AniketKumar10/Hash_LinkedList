def generate_hash(key):
        h=0
        for char in key:
            h += ord(char)
        return h % 10
value = input("Enter a value to generate a Key : ")
val = generate_hash(value)
print(val)