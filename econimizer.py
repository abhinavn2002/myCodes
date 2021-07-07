import pandas as pd
from datetime import datetime

hour = datetime.now().hour
day = datetime.now().day
anatomy = 2222/500
biochemistry = 8888/750
physiology = 8888/1000

file = pd.read_csv("log.csv")

def add():
    sub = input("Enter subject")
    pages = input("Enter number of pages")
    note = input("Add a note")
    data = pd.DataFrame([[hour,day,sub,pages,note]])
    data.to_csv("log.csv", mode = "a", header = False)
    if input("Add more?"):
        add()
		
def view():
    print(file)
    subset1 = file[file["day"]==day]
    subset2 = subset1[subset1["hour"]==hour]
    print("yes")
    print(subset2)
    count = 0
    cumsum = 0
    for i in subset2['sub']:
        j=subset2.iloc[count]
        print(i)
        if i == "a":
            cumsum += j['pages']*anatomy
        elif i == "p":
            cumsum += j['pages']*physiology
        else:
            cumsum += j['pages']*biochemistry
            
        count+=1
    print(cumsum)
	
	
if input("Want to add?"):
    add()
else:
    view()