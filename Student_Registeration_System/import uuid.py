from operator import add

import time
import json
import os
import sys 
import time
import asyncio
from sys import exit
import turtle
from xml.dom.minidom import Element

###################################################################################################
Students = [
    {
        "id":"20221",
        "name": "DEEB",
        "choosen_courses": []
    },
    {
        "id":"20222",
        "name": "BORIS",
        "choosen_courses": []
    },
    {
        "id":"20223",
        "name": "SABRETOOTH",
        "choosen_courses": []
    },
    {
        "id":"20224",
        "name": "KIROV",
        "choosen_courses": []
    },
    {
        "id":"20225",
        "name": "ZULFIQAR",
        "choosen_courses": []
    },
    {
        "id":"20226",
        "name": "RAMBO",
        "choosen_courses": []
    },
    {
        "id":"20227",
        "name": "IORI",
        "choosen_courses": []
    },
    {
        "id":"20228",
        "name": "WOLVERINE",
        "choosen_courses": []
    },
    {
        "id":"20229",
        "name": "BLAIDD",
        "choosen_courses": []
    },
    {
        "id":"20230",
        "name": "YURI",
        "choosen_courses": []
    },
    {
        "id":"20231",
        "name": "SCUD",
        "choosen_courses": []
    },
]
###################################################################################################
TA = [
    {
        "TA_ID" : "0001",
        "TA_Name" : "Omar Hussein",
        "Teaching_Course" : [],
    },
    {
        "TA_ID" : "0002",
        "TA_Name" : "Nikita Molotov",
        "Teaching_Course" : [],
    },
    {
        "TA_ID" : "0003",
        "TA_Name" : "Tanya Ryden",
        "Teaching_Course" : [],
    },
    {

        "TA_ID" : "0004",
        "TA_Name" : "Yuri Prime",
        "Teaching_Course" : [],
    },
]
###################################################################################################
Available_courses = [
    {
        "id":"MATH111",
        "name": "ANALYTICAL AND SOLID GEOMETERY - CALCULUS I",
        "course_slots": [{
            "day":"SUNDAY",
            
            
            "start_time":"10:30",
            "end_time":"12:29",
            
        },
        {
            "day":"TUESDAY",
            "start_time":"12:30",
            "end_time":"1:30",
        },
        
        ]
    },
    {
        "id": "MATH112",
        "name": "ANALYTICAL AND SOLID GEOMETERY - CALCULUS II",
        "course_slots": [{
            "day":"SUNDAY",
            "start_time":"10:30",
            "end_time":"12:29",
        },
    
        {
            "day":"TUESDAY",
            "start_time":"12:30",
            "end_time":"1:30",
        },
        
        ]
    },
    {
        "id": "MATH210",
        "name": "CALCULUS III",
        "course_slots": [{
            "day":"THURSDAY",
            "start_time":"2:00",
            "end_time":"4:29",
        },
        {
            "day":"WEDNESDAY",
            "start_time":"8:30",
            "end_time":"9:30",
        },
        
        ]
    },
    {
        "id":"MATH203",
        "name": "INTRODUCITON TO PROBABILITY AND STATISTICS",
        "course_slots": [{
            "day":"WEDNESDAY",
            "start_time":"8:30",
            "end_time":"10:30",
        },
        {
            "day":"TUESDAY",
            "start_time":"3:30",
            "end_time":"4:29",
        },
        
        ]
    },
    {
        "id":"MATH203",
        "name": "DIFFERENTIAL EQUATIONS",
        "course_slots": [{
            "day":"THURSDAY",
            "start_time":"1:00",
            "end_time":"3:30",
        },
        {
            "day":"MONDAY",
            "start_time":"2:30",
            "end_time":"3:29",
        },
        
        ]
    },
    {
        "id":"ENGL101",
        "name": "ENGLISH I",
        "course_slots": [{
            "day":"SUNDAY",
            "start_time":"9:00",
            "end_time":"10:30",
        },
        {
            "day":"WEDNESDAY",
            "start_time":"12:30",
            "end_time":"2:29",
        },
        
        ]
    },
    {
        "id":"ENGL201",
        "name": "ENGLISH II - WRITING SKILLS",
        "course_slots": [{
            "day":"MONDAY",
            "start_time":"12:30",
            "end_time":"1:30",
        },
        {
            "day":"WEDNESDAY",
            "start_time":"11:30",
            "end_time":"1:29",
        },
        
        ]
    },
    {
        "id":"ENGL202",
        "name": "COMMUNICATION AND PRESENTATION SKILLS",
        "course_slots": [{
            "day":"WEDNESDAY",
            "start_time":"8:30",
            "end_time":"9:30",
        },
        {
            "day":"SUNDAY",
            "start_time":"11:30",
            "end_time":"1:30",
        },
        
        ]
    },
    {
        "id":"CSCI101",
        "name": "COMPUTER AND INFORMATION SKILLS",
        "course_slots": [{
            "day":"SUNDAY",
            "start_time":"3:00",
            "end_time":"4:30",
        },
        {
            "day":"THURSDAY",
            "start_time":"12:30",
            "end_time":"2:29",
        },
        
        ]
    },
    {
        "id":"CSCI201",
        "name": "INTRODUCTION TO PROGRAMMING",
        "course_slots": [{
            "day":"MONDAY",
            "start_time":"10:29",
            "end_time":"12:29",
        },
        {
            "day":"SUNDAY",
            "start_time":"2:30",
            "end_time":"4:29",
        },
        
        ]
    },
    {
        "id":"CSCI205",
        "name": "INTRODUCTION TO COMPUTER SYSTEMS",
        "course_slots": [{
            "day":"THURSDAY",
            "start_time":"12:30",
            "end_time":"2:30",
        },
        {
            "day":"SUNDAY",
            "start_time":"11:30",
            "end_time":"12:30",
        },
        
        ]
    },
    {
        "id":"CSCI207",
        "name": "DATA STRUCTURE AND ALGORITHMS",
        "course_slots": [{
            "day":"TUESDAY",
            "start_time":"1:30",
            "end_time":"2:30",
        },
        {
            "day":"SUNDAY",
            "start_time":"3:29",
            "end_time":"4:29",
        },
        
        ]
    },
    {
        "id":"CSCI208",
        "name": "DESIGN AND ANALYSIS OF ALGORITHMS",
        "course_slots": [{
            "day":"SUNDAY",
           "start_time":"2:00",
            "end_time":"4:00",
        },
        {
            "day":"THURSDAY",
            "start_time":"11:00",
            "end_time":"12:59",
        },
        
        ]
    },
    {
        "id":"CSCI217",
        "name": "ADVANCED COMPUTER PROGRAMMING",
        "course_slots": [{
            "day":"TUESDAY",
            "start_time":"8:30",
            "end_time":"10:29",
        },
        {
            "day":"SUNDAY",
            "start_time":"12:00",
            "end_time":"1:29",
        },
        
        ]
    },
    {
        "id":"CSCI221",
        "name": "LOGIC DESIGN",
        "course_slots": [{
            "day":"MONDAY",
           "start_time":"12:30",
            "end_time":"2:30",
        },
        {
            "day":"SUNDAY",
            "start_time":"3:00",
            "end_time":"4:30",
        },

        ]
    },
    {
        "id":"CSCI479",
        "name": "SELECTED TOPICS IN COMPUTER SCIENCE",
        "course_slots": [{
            "day":"SUNDAY",
            "start_time":"11:30",
            "end_time":"1:30",
        },
        {
            "day":"MONDAY",
            "start_time":"11:29",
            "end_time":"1:29",
        },
        ]
    },
]
###################################################################################################
#access time slots mn el course el byet3mlo register listof two ubjext lecture w tut 
#loop 3leeh
#access awel Element
#access start time end time
#start > end 
#aw end < start 
#loop 3al courses el metsagela 
 




