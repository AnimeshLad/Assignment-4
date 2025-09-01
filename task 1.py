# Task 1: Read a File and Handle Errors

#1
file = open('sample.txt','r')
print(file.read())

#2
try:
    file = open('sample1.txt','r')
    print(file.read())
except FileNotFoundError:
    print("ERROR : File sample1.txt not found")