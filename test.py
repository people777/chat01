dict01 = {}
dict01["aaa"] = "aaaaa"
dict01["bbb"] = "bbbbb"
dict01["ccc"] = "ccccc"
for item in dict01:
    print(item,dict01[item])
print("-------------")
del dict01["aaa"]
for item in dict01:
    print(item,dict01[item])