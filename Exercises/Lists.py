#User square brackets to start a lsit
clothes_rack=[]
#To add, use append, add to end of list
clothes_rack.append("dress")
clothes_rack.append("trousers")
clothes_rack.append("socks")
clothes_rack.append("skirt")
clothes_rack.append("shirt")

print(clothes_rack)
#Splicing means to take a part of the list/cutting. The first (1) is the starting index and the (4) is the ending index. However, it will end before 4 and not include it.
print(clothes_rack [1:3])
print(clothes_rack [1:4])

#extends the list 
clothes_rack.extend(["t-shirt", "shoes", "cap"])
print(clothes_rack)

#Inserts before the given index
clothes_rack.insert(4, "gloves")
print(clothes_rack)

#Removes the first occurrence of the given item
clothes_rack.remove("shoes")
print(clothes_rack)

#Delete the given index in the list
del clothes_rack[5]
print(clothes_rack)

#It removes and returns the last item in the list
last_item = clothes_rack.pop()
print(last_item)

#Checks if the list contains the given item
if "dress" in clothes_rack:
    print("i have found my dress")
else:
    print("i cant find my dress")

#Returns the index of the word
print(clothes_rack.index("gloves"))

#Sorts the list in alphabetical order
clothes_rack.sort()
print(clothes_rack)

#Reverses the list
clothes_rack.reverse()
print(clothes_rack)

#Prints the items in the list with new line for each. The "x" is given the index value to all the items in the list. Your printing the index of x in that list.
for x in clothes_rack:
    print(x)