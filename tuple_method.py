a = tuple([1,2,377])
print(a.index(2))


b=[1,2,55,4,11]
print(b.index(55))

for i in b:
    print(b.index(i), end=" ")

print("")
lst = [1, 5, 4, 3, 2, 7, 8]
print(lst.count(2))
print("최대:%d" %max(lst))
print("최소:%d" %min(lst))

tup = (1, 5, 4, 3, 2, 7, 3)
print(tup.count(3))
print("최대:%d" %max(tup))
print("최소:%d" %min(tup))

