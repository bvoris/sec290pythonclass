# Oython and JSON
#
# Originally developed for JavaScript
# JavaScript Onbject Notation
# Simple way to stare and share data between programs is wreitten in the same or other languages
#
#Sharing/Saving/Restoring your data with JSON
# Sometimes you need to savee the state of your data structures for later or to share with anotehr program
# JSON is an easy way to do so
# To use JSON import the JSON module
# create a disctionary with an item for each of the data structures you want to store
# Before dumping your data to JSON store each data structure as an item in a dictionary
# dump the dictionary to JSON
# To restore your data structures from JSON
# Load the file to restore the dictionary
# overwrite each of your data structures from the items in the dictionary

# Saving data structures in a JSON File
import json
students = []
student_1 = {
    "name":"Garcia",
    "quizzes":[80,95,100]
    }
student_2 = {
    "name":"Culley",
    "quizzes":[95,87,95]
    }
students.append(student_1)
students.append(student_2)
save_it = {"students": students}
fp = open("grade_book.json", "w")
json.dump(save_it, fp)
fp.close()

# Restoring data structures from JSON FILE
students = []
fp = open("grade_book.json")
js = json.load(fp)
fp.close()
students = js["students"]
print(f'Student list: {students}')