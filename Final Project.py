p=True
main=input ("entering as a admin or user:")
if (main=='a'):
    while p:
        name=input("enter username:")
        if name=="umer".lower():
            pas=input("enter password:")
            if pas=="uzair":
                print ("welcome to society management system")
                f=open(r"C:/Users/Mohammad Uzair/Downloads/python project.csv","r")
                a=f.readline()
                maintenance_bike=150
                maintenance_car=300
                maintenance_house=500
                my_list=[]
                k=0
                g='n'
                for i in a:
                    b=f.readline()
                    c=b.split(",")
                    my_list.append(c)
                f_no=int(input("enter flat no:"))
                while(k<=49):
                    if f_no==int (my_list[k][2]):
                        Tm=int (my_list[k][3])*maintenance_car+int (my_list[k][4])*maintenance_bike+int (my_list[k][5])
                        n_cars=int (my_list[k][3])
                        n_bikes=int (my_list[k][4])
                        m_cars=int (my_list[k][3])*maintenance_car
                        m_bikes=int (my_list[k][4])*maintenance_bike
                        g='y'
                        break
                    k=k+1
                if g=='y':
                    print (f"no of bikes={n_bikes}")
                    print (f"no of cars={n_cars}")
                    print (f"maintenance for bikes={m_bikes}")
                    print (f"maintenance for cars={m_cars}")
                    print (f"maintenance for house={int (my_list[k][5])}")
                    print (my_list[k][1],f"flat no {f_no} total maintenance=",Tm)
                    break
                else:
                    print ("invalid value")
            if name!="umer":
                pas_incorrect=input("enter username:")
                p=True
            if pas!="uzair":
                name_incorrect=input("enter password:")
                p==True
        else:
            if name=="admin":
                pas=input("enter password:")
                if pas=="021":
                    f=open("C:/Users/Mohammad Uzair/Downloads/python project.csv","r")
                    a=f.readline()
                    maintenance_bike=150
                    maintenance_car=300
                    maintenance_house=500
                    my_list=[]
                    k=0
                    for i in a:
                        b=f.readline()
                        c=b.split(",")
                        my_list.append(c)

                    while(k<=49):
                        Tm=int (my_list[k][3])*maintenance_car+int (my_list[k][4])*maintenance_bike+int (my_list[k][5])
                        n_cars=int (my_list[k][3])
                        n_bikes=int (my_list[k][4])
                        m_cars=int (my_list[k][3])*maintenance_car
                        m_bikes=int (my_list[k][4])*maintenance_bike
                        print (f"no of bikes={n_bikes}")
                        print (f"no of cars={n_cars}")
                        print (f"maintenance for bikes={m_bikes}")
                        print (f"maintenance for cars={m_cars}")
                        print (f"maintenance for house={int (my_list[k][5])}")
                        print (my_list[k][1],f"flat no {my_list [k][2]} total maintenance=",Tm,"\n")
                        k=k+1
                    break
                if pas!="021":
                    pas_incorrect=input("enter password:\n")
                    p=True
                if name!="admin":
                    name_incorrect=input("enter username:\n")
                    p==True
elif (main=='u'):
    read=open(r"C:/Users/Mohammad Uzair/Downloads/python project.csv","r") 
    readlines=read.readlines()
    usn=input("enter your user name:-")
    pasd=input("enter your password:-")
    passfile=open (r"C:/Users/Mohammad Uzair/Desktop/2.txt",'r')
    pss=passfile.readlines()
    leng=len (pss)
    to=0
    while (to<leng):
        ind=pss[to]
        split=ind.split (',')
        username=split[0]
        password=split[1]
        ret=readlines[to]
        split2=ret.split(',')
        in1=split2[1]
        in2=split2[2]
        in3=split2[3]
        in4=split2[4]
        in5=split2[5]
        
        if (username==usn and password==pasd):
          print(f"Your Name={in1}")
          print (f"Your Flat No is{in2}")
          print (f"No of Cars you have {in3} and total mantaince of your cars ={int(in3)*300}")
          print (f"No of Bikes you have {in4} and total maintenance for your bikes={int(in4)*150}")
          print (f"your house Mantainance={int (in5)}")
          print (f"so your total Maintanence ={int(in3)*300+int(in4)*150+int(in5)}")
        to+=1
else :
    if (username!=usn or password!=pasd):
        print ("invalid")
print ("Hope You Get's Your desire Information")

        
                 
    
    
