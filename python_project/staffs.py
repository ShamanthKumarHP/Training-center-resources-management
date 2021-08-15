#1.Staff Management
from cursor import ptr,cnx

#to set as 0
def staff0(a):
    if len(a) == 0:
        a = 0
        return a
    else:
        return a
    
#displaying all info of staffs    
def staff1():
    query = "select * from staffs"
    ptr.execute(query)
    for a,b,c,d in ptr:
        print("Staff_ID:{0}   Name: {1}     Courses: {2}   MobNo: {3}".format(a,b,c,d))
    return

#inserting a new staff to staffs table
def insertStaffs(a,b,c):
    query = "insert into staffs (Names,Course,MobNo) values ('{0}','{1}','{2}')".format(a,b,c)
    ptr.execute(query)
    cnx.commit()
    return

#deleting a staff
def staff3(a):
    query = "delete from staffs where SID='{0}'".format(a)
    ptr.execute(query)
    cnx.commit()
    return

#main method
def staff():
    t1 = True
    while t1 == True:
            print("Staff details")
            staff1()
            print("1.Add new staff")
            print("2.Delete staff")
            print("3.Exit")
            
            aa = input("Enter your choice: ")            
            if aa =='1':
                Sname = input("Enter staff name ")
                if staff0(Sname) == 0:
                    print("Feilds can't be empty")
                    continue
                Course = input("Enter courses: ")
                Course = staff0(Course)
                Mobnumb = input("Enter mobile number: ")
                Mobnumb = staff0(Mobnumb) 
                insertStaffs(Sname,Course,Mobnumb)   
                
            elif aa=='2':
                stid = input("Enter Staff ID: ")
                staff3(stid) 
                
            elif aa == '3':
                t1 = False
                
            else:
                print("Enter Valid Choice")
    return

