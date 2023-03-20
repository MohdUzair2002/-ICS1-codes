
def encryption():
    import math
    global mul
    numbers=['000','001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020','021','022','023','024','025','026']
    alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    desirednumberlength=0
    lengthofalphabets =len(alphabets)
##    numbers=[]
##    while(desirednumberlength<lengthofalphabets):
##         givennumbers=str(input(f"Enter desired number in accordance with {alphabets[desirednumberlength]}"))
##         numbers.append(givennumbers)
##         desirednumberlength+=1
    originalpassword="password is abcyzx"
    sepration=list(originalpassword)
    print(sepration)
    lengthofpassword=len(sepration)

    i=0
    numbersforonedigit=[]
    Mi=[]
    Ci=[]

    while(i<lengthofpassword):
        Indexofpassword=sepration[i]
        j=0
        while(j<lengthofalphabets):
            indexofalphabets=alphabets[j]
            if (Indexofpassword==indexofalphabets):
                numbersforonedigit.append(numbers[j])
                j=0
                break
            j+=1
        i+=1
    print(numbersforonedigit)
    seperationquantity=int(input("In how Many Words Do You want to break alphabets"))
    index1=(lengthofpassword/seperationquantity)
    index=math.floor(index1)
    sub=index1-index
    mul1=sub*index
    mul=lengthofpassword-mul1
    print(mul)
    rr=numbersforonedigit[-1]
    k=0
    m99=[]
    while(k<index):
        h=0
        while(h<seperationquantity):  
         m2=numbersforonedigit[h]
         m99.append(m2)
         if(h==seperationquantity-1):
            m995=''.join(m99)
            Mi.append(int(m995))
            m99=[]
            del numbersforonedigit[0:h+1]
          
            
         h+=1    
        k+=1
    if(lengthofpassword%seperationquantity!=0):
             r=0
             while(r<mul1):
               m2=numbersforonedigit[int(r)]

               Mi.append(int(m2))
               r+=1
    print(numbersforonedigit)
    l=0
    LengthofMi=len(Mi)
    while(l<LengthofMi):
          q=((Mi[l])**17)%2773
          Ci.append(q)
          l+=1
    r=0
    while(r<len(Ci)):
          Ci[r]=str(Ci[r])
          Ci[r]=Ci[r].zfill(seperationquantity*2)
          Mi[r]=str(Mi[r])
          Mi[r]=Mi[r].zfill(seperationquantity*2)
          r+=1

    print(Mi)
    print(Ci)
    encryptedkey=''.join (Ci)
    print(encryptedkey)
    list1=[]
    list1.append(Ci)
    list1.append(encryptedkey)
    print(list1)
    return list1
    



def Descryption (list1):
    
    global gg
##    encryptedkey='241719921354087902180276000118470488'
##    Ci=['2417','1992','1354','0879','0218','0276','0001','1847','0488']
    seperationquantity1=int(input("In how many digits do you break Encrption Key"))
    main=list1
    encryptedkey=main[1]
    Ci=main[0]
    lenci=len(Ci)
    i=0
    Mi=[]
    while(i<lenci):
        m1=(int(Ci[i]))
        m2=((m1**157))%2773
        m0=str(m2).zfill(seperationquantity1*2)
        Mi.append(m0)
        i+=1
    print(Mi)
    Mii=''.join(Mi)
    print(Mii)
    numbers=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
    alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    ln1=len(numbers)
    ig=0
    ihh=[]
    igg=0    
    while(igg<len(Mii)):
     fg=Mii[igg]+Mii[igg+1]
     ihh.append(fg)
     igg+=2
    print(ihh)    
    fgg=0
    fgg1=[]
    while(fgg<len(ihh)):
         dff=ihh[fgg]
         nm=0
         while(nm<len(alphabets)):
          dfff=numbers[nm]
          df=alphabets[nm]
          
          if(dfff==dff):
           fgg1.append(df)
           nm+=1
           break
          else:
              nm+=1
              
            
         fgg+=1
    print(fgg1)
    d=''.join(fgg1)
    print(d)
Descryption(encryption())


    
    
      
    
