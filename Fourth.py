# Tuples:- Immutable(cant change)
# ===============
tup= (1,5,6,5,5,5,5,5)
print(type(tup),tup)
print(tup[1])
print(tup[2:5])
print(tup[1:5])
print(tup[1:5:2])
print(tup[1:5:3])
# Tuple Methods:-
# =================
print(tup.index(1))
print(tup.count(1))
print(len(tup))


# Tuples is ordered 
# Tuples are fast 
# Tuples can be sliced

if 50 in tup:
    print("5 is in the tuple")
else:
    print("5 is not in the tuple")
    

# Manipulating tuples :- Convert it to list , change it and convert it back to tuple
# =====================
tup= (1,2,3,4)
tup2= (5,6,7,8)
tup3= tup+tup2
print(tup3)
tup4= tup*2
print(tup4)

temp=list(tup)
print(temp)
temp.append(9)
print(temp)
temp=tuple(temp)
print(temp)
temp.remove(1)
print(temp)
temp.pop()
print(temp)

print(tup.count(5))
print(tup.index(5))
print(tup.index(3,4,6))
tup.reverse()
print(tup)
tup.sort()
print(tup)