# Reading and writing text files in Python
#
# The ability to read a text file from Python makes Python a very valuable tool
# Text files consist of characters encoded in ASCII, UTF-8 or one of many other common ecoding standards
# Each line in a text file ends in a new line character
# There are several techniques for reading text files.
# When writing text files, the file can either be completely replaced or appended to.
# Sometimes you may need to maintain a running count, such as when reading a file.

# Text files are squences of lines of characters
# each line ends in a line break also known as a new line
# new lines are represented in text strings as ""\n"
# When a line is read from a text file, it includes the trailing new line character.
# when you write a line of text to a text file, be sure to include the trailing newline character.

# Use the open() function and specify the name of the file exactly and create a file object.
# text_file = open("myfile.txt")
# spelling must be exact
# be sure to include the file in thesame directory as your program
# One way to go is to read the entire file into a string using the read() method with no parameter.
# file_str = text_file.read()
#
# As the file is read a pointer is maintained by text_file is updated to point to the next line to be read
# After read() is called the file object pointer will point to the end of the file (EOF)
# You can also read a specified number of bytes by providing a count in the read parameter
# stuff =  text_file.read(5) provides 5 characters
# for the most part this technique is best used with binary files
# Remembner to close the file after you are done reading it.
#
# File Paths
#
# If you only include the file name in the open() call Python wlooks for the file in the same directory as your program file
# this is a kind of relative path
# YOu could choose to store your data in a subdirectory named data. In that case you would need to include the aname of the subdirectory followed by a slash followed by the file name
# Example: fp = open("data/my_file.text")
# This is also a relative path
#
# You can open a file anywhere on  your system assuming you have permission using an absolute path.
# fp = open("/var/log/auth.log")
# Relative paths tend to be portable meaning you dont have to edit your program to run it on another system. Absolute paths are not.
# In all cases when a slash is needed in a path use the forward slash even on Windows
# Example: fp = open("c:/documentes/newsletter/summer2018.pdf")
# Note that the backwards slkash has special meaning in python strings
#
# Sample
# Open the file first
text_file = open("sample.txt")
# Read the file
content = text_file.read()
# Close the file
text_file.close()
# Display content
print(content)
print()
#if you want to read a portion of the content you can put the number of character to read
text_file = open("sample.txt")
content01 = text_file.read(5) # 5 being the number of characters
text_file.close()
print(content01)
print()
# Reading one line at a time
#
# Since a text file is a squence it can be used in the for statement
# to read one line at a time use a for lopp in the statement
# The following reads sample.txt one line at a time and displays it
with open("sample.txt") as text_file:
    for line in text_file:
        print(line)
# by using with the file is automatically closed when the for loop is done

# Maintaining a running count
# Sometimes you need to count how many times something happens in a loop
# To do so
# Initalize a counter variable to zero before entering the loop
# each the condition you are looking for happens increment then counter
count = 0
keyword = "python"
with open("sample.txt", encoding='utf8') as text_file:
    for line in text_file:
        line = line.strip()
        print(line)
        if keyword in line:
            count += 1
print()
print(f'The term "{keyword}" appeared om {count} lines of the file.')
#
text_file =  open("sample.txt")
# read a specific line
# Read the first line
line1 = text_file.readline()
# Read line two
line2 = text_file.readline()
# Print both lines
print("#1: {}".format(line1))
print("#2: {}".format(line2))
print()
#ln =  3
#for line in text_file:
#    line = line.strip() # removes the line break
#    print("{}#: {}".format(ln, line))
#    ln+= 1
    
ln = 1
with open("sample.txt") as text_file:
    for line in text_file:
        line =  line.strip()
        print("{}#: {}".format(ln, line))
        ln += 1


# Note about Text File Compatibility
# Not all systems use the same form of text encoding
# if you created a text file with python on your system you should be able to read it withou a problem
# if the file you are trying to read was created on a different system or a different applicaiton then you might have to tell python which encoding to use in the open() call

# Reading a file all at once into a list
# You can read an entire file at once into a list
# its quickk and easy but not recommended
# doing so with a very large file will consume a lot of memory
#
#
fp = open("sample.txt", encoding='utf-8')

lines = fp.readlines()
fp.close
print(lines)
#
# Writing to text files
#
# To open a file for writing a mode parameter must be specified
# a is for appending to existing data
# w truncates (deletes) the current file and starts at the beginning
# In most cases its simplier and easier to rewrite a file  w then to append to it a.
# always close the file to ensure that the OS writes the data to disk
fp = open("writetome.txt", "w")
fp.write("hello world!\n")
fp.close()
