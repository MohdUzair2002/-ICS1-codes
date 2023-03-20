a=[1,2,3,4]
b=[3,4,5,6,7]
i=0
d=[]
n=len (a)
p=len (b)
while (i<n and i<p):
    c=b[i]
    e=a[i]
    if c in a:
       if (c==e):
        d.append (c)
       else:
         d.append (c)
         d.append (e)
    else:
         if (c in d ):
           break
         else:
          d.append (c)
         if (e in d):
          list.sort (d)
         else:
          d.append (e)
    i=i+1
if (n!=p):
    if (n<p) :
        t=p-n
        q=b[-t]
        if q in d:
            list.sort (d)
        else:
            d.append (q)
    if (p<n):
        x=n-p
        g=a[-x]
        if g in d:
            list.sort (d)
        else:
            d.append (g)
list.sort (d)
print (d)
