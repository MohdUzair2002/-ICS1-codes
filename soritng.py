a=[22,55,44,33,11,66,99,00]
n=len(a)
print (a)
j=0
while (j<n):
    s=a[j]
    p=j
    i=j+1
    while(i<n):
        if a[i]<s:
            s=a[i]
            p=i
        i+=1
    a[p],a[j]=a[j],a[p]
    j+=1
print (a)
