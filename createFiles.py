import os

# Python program to explain os.mkdir() method
		
# path
assignmentPath = './assignments'
nbgraderPath = './nbgrader/submitted'

try:
	os.mkdir(assignmentPath)
except OSError as error:
	print(error)

try:
	os.makedirs(nbgraderPath)
except OSError as error:
	print(error)

studentCount = int(input("Enter number of students: "))

print('Starting to create test assignment files for % s students' % studentCount)

try:
  for i in range(studentCount):
    f = open(assignmentPath + "/RD0" + str(i+1) + ".ipynb", "w")
except Exception as error:
  print(error)

print('Test files created for % s students' % studentCount)
