a=input ("enter new us")
z=input ("enter user name")
zz=input ("new us")
b=open (r"C:/Users/Mohammad Uzair/Desktop/2.txt",'r')
bb=b.readlines()
i=0
f=len (bb)
while (i<f):
    p=bb[i]
    s=p.split (',')
    u=s[0]
    pp=s[1]
    if u==z:
        s[0]=zz
        s[1]=a
        row=",".join(s)
        bb[i]=row
        
        
        break
    i+=1
print(bb)
gt=open ("C:/Users/Mohammad Uzair/Desktop/passwords.txt",'w')
for u in bb:
 gt.write(u)
gt.close()


    

    
