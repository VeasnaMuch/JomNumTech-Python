import os

class Student():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getSex(self):
        return self.sex
    

def display_main_menu ():   
    clear_screen()     
    print ("Please choose your action from 1..5. " \
           "\n1. Add new student to class"\
           "\n2. Remove a student by name from class"\
           "\n3. Display all student profile in the class"\
           "\n4. Count total student"\
           "\n5. Exit ")

def clear_screen():
    # 'nt' means Windows, others are usually Unix-based
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_for_action():
    input('Hit any key to continue ...')

def display_list_items(lstudents):
    if type(lstudents) is list:
        if(len(lstudents) == 0):
            print("\nThe class has no student")
        else:
            print("\nStudent of the class:")
            for stu in lstudents:
                print(f"Name: {stu.getName()} | Age: {stu.getAge()} | Sex: {stu.getSex()}")
    else:
        print("Function parameter is not list. It can not iterate to display elements.")

#number of dash characters to display
NDASH = 20

#global object of student
list_students = []



    
option = 0
while(option != 5):    
    display_main_menu()
    
    while True:
        option = input("Input your chouce: ")             
        try:
            option = int(option) 
            break                   
        except ValueError:
            print("No, your choise should be an integer.")

    match option:
        case 1: #Add new student
            print('-' * NDASH + " Add new Student " + '-' * NDASH )           
            #Student Name
            stName = input("Student Name: ")              
            #Student Age - validation only integer is accept
            while True:
                stAge = input("Student Age: ")            
                try:
                    stAge = int(stAge) 
                    break                   
                except ValueError:
                    print("No, Age should be an integer.")
            #Student Sex
            stSex = input("Student Sex: ") 

            #Create object student from input
            newStudent = Student(stName, stAge, stSex)

            #Append new instant of student object to the list
            list_students.append(newStudent)
            print("Student is added succesfull")
            pause_for_action()

        case 2: #Remove student by name         
            if len(list_students) == 0:
                print("\nThe class has no student, you can not remove any at the moment.")
            else: 
                student_name_to_remove = input("\nInput student name to remove: ")
                student_is_found = False
                for stu in list_students:
                    if stu.getName() == student_name_to_remove:
                        student_is_found = True
                        list_students.remove(stu)
                        print(f'Student name [{student_name_to_remove}] has been removed from  the class.')
                        break
                if student_is_found == False:    
                    print(f"\nNo student name [{student_name_to_remove}] in the class")   

            pause_for_action()          
           
        case 3: # display all student
            display_list_items(list_students)
            pause_for_action() 
        case 4:            
            print(f"\nTotal student count in the clas is : ", len(list_students))
            pause_for_action() 
          
  
data = [20]
display_list_items(data)