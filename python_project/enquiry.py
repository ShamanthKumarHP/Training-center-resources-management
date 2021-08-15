#4.Course Enquiries of Students
from cursor import ptr,cnx


#returns null if course not found wrt course id
def retnull(Id):
    query = " select Cname from clist where CID = '{0}' ".format(Id)
    ptr.execute(query) 
    for l1 in ptr:
        l1 = ''.join(l1)
        return l1 

#inserting enquiry to enq table
def insertEnq(a,b,c,d,e,f,g):
    query = "insert into enq (Name,Pnum,Cs,Sess,Mail,OtherDetails,NewCourse) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(a,b,c,d,e,f,g)
    ptr.execute(query)
    cnx.commit()
    return

#main method
def enquiry():
    N = input("Enter Name: ")
    if len(N)==0:
        print("Feilds cannot be empty")
        return
    N = N.strip()
    P = input("Enter Ph.Number: ")
    P = P.strip()
    print("Available Courses")
    query = "select CID,Cname from Clist"
    ptr.execute(query)
    for c1,c2 in ptr:
        c2 = ''.join(c2)
        print("Course-ID:{0}   Name:{1}".format(c1,c2))
    print("Enter 0 for new course: ")
    while True:
        CI = input("Enter interested Course ID, ")
        if CI == '0':
            new = input("Enter new course name: ")
            new = new.upper()   #uppercase for new courses
            C = 0               #making course column as 0
            break
        else:                    
            cor = retnull(CI)  #course id as argument
            if cor == None:
                print("Enter valid course id: ")
                continue
            else:
                new = 0         #making NewCourse column as 0
                C = cor          #assigning course name ie returned from function
                break
                    
    print("Choose session: ")
    print("1.Weekend")
    print("2.Weekdays")
    print("3.Any")
    
    ch = input("Enter your choice: ")
    if ch == '1':
        D = 'Weekend'
    elif ch == '2':
        D = 'Weekdays'
    else:
        D = 'Any'
        pass 
        
    O = input("Other details: ")
    M = input("Enter Your mail Address: ")
    M = M.strip()
    M = M.lower()               #mail id should be in lowercase
    insertEnq(N,P,C,D,M,O,new)
    return                    
        