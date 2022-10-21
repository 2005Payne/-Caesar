a=list(input())
key=int(input())
for i in range(len(a)):
    if(ord(a[i])<91 and ord(a[i])>=65):
        a[i]=chr(((ord(a[i])-65+key)%26)+65)
    elif(ord(a[i])>=97 and ord(a[i])<=122):
        a[i]=chr(((ord(a[i])-97+key)%26)+97)
for i in a:
    print(i,end="")
