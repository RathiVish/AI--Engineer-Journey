# a=[1,2,3,4,5]
# print(a[1])

# a.pop(2)
# print(a)
# print(a[2])



# l = ["a", "b", "c"]

# l.append("d")       # add to the END     → ["a", "b", "c", "d"]
# l.insert(0, "z")    # add at index 0     → ["z", "a", "b", "c", "d"]

# l = ["b", "c"]
# print(len(l)) #2

# l.append("d")   
# l.insert(0, "a") 
# print(l)    #a,b,c,d
# print(len(l))   #4

# last = l.pop()  
# first = l.pop(0)
# print(last, first)  #d,a.  (Wrong)
# print(l)    #b,c

# print("c" in l) #true
# print("z" in l) #false

# print("d", "a")             # d a
# print("d", "a", sep=", ")   # d, a
# print("d", "a", sep="-")    # d-a

# import sys
# import timeit

# # 1. Watch over-allocation happen
# l = []
# prev = sys.getsizeof(l)
# print(f"len= 0  bytes={prev}")
# for i in range(30):
#     l.append(i)
#     size = sys.getsizeof(l)
#     if size != prev:
#         print(f"len={len(l):2}  bytes={size}   <- resized")
#         prev = size

# 2. append vs insert(0) on 100k items
# n = 100_000
# t_append = timeit.timeit("l.append(1)", setup="l = []", number=n)
# t_insert = timeit.timeit("l.insert(0, 1)", setup="l = []", number=n)
# print(f"append:    {t_append:.4f}s")
# print(f"insert(0): {t_insert:.4f}s   ({t_insert / t_append:.0f}x slower)")


# ---------------------------Dict-------------------------------

stock = {"apple": 5, "mango": 0}
stock["banana"] = 12
stock["apple"] = stock["apple"] + 3

# print(stock)


# Make a list of job IDs that contains duplicates, for example 8 IDs where 3 are repeated.
# Convert it to a set and print how many unique jobs there are.
# Check whether one job ID is in the set and print the result.
# Add a new job ID to the set and print the new count.
# Make a dict of 3 job titles and their salaries.
# Raise one salary by 10,000 (hint: you saw this in Q4) and print the dict.
# Use .get() with a default to look up a title that doesn’t exist, and print the result.
# Use f-strings for at least 2 of your prints, for example f"Unique jobs: {count}".
# Above each step, write a # comment with the time complexity of that operation, for example # O(1) - set lookup uses hashing.

#O(1)
jobIds = [123,345,678,123,654,765,345,654]

print(f"jobIds  {jobIds}")
#O(n)
uniqueIds = set(jobIds)
print(f"uniqueIds     {uniqueIds}")

print(123 in uniqueIds)

#O(n)
uniqueIds.add(980)
print(f"New set length  {len(uniqueIds)}")


#O(n)
roles = {"Tester": 50000, "Developer": 80000, "Manager": 100000}
print(f"Initial Salaries -> {roles}")
#O(1)
roles["Developer"] = roles["Developer"] + 10000
print(f"Revised salary->    {roles}")

#O(1)
isDesignerAvailable = roles.get("Designer", "Not hired yet") 
print(f"Designer -> {isDesignerAvailable}")




