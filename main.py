

thislist = ["apple", "banana", "cherry"]

thislist.insert(1, "mango") # adding an item in the list

thislist[1] = "ovacado"

thislist.append("orange")

tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

thislist.remove("banana")

print(thislist)
thislist .sort()
for fruit in thislist:
    print(fruit)

print("-----")

for fruit in range(len(thislist)):
    print(thislist[fruit])