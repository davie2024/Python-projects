# create empty list
My_list = []

# append elements to the list
My_list.append(10)
My_list.append(20)
My_list.append(30)
My_list.append(40)

# Print the list to see the changes
print("After appending elements:", My_list)

# Insert a value at the second position
My_list.insert(1, "15")

# Print the list to see the changes
print("After inserting at the second position:", My_list)


# create another list to extend with
Another_list = [50, 60, 70] 

# Extend the fisrt list with the elements of the second list
My_list.extend(Another_list)

# Print the list to see the changes
print("After extending with another list:", My_list)

# Remove an element from My_list
My_list.remove(40)
# Print the list to see the changes
print("After removing element:", My_list)

# Sort My_list in ascending order
My_list.sort()

# Print the sorted list
print("Sorted list in ascending order:", My_list)

# Find the index of a value in My_list
value = 30
index = My_list.index(value)

# Print the index of the value
print(f"The index of {value} in the list is:", index)