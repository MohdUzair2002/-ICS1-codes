a=float (input ("enter the range of the eq."))
b=float (input ("enter the range of the eq."))
x=a
fa=x**2+3 *x-10
x=b
fb=x**2+3 *x-10
f=fa * fb
if  (f>0):
    print ("given range does not have a solution")
else:
    fc = 1
    while (fc !=0):
        c = (a+b)/2
        x = c
        fc=x**2 +3*x - 10
        f = fa * fc
        if (f < 0):
            b = c
        else:
            a = c
            print (a,b,c)
print ("the solution is 1.8",(a,b,c))
    

    
    
    

