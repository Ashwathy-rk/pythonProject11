s=(input("enter the string  "))
dict={}
for n in s:
    if n in dict:
        dict[n]+=1
    else:
        dict[n]=1
for m,n in dict.items():
     print(m,n)