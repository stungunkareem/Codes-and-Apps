import random
students = {'kareem':['cs208','cs217','cs479','cs201','math203'],'Hassan':['cs479','cs217','cs205','cs207','math203'],'sayed':['cs479','math201','math203','cs205','cs201'],'ali':['cs208','cs217','cs479','math111','math211'],'Ashraf':['cs208','cs217','cs205','math112','math203'],'Abdo':['cs208','cs217','cs205','math211','math201'],'yousef':['math201','cs217','math203','cs201','math203'],'tarek':['math211','cs205','math203','cs479','cs208'],'khaled':['cs479','cs217','math111','math201','cs201']}
Ta = {}
courses = {'cs208':200,'cs201':200,'cs479':200,'cs205':200,'cs217':200,'cs207':200,'math203':200,'math201':200,'math112':200,'math111':200}
courses_for_Ta={}
offeredcourses = []
def dividenconquer(list,n):
    if(len(list)==0):
        return False
    if(len(list)==1):
          if(list[0]==n):
              return True
          else :
              return False
    l = dividenconquer(list[0:int(len(list)/2)],n)
    r = dividenconquer(list[int(len(list)/2):len(list)],n)
    if l == True or r == True:
        return True
    else:
        return False
def generateTnL():
    slots = ["8:10", "10:12", "12:2", "2:4"]
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday"]
    lec_rooms = ["1", "52", "53", "264", "265"]
    tut_rooms = ["G17", "G18", "G29", "G25"]
    Lectures_Timing = []
    Tut_Timing = []
    lec=0
    tut = 0
    while (lec != 40):
        value = str(days[random.randint(0, 4)]) + '-' + str(slots[random.randint(0, 3)]) + '-' + str(lec_rooms[random.randint(0, 4)])
        if dividenconquer(Lectures_Timing,value) is True:
            continue
        else:
            Lectures_Timing.append(value)
            lec = lec + 1
    while(tut != 80):
        value = str(days[random.randint(0, 4)]) + '-' + str(slots[random.randint(0, 3)]) + '-' + str(tut_rooms[random.randint(0, 3)])
        if dividenconquer(Tut_Timing,value) is True:
            continue
        else:
            Tut_Timing.append(value)
            tut = tut + 1
    generatecourses(Lectures_Timing,Tut_Timing)

def updatecoursedic(list):
    for i in list:
        if dividenconquer(list(courses.keys()),i) is True:
           courses[i]=courses.get(i)+1
        else:
            courses[i]= 1
def student():
    if(len(students))==2000:
        print("Can't add more students.")
        return
    course_list=[]
    id=input("Enter your ID : ")
    course = 'course'
    print("Hint : After you finish entering the courses you want to study enter stop.")
    while(course!='stop'):
        course= input("Enter the course code : ").lower()
        if(course!='stop'):
            course_list.append(course)
            if(dividenconquer(offeredcourses,course)==False):
             offeredcourses.append(course)
    students[id]=course_list
    updatecoursedic(course_list)

def generatecourses(Lectures_Timing,Tut_Timing):
    shortcut = {}
    course_gen = []
    for i in courses.keys():
        if(courses[i]/50-int(courses[i]/50)!=0): #1.5 - 1 = 0.5
            for j in range(0,int(courses[i]/50+1)): #2
                list=[]
                tut_shortcut = {}
                string = i + "-" + str(j + 1) + "A-" + Tut_Timing[random.randint(0,79)]
                string_1 = string.split('-') #['cs208','1a','wednesday10:30','1']
                while(dividenconquer(list,string_1[2]+string_1[3])==True or dividenconquer(course_gen,string_1[2]+string_1[3]+string_1[4])==True ):
                    string = i + "-" + str(j + 1) + "A-" + Tut_Timing[random.randint(0,79)]
                    string_1 = string.split('-')
                course_gen.append(string_1[2]+string_1[3]+string_1[4])
                list.append(string_1[2]+string_1[3])
                tut_shortcut[string] = 0
                string = i + "-" + str(j + 1) + "B-" + Tut_Timing[random.randint(0,79)]
                string_1 = string.split('-')
                while (dividenconquer(list, string_1[2] + string_1[3]) == True or dividenconquer(course_gen,string_1[2]+string_1[3]+string_1[4])==True ):
                    string = i + "-" + str(j + 1) + "B-" + Tut_Timing[random.randint(0, 79)]
                    string_1 = string.split('-')
                course_gen.append(string_1[2] + string_1[3] + string_1[4])
                list.append(string_1[2] + string_1[3])
                tut_shortcut[string] = 0
                string = i + "-" + str(j + 1) + "-" + Lectures_Timing[random.randint(0, 39)]
                string_1 = string.split('-')
                while (dividenconquer(list, string_1[2] + string_1[3]) == True or dividenconquer(course_gen,string_1[2]+string_1[3]+string_1[4])==True ):
                    string = i + "-" + str(j + 1) + "-" + Lectures_Timing[random.randint(0, 39)]
                    string_1 = string.split('-')
                course_gen.append(string_1[2] + string_1[3] + string_1[4])
                shortcut[string]=tut_shortcut
        else:
            for j in range(0,int(courses[i]/50)):
                list = []
                tut_shortcut = {}
                string = i + "-" + str(j + 1) + "A-" + Tut_Timing[random.randint(0,79)]
                string_1 = string.split('-')
                while (dividenconquer(list, string_1[2] + string_1[3]) == True or dividenconquer(course_gen,string_1[2]+string_1[3]+string_1[4])==True ):
                    string = i + "-" + str(j + 1) + "A-" + Tut_Timing[random.randint(0, 79)]
                    string_1 = string.split('-')
                list.append(string_1[2] + string_1[3])
                course_gen.append(string_1[2] + string_1[3] + string_1[4])
                tut_shortcut[string] = 0
                string = i + "-" + str(j + 1) + "B-" + Tut_Timing[random.randint(0, 79)]
                string_1 = string.split('-')
                while (dividenconquer(list, string_1[2] + string_1[3]) == True or dividenconquer(course_gen,string_1[2]+string_1[3]+string_1[4])==True):
                    string = i + "-" + str(j + 1) + "B-" + Tut_Timing[random.randint(0, 79)]
                    string_1 = string.split('-')
                list.append(string_1[2] + string_1[3])
                tut_shortcut[string] = 0
                course_gen.append(string_1[2] + string_1[3] + string_1[4])
                string = i + "-" + str(j + 1) + "-" + Lectures_Timing[random.randint(0, 39)]
                string_1 = string.split('-')
                while (dividenconquer(list, string_1[2] + string_1[3]) == True or dividenconquer(course_gen,string_1[2]+string_1[3]+string_1[4])==True):
                    string = i + "-" + str(j + 1) + "-" + Lectures_Timing[random.randint(0, 39)]
                    string_1 = string.split('-')
                course_gen.append(string_1[2] + string_1[3] + string_1[4])
                shortcut[string] = tut_shortcut
    courses.clear()
    courses.update(shortcut)
    courses_for_Ta.update(shortcut)
