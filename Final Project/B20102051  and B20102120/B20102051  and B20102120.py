p = True
main = input("entering as a admin or user(type'a' for admin and 'u' for user):")
if (main == 'a'):
    pak = open("C:\\Users\\Umar\\OneDrive\\Desktop\\1.txt", 'r')
    pak1 = pak.readlines()
    adusn1 = input("enter the Username")
    adpsd1 = input("Enter the Password")
    pak5 = len(pak1)
    s = 0
    while p:
        while s < pak5:
            in5 = pak1[s]
            sp5 = in5.split(',')
            adusn = sp5[0]
            adpsd = sp5[1]
            if (adusn == adusn1 and adpsd == adpsd1):
                print("welcome to society management system")
                ques1 = input("Do u want to change your Username  or Password or both?:-")
                if (ques1 == 'n'):
                    x=input("do you want to print whole list or search by flat no?l or f ")
                    print("Thank's for Answering")
                    f = open("C:\\users\\Umar\\OneDrive\\Desktop\\python project.csv", "r")
                    a = f.readline()
                    maintenance_bike = 150
                    maintenance_car = 300
                    maintenance_house = 500
                    my_list = []
                    k = 0
                    g = 'n'
                    for i in a:
                        b = f.readline()
                        c = b.split(",")
                        my_list.append(c)
                    if x=="f":
                        f_no = int(input("enter flat no:-\n"))
                        while (k <= 49):
                            if f_no == int(my_list[k][2]):
                                Tm = int(my_list[k][3]) * maintenance_car + int(my_list[k][4]) * maintenance_bike + int(
                                    my_list[k][5])
                                n_cars = int(my_list[k][3])
                                n_bikes = int(my_list[k][4])
                                m_cars = int(my_list[k][3]) * maintenance_car
                                m_bikes = int(my_list[k][4]) * maintenance_bike
                                g = 'y'
                                break
                            k = k + 1
                        if g == 'y':
                            print(f"name={my_list[k][1]}")
                            print(f"no of bikes={n_bikes}")
                            print(f"no of cars={n_cars}")
                            print(f"maintenance for bikes={m_bikes}")
                            print(f"maintenance for cars={m_cars}")
                            print(f"maintenance for house={int(my_list[k][5])}")
                            print(my_list[k][1], f"flat no {f_no} total maintenance=", Tm)
                            break
                        else:
                            print("invalid value")
                    if x == "l":
                        f = open("C:\\users\\Umar\\OneDrive\\Desktop\\python project.csv", "r")
                        a = f.readline()
                        maintenance_bike = 150
                        maintenance_car = 300
                        maintenance_house = 500
                        my_list = []
                        k = 0
                        for i in a:
                            b = f.readline()
                            c = b.split(",")
                            my_list.append(c)
                        while (k <= 49):
                            Tm = int(my_list[k][3]) * maintenance_car + int(my_list[k][4]) * maintenance_bike + int(
                                my_list[k][5])
                            n_cars = int(my_list[k][3])
                            n_bikes = int(my_list[k][4])
                            m_cars = int(my_list[k][3]) * maintenance_car
                            m_bikes = int(my_list[k][4]) * maintenance_bike
                            print(f"name={my_list[k][1]}")
                            print(f"no of bikes={n_bikes}")
                            print(f"no of cars={n_cars}")
                            print(f"maintenance for bikes={m_bikes}")
                            print(f"maintenance for cars={m_cars}")
                            print(f"maintenance for house={int(my_list[k][5])}")
                            print(my_list[k][1], f"flat no {my_list[k][2]} total maintenance=", Tm, "\n")
                            k = k + 1
                        break
                if (ques1 == 'y'):
                    ques2 = input("What will you like to Change Username,Password,or Both ?:-")
                    if (ques2 == 'u'):
                        ques = input("enter the new Username")
                        sp5[0] = ques
                        row = ','.join(sp5)
                        pak1[s] = row
                        print(pak1)
                        wri = open("C:\\Users\\Umar\\OneDrive\\Desktop\\1.txt", 'w')
                        for uu in pak1:
                            hhh = wri.write(uu)
                        wri.close()
                    if (ques2 == 'p'):
                        ques = input("enter the new Password")
                        sp5[1] = ques
                        row = ','.join(sp5)
                        pak1[s] = row
                        print(pak1)
                        wri = open("C:\\Users\\Umar\\OneDrive\\Desktop\\1.txt", 'w')
                        for uu in pak1:
                            hhh = wri.write(uu)
                        wri.close()
                    if (ques2 == 'b'):
                        ques = input("enter the new Username")
                        sp5[0] = ques
                        row = ','.join(sp5)
                        pak1[s] = row
                        print(pak1)
                        wri = open("C:\\Users\\Umar\\OneDrive\\Desktop\\1.txt", 'w')
                        for uu in pak1:
                            hhh = wri.write(uu)
                        wri.close()
                        ques = input("enter the new Password")
                        sp5[1] = ques
                        row = ','.join(sp5)
                        pak1[s] = row
                        print(pak1)
                        wri = open("C:\\Users\\Umar\\OneDrive\\Desktop\\1.txt", 'w')
                        for uu in pak1:
                            hhh = wri.write(uu)
                        wri.close()
                    f = open("C:\\users\\Umar\\OneDrive\\Desktop\\python project.csv", "r")
                    a = f.readline()
                    maintenance_bike = 150
                    maintenance_car = 300
                    maintenance_house = 500
                    my_list = []
                    k = 0
                    g = 'n'
                    for i in a:
                        b = f.readline()
                        c = b.split(",")
                        my_list.append(c)
                    x=input("do you want to print whole list or search by flat no?l or f ")
                    if x=="f":
                        f_no = int(input("enter flat no:-\n"))
                        while (k <= 49):
                            if f_no == int(my_list[k][2]):
                                Tm = int(my_list[k][3]) * maintenance_car + int(my_list[k][4]) * maintenance_bike + int(
                                    my_list[k][5])
                                n_cars = int(my_list[k][3])
                                n_bikes = int(my_list[k][4])
                                m_cars = int(my_list[k][3]) * maintenance_car
                                m_bikes = int(my_list[k][4]) * maintenance_bike
                                g = 'y'
                                break
                            k = k + 1
                        if g == 'y':
                            print(f"name={my_list[k][1]}")
                            print(f"no of bikes={n_bikes}")
                            print(f"no of cars={n_cars}")
                            print(f"maintenance for bikes={m_bikes}")
                            print(f"maintenance for cars={m_cars}")
                            print(f"maintenance for house={int(my_list[k][5])}")
                            print(my_list[k][1], f"flat no {f_no} total maintenance=", Tm)
                            break
                        else:
                            print("invalid value")
                    if x == "l":
                        f = open("C:\\users\\Umar\\OneDrive\\Desktop\\python project.csv", "r")
                        a = f.readline()
                        maintenance_bike = 150
                        maintenance_car = 300
                        maintenance_house = 500
                        my_list = []
                        k = 0
                        for i in a:
                            b = f.readline()
                            c = b.split(",")
                            my_list.append(c)
                        while (k <= 49):
                            Tm = int(my_list[k][3]) * maintenance_car + int(my_list[k][4]) * maintenance_bike + int(
                                my_list[k][5])
                            n_cars = int(my_list[k][3])
                            n_bikes = int(my_list[k][4])
                            m_cars = int(my_list[k][3]) * maintenance_car
                            m_bikes = int(my_list[k][4]) * maintenance_bike
                            print(f"name={my_list[k][1]}")
                            print(f"no of bikes={n_bikes}")
                            print(f"no of cars={n_cars}")
                            print(f"maintenance for bikes={m_bikes}")
                            print(f"maintenance for cars={m_cars}")
                            print(f"maintenance for house={int(my_list[k][5])}")
                            print(my_list[k][1], f"flat no {my_list[k][2]} total maintenance=", Tm, "\n")
                            k = k + 1
                        break        
            else:
                if (adusn!=adusn1 or adpsd!=adpsd1):
                    print ("invalid username or password")
                    break        
        s += 1    
