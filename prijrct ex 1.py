a=open ("C:\\Users\\Mohammad Uzair\\Desktop\\passwords.csv",'r')
b=a.readlines()
print (b )
c=b[0].split(',')
d=c[1].replace("\n","")

print (d)



