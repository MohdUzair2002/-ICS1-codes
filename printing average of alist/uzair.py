a=[1,2,3,4,5,6,7,8,9,10]
i=0
t=0
k=len(a)
while (i<k):
    n=a[i]
    i=i+1
    t=t+n
    if (i==k):
        c=t/k
        print (i,"-",t,"-",c)