def generateshedule():
    for i in students.keys():
        done_courses = []
        used_times = []
        schedule = []
        for m in courses:
            x=m.split("-")
            y=str(x[2]+x[3])
            left = dividenconquer(students[i],x[0])
            right = dividenconquer(used_times,y)
            middle = dividenconquer(done_courses,x[0])
            if (left is True)  and (right is False) and (middle is False):
                variable = list(courses[m])
                storage = variable[0].split('-')
                storage2 = variable[1].split('-')
                if (dividenconquer(used_times,storage[2] + storage[3])==False) or (courses[m][variable[0]] != 25):
                    courses[m][variable[0]] = courses[m][variable[0]] + 1
                    used_times.append(y)
                    used_times.append(storage[2] + storage[3])
                    schedule.append(m)
                    schedule.append(variable[0])
                    done_courses.append(x[0])
                else :
                    if (dividenconquer(used_times,storage2[2] + storage2[3])==False) or (courses[m][variable[1]] != 25):
                     courses[m][variable[1]] = courses[m][variable[1]] + 1
                     used_times.append(y)
                     used_times.append(storage2[2] + storage2[3])
                     schedule.append(m)
                     schedule.append(variable[1])
                     done_courses.append(x[0])
        students[i]=schedule
def generateTaschedule():
    for i in Ta.keys():
        used_times = []
        done_courses = []
        schedule = []
        for m in courses_for_Ta:
            x=m.split("-")
            y=x[2]+x[3]
            middle = dividenconquer(done_courses, x[0])
            if (dividenconquer(Ta[i],x[0]) == True) and (dividenconquer(used_times,y)==False) and m == False:
                variable = list(courses_for_Ta[m])
                storage = variable[0].split('-')
                storage2 = variable[1].split('-')
                if (dividenconquer(used_times,storage[2] + storage[3])==False) or (courses_for_Ta[m][variable[0]] != 1):
                    courses_for_Ta[m][variable[0]] = 1
                    used_times.append(storage[2] + storage[3])
                    schedule.append(variable[0])
                    done_courses.append(x[0])
                else :
                    if((dividenconquer(used_times,storage2[2] + storage2[3])==False) or (courses_for_Ta[m][variable[1]] != 1)):
                     courses_for_Ta[m][variable[1]] = 1
                     used_times.append(storage2[2] + storage2[3])
                     schedule.append(variable[1])
                     done_courses.append(x[0])
        Ta[i]=schedule
def ta():
    if (len(Ta)) == 80:
        print("Can't add more TA's.")
        return
    course_list = []
    id = input("Enter your ID : ")
    course = 'course'
    print("Hint : After you finish entering the courses you want to teach enter stop.")
    while (course != 'stop'):
        print("The courses you can teach : ", offeredcourses)
        course = input("Enter the course code : ").lower()
        if (course != 'stop'):
            if(course in offeredcourses):
                course_list.append(course)
            else:
                print("Enter a valid course.")
    Ta[id] = course_list

def studentsystem():
    while(True):
        print("1-Add courses\n2-Exit")
        x=eval(input("Enter your choice : "))
        if(x==1):
            student()
        if(x==2):
            return
def Tasystem():
    while (True):
        print("1-Add courses for Ta\n2-Exit")
        x = eval(input("Enter your choice : "))
        if (x == 1):
            ta()
        if (x == 2):
            return
generateTnL()
generateshedule()
print(courses,"\n\n\n\n")
print(students)