###################################################################################################


print("***************************************************************")
print("\t\tCourse Registeration")
print("***************************************************************")


is_student = True



my_courses=[]
def mainmenu():
    my_courses.clear()
    print("1- I am STUDENT")
    print("2- I am TEACHING ASSISSTANT")
    choice = input()
    if choice == "1":
        my_id=input("Welcome, kindly enter your student ID : ")
        if find_user_by_id("S",my_id):
            print('\t\tGreetings,',find_user_by_id("S",my_id))
            is_student=True
            
            os.system('cls')
            student_menu(find_user_by_id("S",my_id))
        else :
            print('*INVALID ID* ',"Kindly, check your ID and try again. ")
    elif choice == "2":
        my_id_2=input("Kindly, Enter your staff ID : ")
        if find_user_by_id("TA",my_id_2):
            print('\t\tGreetings,',find_user_by_id("TA",my_id_2))
            is_student=True
            
            os.system('cls')
            ta_menu(find_user_by_id("TA",my_id_2))
        is_student=False

    else:
        print("Kindly, Enter a valid ID")
        is_student=None
        time.sleep(1)
        return mainmenu() 

def student_menu(name):
    print("Greetings",name)
    print("1- Courses List")
    print("2- My Registered Courses")
    
    choice = input()
    if choice == "1":
        os.system('cls')
        course_list(name)
    elif choice == "2":
        os.system('cls')
        get_my_courses(name)

    else:
        print("Please, Enter a valid choice.")
        time.sleep(1)
        return student_menu() 

