a=input ("enter the u.m")
b=input ("enter the pass")
c=open (r"C:/Users/Mohammad Uzair/Desktop/2.txt",'r')
d=c.readlines()
e=len(d)
i=0
while (i<e):
    f=d[i]
    g=f.split(',')
    u=g[0]
    p=g[1]
    A=g[2].replace("\n","")
    if (a==u)and (b==p):
        print(g[2].replace("\n",""))
        print (d)
        
    i=i+1

    
