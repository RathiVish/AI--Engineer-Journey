# a=[1,2,3,4,5]
# print(a[1])

# a.pop(2)
# print(a)
# print(a[2])



# l = ["a", "b", "c"]

# l.append("d")       # add to the END     → ["a", "b", "c", "d"]
# l.insert(0, "z")    # add at index 0     → ["z", "a", "b", "c", "d"]

l = ["b", "c"]
print(len(l)) #2

l.append("d")   
l.insert(0, "a") 
print(l)    #a,b,c,d
print(len(l))   #4

last = l.pop()  
first = l.pop(0)
print(last, first)  #d,a.  (Wrong)
print(l)    #b,c

print("c" in l) #true
print("z" in l) #false

print("d", "a")             # d a
print("d", "a", sep=", ")   # d, a
print("d", "a", sep="-")    # d-a

import sys
import timeit

# 1. Watch over-allocation happen
l = []
prev = sys.getsizeof(l)
print(f"len= 0  bytes={prev}")
for i in range(30):
    l.append(i)
    size = sys.getsizeof(l)
    if size != prev:
        print(f"len={len(l):2}  bytes={size}   <- resized")
        prev = size

# 2. append vs insert(0) on 100k items
n = 100_000
t_append = timeit.timeit("l.append(1)", setup="l = []", number=n)
t_insert = timeit.timeit("l.insert(0, 1)", setup="l = []", number=n)
print(f"append:    {t_append:.4f}s")
print(f"insert(0): {t_insert:.4f}s   ({t_insert / t_append:.0f}x slower)")



