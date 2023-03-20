a=input ("enter new")
b=open (r"C:/Users/Mohammad Uzair/Desktop/2.txt",'r')
bb=b.readlines()
c=open (r"C:/Users/Mohammad Uzair/Desktop/2.txt",'w')
i=0
f=len (bb)
while (i<f):
    p=bb[i]
    s=p.split (',')
    u=s[0]
    r=replace (u,a)
    w=c.write (r)
    print (bb)
    
