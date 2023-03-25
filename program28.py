'''
#read function
file = open("student.txt","r")

for line in file:
    print(line)
file.close()
'''
'''
#list
text = file.readlines()[0]
print(text)

'''

'''
print(file.readable())
text = file.read()
print(text)
size = len(text)
print(size)
'''


'''
file = open("student.txt","r")
print(file.readable())
file.close()

file = open("student.txt","r")
print(file.readable())
file.close()
'''

#append write

'''
file = open("student.txt", "a")

file.write("\nE - Lecturer of Arch")
file.close()
'''
file = open("student1.txt", "w")

file.write("\nE - Lecturer of Arch")

file.close()