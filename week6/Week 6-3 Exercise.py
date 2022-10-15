#
# SEC290.12780.B1.Online
# Brad Voris
# 10/05/2022
# week 6 Exercise 6-3

grades = [{"student": "Schmidt", "quiz1": "85", "quiz2": "90", "quiz3": "100"},{"student": "Jones", "quiz1": "100", "quiz2": "95", "quiz3": "100"},{"student": "Garcia", "quiz1": "90", "quiz2": "92", "quiz3": "95"}]
fname = "ex6-3data.txt"
fp = open(fname, "w")

fp.write(f'Student\tQuiz 1\tQuiz 2\tQuiz 3\n')
for rec in grades:
    name = rec["student"]
    q1 = rec["quiz1"]
    q2 = rec["quiz2"]
    q3 = rec["quiz3"]
    fp.write(f"{name}\t{q1}\t{q2}\t{q3}\n")
fp.close
print()
print("Go Open {fname} and verify data has ben written")