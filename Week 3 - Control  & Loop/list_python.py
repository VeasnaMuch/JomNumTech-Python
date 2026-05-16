class Student():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
def display_main_menu ():
    print ("Please choose your choice from 1..5. \n  To terminate using 5")


class_student = []
_student = Student("Veasna", 47, "Male")
class_student.append(_student)

#print(len(class_student))
#print(class_student[0].name)



    
ages = ["You", 2, "are", "welsome"]

#print(ages[:2])

#Insert "He" at index number 2
ages.insert(2, "He")
#print(ages)

#remove item at index number 2
ages.pop(2)
#print(ages)
    

option = 0
while(option != 5):
    display_main_menu()
    option = int(input("Input your chouce: "))
