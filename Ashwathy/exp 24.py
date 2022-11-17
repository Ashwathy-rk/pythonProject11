s=input("enter the string ")
dict={}
t=s.split(" ")
print(t)
for n in t:
    if n in dict:
        dict[n]+=1
    else:
        dict[n]=1
for m,n in dict.items():
     print(m,n)
