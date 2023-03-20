a=int (input("enter the range"))
i=0
b=[]
while (i<a):
    t=i
    if (i<a):
        p=i+1
    s=t+p
    b.append (s)
    i=p+1
    if (b[-1]>=a):
      break
b.pop (-1)
print (b)   

