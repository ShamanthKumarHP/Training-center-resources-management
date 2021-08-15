#5.Enquiries List

import matplotlib.pyplot as gp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cursor import ptr,cnx

#display all enquiries
def allenquiry():
    query="select * from enq "
    ptr.execute(query)
    i=1
    for a,b,c,d,e,f,g in ptr:                   
        print("{0}.Name:{1}    MobNo:{2}   Course:{3}   Session:{4}   mailID:{5}   Enquiry:{6} OtherCourse:{7} ".format(i,a,b,c,d,e,f,g))
        i=i+1
    return

#counting number of students requested for a course
def count(c,x):
    query = "select count(*) from enq where {0} like '{1}'".format(c,x)
    ptr.execute(query)
    for q in ptr:
        m = str(q[0])+"-"+x     #cancaination of course and its frquency with '-'
        return m       

#Notifying students wrt a course ie planned to begin        
def sendingmail(recname,recmail,coursename,User,Pw,startdate,starttime):
    subject = 'Hi {0} , {1} Course by Torus Solutions!'.format(recname,coursename)
    user_email = User
    msg = MIMEMultipart()
    msg['From'] = user_email
    msg['To'] = recmail
    msg['Subject'] = subject
    body = 'We are going to start new batch of {0} course from {1} and time {2} '.format(coursename,startdate,starttime)
    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()
    print("Sending mail to {0} ".format(recname))
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    try:
        server.login(user_email,Pw)
        try:
            server.sendmail(user_email,recmail,text)
            print("Message sent to {0}".format(recname))
        except:
            print("Invalid mail of {0}".format(recname))
    except :
        print("Authentication Error")        #incase of wrong mail-id of user
    server.quit()
    return

def getmail(courseColumn,courseName):
    User = input("Enter sender's e-mail id: ")
    if (User.endswith('@gmail.com')):
        pass
    else:
        print("Invalid mail-id ")
        return
    Pw = input("Enter Password: ")
    if len(Pw) == 0:
        print("Invalid Password ")
        return
    stdate = input("Enter Start date of course: ")
    if len(stdate) == 0:
        print("Invalid date ")
        return
    sttime = input("Enter time: ")
    if len(sttime) == 0:
        print("Invalid time: ")
    else:
        pass
    query = "select Name,Mail from enq where {0} like '{1}' ".format(courseColumn,courseName)
    ptr.execute(query)
    for fname,fmail in ptr: 
            fname = ''.join(fname)
            fmail = ''.join(fmail)
            try:
                sendingmail(fname,fmail,courseName,User,Pw,stdate,sttime)  
            except:
                print("Internet Error")
    return 

#respective course name with its count and printing in descending order
def coursecount(L1):
    L1.sort(reverse=True)
    Lcourse=[]
    Lstrength=[]
    Corid = ''
    for e in L1:
        s=e.split("-")               #num-course into list   
        Lcourse.append(s[1])         #appending course name    
        query = "select CID from clist where Cname = '{0}'".format(s[1])
        ptr.execute(query)
        for e in ptr:
            Corid = e[0]                 #tuple to str of course-id
            Lstrength.append(int(s[0]))  #appending course strength
            print("Course-ID:{2}    Name:{0}  ({1})".format(s[1],s[0],Corid))
    return Lcourse,Lstrength        

#bar graph of coursr name vs frequency
def graph(x,y):
    xy = gp.bar(x,y,width=0.9)
    xy[0].set_color('red')
    gp.show()
    return
        
def enquirylist():
    t6=True
    while t6==True:
        MixList=[]
        CorName=[]            
        A1=''
        column='Cs'
        query = "select Cname from clist"
        ptr.execute(query)            
        for f1 in ptr:
            f1=f1[0]                 #tuple to str
            CorName.append(f1)       #appending course name                 
        for j1 in CorName:
            A1 = count(column,j1)    #return of strength-course
            MixList.append(A1)
        N1,T1 = coursecount(MixList)             
        print("G.Visualize in chart ")
        print("M. For more options")
        print("0.Exit")
        print("Select course id planning to start",end="")
        
        sc = input()
        if sc=='G' or sc=='g':
            graph(N1,T1)
        
        elif sc=='M' or sc=='m':
            
            while True:                     
                print("Other requested courses: ")
                NC = []   #NewCourse column list
                query = "select NewCourse from enq"
                ptr.execute(query)
                for n in ptr:
                    n=n[0]              #str of NewCourse
                    NC.append(n)           
                NC = set(NC)            #removing duplicate of NewCourse
                NC.remove("0")          #removing default 0
                columnName='NewCourse'
                NL=[]    #for strength-course
                for e in NC:
                    B1 = count(columnName,e)
                    NL.append(B1)
                NL.sort(reverse=True)        
                i=1
                Ncourse = [] 
                Tfreq = []
                for e in NL:
                    s=e.split("-")     #num-NewCourse into list 
                    print("{2}.{0} ({1})".format(s[1],s[0],i))
                    Ncourse.append(s[1])     #appending Newcourse
                    Tfreq.append(int(s[0]))  #appending frequency
                    i=i+1
                    
                print("V.View detail enquiries ")
                print("G.Visualize in chart ")
                print("0. Back")
                print("Please Choose Option Of Course Planning To Start",end="")
                
                op = input("Enter your choice: ")                    
                if op == 'V' or op == 'v':
                    allenquiry()   #to display all enquiries
                    
                elif op == 'G' or op == 'g':
                    graph(Ncourse,Tfreq)
                
                elif op == '0':
                    break               
                try:
                    os=int(op)
                except ValueError:
                    print("Enter valid choice")
                    continue
                if os < len(NL)+1:
                    CT = 'NewCourse'          #name of column ie NewCourse in enq table
                    getmail(CT,Ncourse[os-1]) 
                else:
                    print("Enter correct option") 
                    
        elif sc=='0':
            break
        try:
            sc=int(sc)
        except ValueError:
            print("Enter valid choice")
            continue
        try:
            CT = 'Cs'     #name of column of course table in DB
            query = "select Cname from clist where CID = '{0}' ".format(sc)
            ptr.execute(query)
            for e in ptr:
                e = e[0]   # str of course name
            getmail(CT,e)  # column name and course name as arguments
            break
        except UnboundLocalError:  
            print("Enter valid course id")
            
        else:
            print("Enter correct option")
    return