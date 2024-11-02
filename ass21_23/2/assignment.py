# From the previous list, print the odd names on the first line and the even names on the second line.
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# odd names
print(friends[::2])
# even names
print(friends[1::2])

# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"