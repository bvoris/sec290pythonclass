# Nesting data structures
#
# When a data strucutre is a member of another data structure it is said to be "nested"
# Example: is a list of lists or list of dictionaries
#
# Nested data structures
#
# the data structures we'll cover include list tuple and dictionary
# the members of each can have members of ddifferent data types, for example the same list can have elements thats a string, another element thats and int and so forth
# a list can have an element thats another list a tuple or a dictionary
# the same is true for a tuple
# the values for the items in a dictionary can be virtually anything
# however since the keys for the dictionaries must be unique keys must be immutable, since lists are mutable they cannot be used as keys, tuples on the other hand can because tuples cannot change

#Example of a dictionary with Lists
student_grades = {
    "name":"Garcia",
    "quizzes": [80,95,100],
    "assignments":[100,85,90],
    "final_exam":88
    }
print(f'Grades for {student_grades["name"]}')
print(f'     Quizzes: {student_grades["quizzes"]}')
print(f'     Assignments: {student_grades["assignments"]}')
print(f'     Final Exam: {student_grades["final_exam"]}')