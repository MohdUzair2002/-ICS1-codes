a=input ("enter the username:")
b=input ("enter the password:")
c=open (r"C:/Users/Mohammad Uzair/Desktop/2.txt",'r')
p=input ("enter the admin's pin:")
x=open (r"C:/Users/Mohammad Uzair/Downloads/python project.csv",'r')
d=c.readlines()
y=x.readlines()
e=len (d)
i=0
usl=[]
psl=[]
adl=[]
while (i<e):
    g=d[i]
    f=g.split (',')
    us=f[0]
    
    ps=f[1]
    ad=f[2]
    ff=len (y)
    k=0
    if (i==0):
       if (us==a and ps==b and ad==p ):
        
            print ("this admin's server")
            while (k<ff):
                za=y[k]
                zz=za.split (',')
                print (zz)
                k+=1
    t=y[i]
    o=t.split (',')
    v=o[0]
    vv=o[1]
    vvv=o[2]
    vvvv=o[3]
    vvvvv=o[4]
    vvvvv=o[5]
    l=0
        
    
              
    if (us==a and ps==b and p=='no'):
         print (f"The S.no. of the resident in the program is{v}")
         print (f"has Flat no {vv},Has bikes {vvv}")
         print (f"has cars {vvvv}")
         print (f"has house maintainance{vvvvv}")
    else:
        ("invalid entry")
    i+=1

else :
      "program ends"


        

        
        
   

    
    
    
