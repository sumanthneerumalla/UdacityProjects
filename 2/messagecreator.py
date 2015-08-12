import os
import shutil
import random

#Find the names of the file in the directory of alphabet
saved_path = os.getcwd()

fileList = os.listdir(r"C:\Sumanth\pythonprojects\Udacity\2\alphabet")

userMessage = raw_input("What message do you want to make? Enter a lowercase message only. You can use spaces and periods but no other punctuation")

alphabetArray = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","."," "]


for eachCharacter in userMessage:
    count = -1
    characterCount = 0
    print 'comparing ' + eachCharacter + ' from your input to',
    for eachLetter in alphabetArray:
        print eachLetter
        count = count + 1
        if eachLetter == eachCharacter:
            imageSource = "C:\\Sumanth\\pythonprojects\\Udacity\\2\\alphabet\\" + fileList[count]
            imageDest = "C:\\Sumanth\\pythonprojects\\Udacity\\2\\secretmessage\\ " + str(random.randrange(0,1000)) + alphabetArray[characterCount]
            print 'File to be copied is ', imageSource
            print 'It has been copied to ', imageDest
            shutil.copy(imageSource,imageDest)
            characterCount = characterCount + 1
            break