elif (main == 'u'):
    read = open("C:\\Users\\Umar\\OneDrive\\Desktop\\python project.csv", "r")
    readlines = read.readlines()
    usn = input("enter your user name:-")
    pasd = input("enter your password:-")
    passfile = open("C:\\Users\\Umar\\OneDrive\\Desktop\\2.txt", 'r')
    pss = passfile.readlines()
    leng = len(pss)
    to = 0
    while (to < leng):
        ind = pss[to]
        split1 = ind.split(',')
        username = split1[0]
        password = split1[1]
        ret = readlines[to]
        split2 = ret.split(',')
        in1 = split2[1]
        in2 = split2[2]
        in3 = split2[3]
        in4 = split2[4]
        in5 = split2[5]
        if (username == usn and password == pasd):
            print("welcome to society management system")
            print(f"Resident's Name={in1}")
            print(f"Your Flat No is{in2}")
            print(f"No of Cars you have are  {in3} and total mantaince of your cars ={int(in3) * 300}")
            print(f"No of Bikes you have are  {in4} and total maintenance for your bikes={int(in4) * 150}")
            print(f"your house Mantainance={int(in5)}")
            print(f"Your total Maintanence ={int(in3) * 300 + int(in4) * 150 + int(in5)}")
            ques1 = input("Do u want to change your Username  or Password or both?:-")
            if (ques1 == 'n'):
                print("Thank For Visiting Here")

            if (ques1 == 'y'):
                ques2 = input("What will you like to Change Username,Password,or Both ?:-")
                if (ques2 == 'u'):
                    ques = input("enter the new Username")
                    split1[0] = ques
                    row = ','.join(split1)
                    pss[to] = row
                    wri = open("C:\\Users\\Umar\\OneDrive\\Desktop\\2.txt", 'w')
                    for uu in pss:
                        hhh = wri.write(uu)
                    wri.close()
                if (ques2 == 'p'):
                    ques = input("enter the new Password")
                    split1[1] = ques
                    row = ','.join(split1)
                    pss[to] = row
                    wri = open("C:\\Users\\Umar\\OneDrive\\Desktop\\2.txt", 'w')
                    for uu in pss:
                        hhh = wri.write(uu)
                    wri.close()
                if (ques2 == 'b'):
                    ques = input("enter the new Username")
                    split1[0] = ques
                    row = ','.join(split1)
                    pss[to] = row
                    wri = open("C:\\Users\\Umar\\OneDrive\\Desktop\\2.txt", 'w')
                    for uu in pss:
                        hhh = wri.write(uu)
                    wri.close()
                    ques = input("enter the new Password")
                    split1[1] = ques
                    row = ','.join(split1)
                    pss[to] = row
                    wri = open("C:\\Users\\Umar\\OneDrive\\Desktop\\2.txt", 'w')
                    for uu in pss:
                        hhh = wri.write(uu)
                    wri.close()
                if (ques2 != 'u' or ques2 != 'p' or ques3 != 'b'):
                    print("Invalid Input")
            break
        to += 1

    if (username != usn or password != pasd):
        print("Invalid username or password")
else:
    if main != 'a' or main != 'u':
        print("Invalid Input (Press a(admin) or u(user)) ")

print("Hope You Get's Your desire Information")
