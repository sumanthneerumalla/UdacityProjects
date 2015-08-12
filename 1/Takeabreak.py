import time
import webbrowser

for range in (0,3):
    currenttime = time.ctime()
    print("current time is " , currenttime)
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
