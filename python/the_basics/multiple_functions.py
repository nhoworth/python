# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

help(sorted)

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

#outpu
#[20.0, 18.0, 11.25, 10.75, 9.5]

# sorted(iterable, key=None, reverse=False)
#     Return a new list containing all items from the iterable in ascending order.
    
#     A custom key function can be supplied to customise the sort order, and the
#     reverse flag can be set to request the result in descending order.
