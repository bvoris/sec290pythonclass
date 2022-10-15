# Tab delimited text files
#
# These are a simple kind of spreadsheet made up purely of plain text with each cell separated by a tab character.
# Tab delimited text files are a kind of CSV file, with a ".txt" file extension that  is supported by Microsoft Excel.

fp = open("tabdelimitedfile.txt", "w")
course_num = "sec290"
course_title = "Introduction to programming with Python"
term = "Fall 2022"
crn = "30040"
column_heading = "Course #\tTitle\tTerm\tCRN\n"
fp.write(column_heading)
row = f'{course_num}\t{course_title}\t{term}\t{crn}\n'
fp.write(row)
fp.close

# Reading a tab delimited text file
# 
# To read a tab delimited text file open it like any other text file. If it has column headings discard the firt line
# Read each line in a for loop
# strip the trailing newline character
# split the fields using the split method and the tab character as a delimiter

fp = open("datafile.txt")
fp.readline()
for line in fp:
    line = line.strip()
    name, q1, q2, q3 = line.split("\t")
    q1 = float(q1)
    q2 = float(q2)
    q3 = float(q3)
    avg = (q1 + q2 + q3)/3
    print(f'Grade for {name:10}: {avg:.1f}')
fp.close