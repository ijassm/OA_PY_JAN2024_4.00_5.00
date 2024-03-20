import os

# File Handling


# The open() function takes two parameters; filename, and mode.

# syntax

# open(filname, mode)


# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists


# example program

# try:
#     f = open("text.txt", "rt")
#     # print(f.read(10))
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     f.close()
#     print(f.readline())


# except Exception as e:
#     print(e)

# print("Testing")

# try:
#     f = open("demofile2.txt", "a")
#     f.write("Now the file has more content!\n")
#     f.close()


# except Exception as e:
#     print(e)

# print("Testing")

# try:
#     f = open("demofile2.txt", "w")
#     f.write("hello\n")
#     f.close()


# except Exception as e:
#     print(e)

# print("Testing")

# delete file

if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
