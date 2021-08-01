# a,b,c = map(int, input().split())
# def change():
#     return (a,b,c)
# f1 = change()
#
# def plus():
#     return (a+5, b+5, c+5)
# f2=plus()
#
# def ABC():
#     print(f1)
#     print(f2)
# f3=ABC()
#
# def swap(a, b):
#     a, b = b, a
#     print(a)
#     print(b)
# f4=swap(f1, f2)

t = map(int, input().split())
t = tuple(t)

lst = []

for i in t:
    i += 5
    lst.append(i)
tup = tuple(lst)

print(tup)