

thislist = ['banana', 'apple', 'cherry', 'mango']

for fruit in thislist:
    print(fruit)


print(len(thislist))


i = 0 

while i < len(thislist):
    print(thislist[i])
    i = i + 1



# List comprehension

print()
print("-----------List comprehension---------------")

[print(x) for x in thislist]


print("-------------New List-------------")

newlist = []

for fruit in thislist:
    if 'a' in fruit:
        newlist.append(fruit)

print(newlist)

# using list comprehension

newlist = [x for x in thislist if 'e' in x]

print(newlist)
