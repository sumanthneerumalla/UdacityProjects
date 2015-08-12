import os

def renameFiles():
    #Find the names of the file in the directory
    fileList = os.listdir(r"C:\Sumanth\pythonprojects\Udacity\2\secretmessage")
    saved_path = os.getcwd()
    print(fileList)
    os.chdir(r"C:\Sumanth\pythonprojects\Udacity\2\secretmessage")
    #Rename the files accordingly
    for eachFileName in fileList:
            newName = eachFileName.translate(None, "0123456789" )
            print "Old Name - ", eachFileName
            print "New Name - ", newName
            print
            os.rename(eachFileName, newName )
    os.chdir(saved_path)
    print(saved_path)
    print(os.getcwd())

renameFiles()
