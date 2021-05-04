# Types of files in python: Text file, CSV file and Binary file

# Modes for Text file and CSV file:
#     'r': for reading
#     'w': for writing
#     'a': for appending/writing
#     'r+': for reading and writing
#     'w+': for writing and reading

# Modes for Binary files:
#     'rb': for reading
#     'wb': for writing
#     'ab':for appending / writing
#     'rb+': for reading and writing
#     'wb+': for writing and reading

# 1st method for creating or open text file

# Text file

# file = open("<filename.exe>", "modes")
#
# file = open("Python.txt", 'w')
# file.write("Python is Easy.\n")
# file.write("Hi I am Satyam.\n")
# file.write("How are you?")
# print("Successfully enter the records.")
# file.close()

# file_read = open("Python.txt")
# data = file_read.read()
# data = file_read.readline()
# data = file_read.readlines()
# print(data)
# file_read.close()

import csv

# f = open("Student.csv", "w")
# n = int(input("Enter how many records you have to entered: "))
# for i in range(n):
#     roll = int(input("Enter roll number: "))
#     name = input("Enter name: ")
#     stu = [roll, name]
#     fwrite = csv.writer(f)
#     fwrite.writerow(stu)
# f.close()

# readfile = open("Student.csv", "r")
# data = csv.reader(readfile)
# for i in data:
#     print(i)
# readfile.close()

# Binary Files

import pickle
# stu = {}
# with open("Student.dat", 'wb') as stufile:
#     ans = 'y'
#     while ans == 'y':
#         roll = int(input("Enter roll number: "))
#         name = input("Enter name: ")
#         stu["Roll"] = roll
#         stu["Name"] = name
#         pickle.dump(stu, stufile)
#         ans = input("Want to append more records: ")
#         if ans == 'n':
#             break

with open("Student.dat", "rb") as readfile:
    try:
        while True:
            val = pickle.load(readfile)
            print(val)
    except EOFError:
        readfile.flush()





