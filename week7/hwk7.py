#
# SEC290.12780.B1.Online
# Brad Voris
# 10/10/2022
# week 7 hwk7

menu = """
  Grade Book
  
  0: Exit
  1: Enter quiz grade for Student 1
  2: Enter quiz grade for Student 2
  3: Display current grades for all students

"""

class GradeBook:
    count = 0
    def __init__(self, name):
        self.name = name
        GradeBook.count += 1
        print("There are",GradeBook.count,"students in the grade book")
        print()
        self.grades = []      
    def quizScore(self,score):
        self.grades.append(score)    
  
    def currentAverage(self):
        sum = 0
        for i in self.grades:
            sum += i
        avg = sum/len(self.grades)
        return avg

name1 = input("Please enter the name for Student 1: ")
print()
Student1 = GradeBook(name1)
name2 = input("Please enter the name for Student 2: ")
print()
Student2 = GradeBook(name2)

while(True):
  print(menu)
  selection = input('Please enter a choice: ')
  if (selection == '0'):     
    break
  elif(selection == '1'):
    print(f'Student 1: ', name1)
    grade = float(input("Enter the grade for the quiz: "))  
    Student1.quizScore(grade)  
  elif(selection == '2'):
    print(f'Student 2: ', name2)
    grade = float(input("Enter the grade for the quiz: "))
    Student2.quizScore(grade)  
  elif(selection == '3'):
    print("Priting students grade reports....")
    print()
    print("Name:",Student1.name)    
    print("Current Average:",Student1.currentAverage())
    print()
    print("Name:",Student2.name)    
    print("Current Average:",Student2.currentAverage()) 