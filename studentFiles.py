# Script to copy students' assignments from local folder into nbgrader folder sturcture

"""
Convention of nbgrader to find student's assignment is
<path to nbgrader folder>/submitted/<student id>/<name of the assignment>/<name of the notebook when created>
"""
# convention of nbgrader's submission folder
submissionsFolderNB = "submitted"
errorCount = 0


#configure path to local installation of nbgrader
pathToAssignments = "./assignments/"
pathToNB = "./nbgrader/" + submissionsFolderNB + '/'
assignmentName = 'ps'
nameOfNotebook = 'ps1.ipynb'

# Script to perform the copy operation
import os
import shutil

print("Moving the assignment files...")

# iterate over files in the localDirectory
for filename in os.listdir(pathToAssignments):
  try:
    fname, extension = filename.split('.') # fname stands for filename
    targetDir = pathToNB + fname + '/' + assignmentName
    os.makedirs(targetDir)
    target = targetDir + '/' + nameOfNotebook
    shutil.move(pathToAssignments + filename,target)
  except Exception as error:
    print(error)
    errorCount += 1
    continue

print("Execution complete. % s errors" % errorCount)
