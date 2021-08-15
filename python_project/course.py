#3.Course Management
from cursor import ptr,cnx

#displaying all info of courses
def allcourse():
    query = "select * from Clist"
    ptr.execute(query)
    for a,b,c,d,e in ptr:
        print("Course-ID:{0}   Name:{1}   Duration:{2}days   Fee:{3}Rs. PreRq:{4}".format(a,b,c,d,e))
    return
 
#insert all arguments to course table   
def insertingCourse(a,b,c,d):
    query = "insert into Clist (Cname,Duration,Fee,PR) values ('{0}','{1}','{2}','{3}')".format(a,b,c,d)
    ptr.execute(query)
    cnx.commit()
    return

#main method
def course():    
    t3 = True
    while t3 == True:
        print("Present Courses: ")
        allcourse()       
        print("1.Add Course")
        print("2.Delete Course")
        print("3.Exit")
        
        cc = input("Enter your choice: ")        
        if cc == '1':
            CN = input("Enter new course name: ")
            if len(CN) == 0:
                print("Feilds can't be empty")
                continue
            CN = CN.strip()
            DT = input("Please Enter Duration Of Course In Days: ")
            FS = input("Enter Fee Of Course: ")
            PQ = input("Enter Prerequisite For Course: ")
            insertingCourse(CN,DT,FS,PQ)               
            
        elif cc == '2':
            CD= input("Enter Course ID you want to delete: ")
            query="delete from clist where CID='{0}'".format(CD)
            ptr.execute(query)
            cnx.commit()
        elif cc == '3':
            t3 = False
        else:
            print("Enter Valid Choice")
    return
    
