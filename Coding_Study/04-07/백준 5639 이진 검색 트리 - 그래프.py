import sys
tree = []
left = []
right = []
while(1):
    try:
        x = int(input())
        tree.append(x)
    except:
        break
root = tree[0]
for i in range(1, len(tree)):
    if tree[i] < tree[0]:
        left.append(tree[i])
    else:
        right.append(tree[i])

print(left)
print(right)

