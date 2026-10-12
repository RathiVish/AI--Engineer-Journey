a = [1, 2, 3]
b = a          # no copy is made: a second tag goes on the same list

# print(a)      # prints [1, 2, 3]
# print(b)      # prints [1, 2, 3]

b.append(4)

# print("after appending b")
# print(a)      # prints [1, 2, 3, 4]
# print(b)      # prints [1, 2, 3, 4]

b=[9]
# print("after reassigning b")
# print(a)      # prints [1, 2, 3, 4]
# print(b)      # prints [9]

x = [10, 20]
y = x
y.append(30)

print("before reassigning y")
print("x = ", x)    # prints [10, 20, 30]
print("y = ", y)    # prints [10, 20, 30]


y = [0]
print("after reassigning y")
print("x = ", x)    # prints [10, 20, 30]
print("y = ", y)    # prints [0]


### Mutating vs. Rebinding: “Mutating changes the object itself, for example append or list[0] = x,
#  so every reference to that object sees the change. Rebinding just points one name at a different object,
#  and other references are unaffected. That’s why passing a list to a function can change the caller’s data,
#  but reassigning the parameter inside the function can’t.”


def update(items, label):
    items.append(4)
    items = [99]
    label = label + "!"

nums = [1, 2, 3]
tag = "hi"
update(nums, tag)      
print(nums)     # prints [1, 2, 3, 4]
print(tag)      # prints "hi!"