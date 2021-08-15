#2.Update details of staff
from cursor import ptr,cnx

#displaying all info of staffs 
def staff1():
    query = "select * from staffs"
    ptr.execute(query)
    for a,b,c,d in ptr:
        print("Staff_ID:{0}   Name: {1}     Courses: {2}   MobNo: {3}".format(a,b,c,d))
    return

#selecting details of a staff
def selection(a):
    query = " select Names,Course,MobNo from staffs where SID = '{0}' ".format(a)
    ptr.execute(query)
    for name,crs,mn in ptr:
        crs = ''.join(crs)       #tuple to string
        lis = crs.split(",")     #string to list
        return name,crs,lis,mn   #name,course,course as list,mobile no.

#cancatination of ',' for each course and updating
def addcomma(x,y,idname):
    i=1
    while i<len(y):
        x+=','+y[i]
        i=i+1
    query = "update staffs set Course = '{0}' where SID = '{1}' ".format(x,idname)
    ptr.execute(query)
    cnx.commit()

#main method
def updatestaff():
    print("Staff details")
    staff1()
    try:
        Sid = input("Enter Staff ID you want to update: ")
        t2 = True
        while t2 == True:
            name,fstr,flist,Mn=selection(Sid) 
            print("Details of ",name)
            print("Current Courses:",fstr)
            print("Mobile number:",Mn)
            print("1.Add your new course")
            print("2.Delete a course")
            print("3.Update Cell number")
            print("4.Exit")
                
            bb = input("Enter your choice: ")
            if bb == '1':
                Crs = input("Enter new courses: ")
                if len(Crs) == 0:
                    print("Feilds can't be empty")
                    continue
                Crs = Crs.strip() #removing spaces
                if flist[0] == '0':    #if there's no course
                    flist[0] = Crs
                else:
                    flist.append(Crs)                
                f = flist[0]            #inserting first element    
                addcomma(f,flist,Sid) # passing first element,course as list,staff id
                    
            elif bb == '2':
                small = []
                cap = [] #for upper case 
                capstr = ''
                cor = input("Enter course you want to Delete: ")
                cor = cor.upper()                    
                query = " Select Course from staffs where SID = '{0}' ".format(Sid)
                ptr.execute(query)
                for i1 in ptr:
                    i1 = ''.join(i1)
                    capstr = i1.upper()     #converting course string to upper case
                    cap = capstr.split(",") #converting to list
                    small=i1.split(",")     #converting course sting to list
                try:
                    ind = cap.index(cor) #finding index of course in cap list
                    small.pop(ind)       #deleting course of that index
                except ValueError:
                    print("Course not found")
                        
                ele1 = ''                
                if len(small) == 0:
                    ele1 = '0'           #set first element as 0
                else:
                    ele1 = small[0]      #assigning first element
                addcomma(ele1,small,Sid) #arguments as first element,course string,staff id
                    
            elif bb == '3':
                nn = input("Enter your new mobile number: ") 
                query = "update staffs set MobNo = '{0}' where SID = '{1}' ".format(nn,Sid)
                ptr.execute(query)
                cnx.commit()
            elif bb == '4':
                t2 = False
            else:
                print("Enter Valid Choice") 
                    
    except TypeError:
        print("Staff Not Found")
    return