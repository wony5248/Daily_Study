N = int(input())
pattern = input()
filename = [input() for _ in range(N)]
start = pattern.index("*")
end = 0
for i in range(len(pattern)):
    if pattern[i] == "*":
        end = i

front = pattern[:start]
back = pattern[end+1:]

for i in range(N):
    if front == filename[i][:len(front)] and back == filename[i][-len(back):] and len(filename[i]) >= len(front) + len(back):
        print("DA")
    else:
        print("NE")