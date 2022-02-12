#Number of Occurance of Words
# GITHUB-LINK->

t = int(input())

dicts = {}
for i in range(t):
    str = input()
    if str in dicts:
        dicts[str] +=1
    else:
        dicts[str] = 1
print(len(dicts))
for i in dicts.values():
    print(i ,end=' ')