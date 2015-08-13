import urllib

def readText():
    quotes = open("C:\\Sumanth\\pythonprojects\\Udacity\\5\moviequotes.txt", 'r')
    contents = quotes.read()
    checkProfanity(contents)
    text2Pirate(contents)


def checkProfanity(contents):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+contents)
    output = connection.read()
    if "true" in output:
        print "Profanity alert!"
    elif "false" in output:
        print 'No curse words found!'
    else:
        print 'Something happened....'
    connection.close()

def text2Pirate(contents):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+contents)
    output = connection.read()
    print output
    connection.close()

readText()
