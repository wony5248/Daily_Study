dic = {"KFC": 10, "MC": 20, "MOMS": 30, "OTHER": 1000}
KFC = dic["KFC"]
MC = dic["MC"]
MOMS = dic["MOMS"]
a = input()
if a in dic:
    print(dic[a])
else:
    print(dic["OTHER"])

for i in dic.keys():
    print(i, end=" ")

# dic = dict()
# dic["MOMS"] = 30
# dic["KFC"] = 10
# dic["MC"] = 5
#
# a = input()
# print(dic[a])
