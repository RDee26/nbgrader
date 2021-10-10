# Python program to explain os.remove() method
	
# importing os module
import shutil
	
# paths
assignmentPath = './assignments'
nbgraderPath = './nbgrader'
	
# Remove the specified
# file path
try:
	shutil.rmtree(r"% s" % assignmentPath)
except OSError as error:
	print(error)
	print("File path can not be removed")

try:
	shutil.rmtree(r"% s" % nbgraderPath)
except OSError as error:
	print(error)
	print("File path can not be removed")