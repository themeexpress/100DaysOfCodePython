"""
Dictonary of common words and their definitions.

"""
dictionary = {
    "Python": "A high-level programming language known for its readability and versatility.",
    "Dictionary": "A collection of key-value pairs in Python, used to store data values like a map.",
    "Function": "A block of reusable code that performs a specific task.",
    "Variable": "A reserved memory location to store values.",
    "Loop": "A control structure that repeats a block of code as long as a specified condition is true.",
    "List": "An ordered collection of items that can be changed and allows duplicate values.",
    "Tuple": "An ordered collection of items that is immutable, meaning it cannot be changed after creation.",
    "Set": "An unordered collection of unique items, which does not allow duplicate values.",
    "String": "A sequence of characters enclosed in quotes, used to represent text.",
    "Integer": "A whole number without a fractional part, used for counting and indexing.",
    "Float": "A number that has a decimal point, used for representing real numbers.",
    "Boolean": "A data type that can hold one of two values: True or False.",
    "Module": "A file containing Python code that can be imported and used in other Python",
    }

print("Welcome to the Python Dictionary!")
print(dictionary.get("Python", "Definition not found."))
print(dictionary.keys())  
print(dictionary.values())

print(dictionary.items())  # Prints both keys and values as tuples

dictionary.update({"API": "A set of rules and protocols for building and interacting with software applications."})
print("Updated Dictionary:", dictionary)
print(dictionary)
dictionary.pop("API", "Key not found.")  # Removes the key 'API' if it exists
print("After popping 'API':", dictionary)
print("Is 'Function' in dictionary?", "Function" in dictionary)  # Checks if 'Function' is a key in the dictionary
print("Length of dictionary:", len(dictionary))

# loop through the dictionary
for key, value in dictionary.items():
    print(f"{key}: {value}")

