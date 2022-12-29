from io import open
#Create file and save information
text_file = open("file.txt", "w")

phrase = "Welcome to the python programming course \nToday is wednesday"

text_file.write(phrase)

text_file.close()

#Read text from a file
print("####################################################")
text_file = open("file.txt", "r")

read_text = text_file.read()

text_file.close()

print(read_text)

#Save line by line in a list
print("####################################################")
text_file = open("file.txt", "r")

text_lines = text_file.readlines()

text_file.close()

print(text_lines)


#Add a new line of text
print("####################################################")
text_file = open("file.txt", "a")

new_text_line = "\nThis is a new line of text"

text_file.write(new_text_line)

text_file.close()

#Read text from a file and change position of pointer
print("####################################################")
text_file = open("file.txt", "r")
text_file.seek(12)
text_lines = text_file.read()

text_file.close()

print(text_lines)

#Reading and writing
print("----------------------------------------------------")
text_file = open("file.txt", "r+")

text_list = text_file.readlines()

text_list[1] = "This line has been included from the outside\n"

text_file.seek(0)

text_file.writelines(text_list)

text_file.close()


