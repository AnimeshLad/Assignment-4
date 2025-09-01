# Task 2: Write and Append Data to a File

#1 Takes user input and writes it to a file named output.txt.
user_input  = input("enter text to write a file: ")
file = open('output.txt', 'w')
writing__data = file.write(user_input +'\n')

#2 Appends additional data to the same file.
user_input = input("enter additional text to append: ")
file = open('output.txt', 'a')
appending_data = file.write(user_input + '\n')

#3 Reads and displays the final content of the file.
file = open('output.txt','r')
reading_data = file.read()
print(reading_data)