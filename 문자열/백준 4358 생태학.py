import sys
input = sys.stdin.readline
trees = dict()
count = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    elif not trees.get(tree):
        trees[tree] = 1
    elif trees[tree]:
        trees[tree] += 1
    count += 1
lst = list(trees.keys())
lst.sort()
for i in lst:
    print("%s %.4f" %(i, round(100 * (trees[i] / count) , 4)))

