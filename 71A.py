n=int(input())
abreveration=[]
for word in range(n):
    word=input().strip()
    if len(word)>10:
        abreveration.append(word[0]+str(len(word)-2)+word[len(word)-1])
    else:
        abreveration.append(word)
for i in range(n):
        print(abreveration[i])