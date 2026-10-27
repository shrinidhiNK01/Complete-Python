# Python Lists
# =======================
l=[1,2,3,4,5,"Hello","Shri",90.54,True,None]
p=[2,4,6,8,10]
m=[4,8,12,16,20]

for i, j, k in zip(l, p, m):
    print(i, j, k)  

print(type(l))
print(enumerate(l))

# Mutable:- A data type whose value can be changed after its creation is called mutable.
# Immutable:- A data type whose value cannot be changed after its creation is called immutable.

# List is a mutable data type.

if 4 in l:
    print("4 is in the list")
else:
    print("4 is not in the list")

print(4 in l)   # True

marks=[10.2,56,689,57,97,46]

# List Methods:-
# =========================
print(len(marks))
print(sorted(marks))
print(marks.count(56)) 
print(marks.reverse())
print(marks.index(56)) 
print(marks.remove(56)) 
print(marks.pop())  # Remove the last element
print(marks.pop(0))  # Remove the first element
print(marks.append(100))  # Add the element at the end
print(marks.insert(0, 100))  # Add the element at the beginning
marks.copy()
marks.clear()
marks.extend(p)
print(marks.sort())

print(marks[1:-1]) # Slicing
# print([i*j*k for i in p for j in m for k in l])
print(marks[1::-1]) # Reverse Slicing
print(marks[1:4:2])

# List Comprehension
# =============================
ls=[i for i in range(4)]
print(ls)
ls=[i*i for i in range(14)]
print(ls)

# Concatenation:-
# ==============================
print(l+m)