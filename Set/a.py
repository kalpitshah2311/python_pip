#20CE129
# Write a Python program to add member(s) in a set and clear a set
#A new empty set
color_set = set()
print(color_set)
print("\nAdd single element:")
color_set.add("Yellow")
print(color_set)
print("\nAdd multiple items:")
color_set.update(["White", "Black"])
print(color_set)

color_set.clear() #clear function is used to clear the set
print(color_set)
