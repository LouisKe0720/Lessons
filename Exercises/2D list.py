shoe_rack = []
shoe_rack.append(["trainers", "sandals"])
shoe_rack.append(["brown shoes", "sneakers"])
shoe_rack.append(["red pumps", "soccer shoes"])

#To make a 2D list, add multiple lists to a list.
print(shoe_rack)

#It will return the length/amount of items in the list.
print(len(shoe_rack))

#To get the amount of items in the first row (zero-based index)
row = shoe_rack[0]
print(len(row))

#Insert, you can put it at a specific index. Append, adds to the end of list
shoe_rack.insert(1, ["ballet shoes", "red high heels"])
print(shoe_rack)

#Splicing is cutting the list based on what you specified. 0 is the index you start and the 2 means your ending one before 2 (zero-based index).
shoe_rack = shoe_rack[0:2]
print(shoe_rack)

#Prints the list all the way before 2. The second one does the same but prints every thing in the list. In this case, only 2 lists.
shoe_rack = shoe_rack[:2]
shoe_rack = shoe_rack[0:]
print(shoe_rack)

#Pops the last item in the list.
shoe_rack.pop()
print(shoe_rack)

#Removes the list that has this argument.
# shoe_rack.remove(["ballet shoes", "red high heels"])ruby
print(shoe_rack)

shoe_rack = []
shoe_rack.append(["trainers", "sandals"])
shoe_rack.append(["brown shoes", "sneakers"])
shoe_rack.append(["red pumps", "soccer shoes"])

#This will only have the first list in shoe rack and the last.
shoe_rack = shoe_rack[0:1] + shoe_rack[-1] 
print(shoe_rack)

#Sorts the items in alphabetical order
shoe_rack.sort()
print(shoe_rack)

#Reverses the order of the list.
shoe_rack.reverse()
print(shoe_rack)