def find_user_by_id(type,id):

    if type=="S":
        for stud in range(len(Students)):
            if id == Students[stud]["id"]:
                return Students[stud]["name"]
        return None
    else:
        for ta in range(len(TA)):
            if id == TA[ta]["TA_ID"]:
                return TA[ta]["TA_Name"]
        return None



def ta_menu(name):
    print("Greetings,",name)
    print("1- Courses List")
    print("2- Register Courses")
    print("3- My Registered Courses as a TEACHING ASSISSTANT")
    
    choice = input()
    if choice == "1":
        os.system('cls')
        course_list(name)
    elif choice == "2":
        os.system('cls')
    elif choice == "3":
        os.system('cls')
    else:
        print("Kindly, Enter a valid choice.")
        time.sleep(1)
        return ta_menu() 





def course_list(name):
    results=[]
    for i in range(len(Available_courses)):
        results.append(Available_courses[i]["id"])
        print(Available_courses[i]["id"],Available_courses[i]["name"])
        print("")
    course_choice = input("Kindly, Enter a valid course ID to see its slots (or press e/E to return back to the menu) : ").upper()
    if course_choice in results:
        for j in range(len(Available_courses)):
            if course_choice == Available_courses[j]["id"]:
                print(Available_courses[j]["name"])
                for slot in Available_courses[j]["course_slots"]:
                    print(slot["day"],slot["start_time"], "--" ,slot["end_time"])
                course_add=input("would you like to add this course to the whishlist? y/n : ")
                if course_add == "y" or  course_add == "Y":
                        add_course(course_choice,name)
                        #time.sleep(2.5)
                        return course_list(name)
                elif course_add == "n" or  course_add == "N":
                    print("you will be redirected to courses list in 2 seconds")
                    #time.sleep(2)
                    course_list(name)
                else:
                    print("please enter a valid choice")
                    course_list()
                    
    elif course_choice == "e" or  course_choice == "E":
        student_menu(name)
    else:
        print("Course ID is invalid, Retry.")
        time.sleep(1)
        course_list(name)

def add_course(start_time,student_name):
    for stud in range(len(Students)):
            if student_name == Students[stud]["name"]:
                student_id=Students[stud]["id"]

    if start_time in my_courses:
        print("this course is already in your wishlist courses")
        return

    #elif course_slots in my_courses:
           # print("There is a clash")
            #return
    else:
        my_courses.append(id)
        print("Your Course List : ",my_courses)
        print("Your course was added successfully")
        time.sleep(1.5)
        return 





def get_my_courses(name):
    
    courses=[]
    for i in my_courses:
        for course in range(len(Available_courses)):
            if i == Available_courses[course]["id"]:
                print(i,Available_courses[course]["name"])
                for slot in Available_courses[course]["course_slots"]:
                    print(slot["day"],slot["start_time"], "--" ,slot["end_time"])
                    course_slot=Available_courses[course]["id"]+'_'+slot["day"] +'=>'+ slot["start_time"] + "-"+ slot["end_time"]
                    courses.append(course_slot)
    print(courses)               
    choice=input("press y/Y to confirm or (press e/E to go back to menu) : ")
    if choice == "e" or  choice == "E":
        student_menu(name)
    elif choice == "y" or choice=="Y":
        print('any')
        
    

    

mainmenu() 

    






                                                                     

