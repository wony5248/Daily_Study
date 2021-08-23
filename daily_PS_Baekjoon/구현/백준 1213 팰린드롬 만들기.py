name = input()
dic = dict()
for i in name:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

odd = 0
oddalpha = ""
answer = ""

for i in dic:
    if dic[i] % 2 == 1:
        odd += 1
        oddalpha += i
    answer += i * (dic[i] // 2)
answer = list(answer)
answer.sort()
answer = "".join(answer)
if odd > 1:
    print("I'm Sorry Hansoo")

else:
    print(answer + oddalpha + answer[::-1])