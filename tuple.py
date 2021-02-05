a = (1, 3, 4, 2)
for i in range(len(a)):
    print(a[i], end=" ")
print("")
for i in a:
    print(i, end=" ")
print("")
for i in range(len(a)):
    print(i, end=" ")
print("")

def run():
    return (5, 3, 2)

ret = run()
print(ret)

def run1(a):
    for i in a:
        print(i, end=" ")
run1((1, 2, 3, 4, 5))
print("")
def test():
    b = [1,2,3,4,5]
    return b

c = test()
print(c)

def test1():
    return 1,5,3

a,b,c= test1()

print(a,b,c)


