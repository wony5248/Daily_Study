dic = dict()
lst = ["MC","BTS","BTS","MC","BTS"]
bbq = ["ABC","MC","BTS"]

for k in lst:
    if k in dic.keys():
        dic[k]+=1
    else:
        dic[k]=1

for k in bbq:
    if k in dic.keys():
        print(f"{k} : {dic[k]}")
    else:
        print(f"{k} : 0")