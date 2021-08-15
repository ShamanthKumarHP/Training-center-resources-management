#main program
#run this program
from cursor import *

while True:
        print("1.Staff Management")
        print("2.Update details of staff")
        print("3.Course Management")
        print("4.Course Enquiries of Students")
        print("5.Enquiries List")
        print("6.Exit")
    
        ch = input("Enter your choice: ")                 
        if ch=='1':
            from staffs import *
            staff()                
        elif ch=='2':
            from updatingStaff import *
            updatestaff()
        elif ch=='3':
            from course import *
            course()                
        elif ch=='4':
            from enquiry import *
            enquiry()      
        elif ch=='5':
            from enquirylist import *
            enquirylist()
        elif ch=='6':
            break
        else:
            print("Please select correct option")
            pass
