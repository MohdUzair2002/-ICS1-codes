a=float (input("no."))
b=a%2
if (b==0):
    c=[]
    n=0
    a=a+2
    while(n<=9):
        c.append(a)
        a=a+2
        n=n+1
print (c)
