import sys
input = sys.stdin.readline
word = list(input().rstrip())
result = []
string = ""
for i in range(len(word)-2):
    for j in range(i+1, len(word)-1):
        string = "".join(word[:i+1][::-1]) + "".join(word[i+1:j+1][::-1]) + "".join(word[j+1:][::-1])
        result.append(string)
result.sort()

print(result[0])
