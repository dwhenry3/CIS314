# -------------------
# Tuples
# -------------------
print("#------------------------")
print("Tuples")
print("#------------------------")
x = ("a","b","c","d")
print("Full tuple:",x)
print("Tuple first element:",x[0])

y = x + tuple("e")
print("New tuple Y by concatenating tuples:",y)

x += tuple("e") # We actually don't need a new tuple, we force an update to an existing tuple through concatenation
print("Expanded X tuple:",x)

# -------------------
# Sets
# -------------------
print("\n#------------------------")
print("Sets")
print("#------------------------")
x = {"a","b","c","d"}
print("Full Set:",x) # Everytime we run this it will be a different order
#print(x[0]) # This fails because sets are not indexed

x.add("e")
print("Set with .add():",x)
#x.add("f","g") # This is going to error, because .add can only have 1 argument
x.update("f","g") # This is what we do instead of ^
print("Set with .update():",x)

x.remove("e") # This works
x.discard("e") # This also works
#x.remove("e") # This is now going to fail, because "e" does not exist

popped = x.pop()
print("The set is now:",x," and I removed:",popped)
x.clear() # Empties the set
print("The set is:",x)

# -------------------
# Lists
# -------------------
print("\n#------------------------")
print("Lists")
print("#------------------------")
x = ["a","b","c","d"]
print("Full List:",x)
print("2nd Element:",x[1])

x.append("e") # Always on the end
print("Appended list:",x)
x.insert(2,"f") # Goes into the index specified
print("Inserted List:",x)

x[3] = "g"
print("Updated/Replaced List:",x)

x = ["a","a","b","c","d"]
print("List with duplicates:",x)
x.remove("a") # Will remove FIRST instance of element, since values are not unique
print("Removed List:",x)

x.pop(1) # Pops element at index ("b")
print("Popped List:",x)
x.pop() # Pops element at end of list ("d")
print("Popped from end:",x)

x = ["a","b","c","d"]
print("List:",x)
del x[0] # Deletes "a" by index
print("Deleted element from list:",x)
del x # Deletes the entire variable from memory
#print(x) # This will fail because the variable is no longer in existence

x = ["a","b","c","d"]
print("List:",x)
x.clear()
print("Cleared list:",x)

# -------------------
# Dictionaries
# -------------------
print("\n#------------------------")
print("Dictionaries")
print("#------------------------")
x = {
    "course": "CIS 314",
    "name": "Advanced Programming",
    "instructor": "Dane Henry",
    "credits": "3"
}
print("Dictionary:",x)
print("\nBetter print:")
for key, value in x.items():
    print(f"{key}: {value}")

print("Get Keys:", x.keys())
print("Get Value:", x.get["instructor"])

x["room"] = "Snyder 227" # This adds a new key-value pair to the dictionary
x.update({"roster":"13"}) # This does the same thing, but adds by way of appending a dictionary
for key, value in x.items():
    print(f"{key}: {value}")

print("The same methods can be used to update existing information.")