import tkinter
import pandas as pd

windows = tkinter.Tk()
windows.title("Statistics")
windows.geometry('450x400')


def cal_stats():
    df = pd.read_csv("Sensorlogs.csv") # specify file path here 
    stats = df.describe()


    # temperature 

    tkinter.Label(windows, text="Temperature",font = "Helvetica 10 bold").grid(row=1,column=0)
    tkinter.Label(windows,text=df.temp.iat[-1]).grid(row=1,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','temp'].round(2)).grid(row=1,column=2) 
    tkinter.Label(windows,text=stats.loc['max','temp'].round(2)).grid(row=1,column=3) 
    tkinter.Label(windows,text=stats.loc['min','temp'].round(2)).grid(row=1,column=4)

    # humidity
    
    tkinter.Label(windows, text="Humidity",font = "Helvetica 10 bold").grid(row=2,column=0)
    tkinter.Label(windows,text=df.humidity.iat[-1]).grid(row=2,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','humidity'].round(2)).grid(row=2,column=2) 
    tkinter.Label(windows,text=stats.loc['max','humidity'].round(2)).grid(row=2,column=3) 
    tkinter.Label(windows,text=stats.loc['min','humidity'].round(2)).grid(row=2,column=4)

    # Shadow
    
    tkinter.Label(windows, text="Shadow",font = "Helvetica 10 bold").grid(row=3,column=0)
    tkinter.Label(windows,text=df.Shadow.iat[-1]).grid(row=3,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','Shadow'].round(2)).grid(row=3,column=2) 
    tkinter.Label(windows,text=stats.loc['max','Shadow'].round(2)).grid(row=3,column=3) 
    tkinter.Label(windows,text=stats.loc['min','Shadow'].round(2)).grid(row=3,column=4)

    # Mag X

    tkinter.Label(windows, text="Mag X",font = "Helvetica 10 bold").grid(row=4,column=0)
    tkinter.Label(windows,text=df.Magx.iat[-1]).grid(row=4,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','Magx'].round(2)).grid(row=4,column=2) 
    tkinter.Label(windows,text=stats.loc['max','Magx'].round(2)).grid(row=4,column=3) 
    tkinter.Label(windows,text=stats.loc['min','Magx'].round(2)).grid(row=4,column=4)
    
    # Mag Y

    tkinter.Label(windows, text="Mag Y",font = "Helvetica 10 bold").grid(row=5,column=0)
    tkinter.Label(windows,text=df['Mag Y'].iat[-1]).grid(row=5,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','Mag Y'].round(2)).grid(row=5,column=2) 
    tkinter.Label(windows,text=stats.loc['max','Mag Y'].round(2)).grid(row=5,column=3) 
    tkinter.Label(windows,text=stats.loc['min','Mag Y'].round(2)).grid(row=5,column=4)
    
    # Mag Z

    tkinter.Label(windows, text="Mag Z",font = "Helvetica 10 bold").grid(row=6,column=0)
    tkinter.Label(windows,text=df['Mag Z'].iat[-1]).grid(row=6,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','Mag Z'].round(2)).grid(row=6,column=2) 
    tkinter.Label(windows,text=stats.loc['max','Mag Z'].round(2)).grid(row=6,column=3) 
    tkinter.Label(windows,text=stats.loc['min','Mag Z'].round(2)).grid(row=6,column=4)
    
    # Magfield

    tkinter.Label(windows, text="Magfield",font = "Helvetica 10 bold").grid(row=7,column=0)
    tkinter.Label(windows,text=df['Magfield'].iat[-1]).grid(row=7,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','Magfield'].round(2)).grid(row=7,column=2) 
    tkinter.Label(windows,text=stats.loc['max','Magfield'].round(2)).grid(row=7,column=3) 
    tkinter.Label(windows,text=stats.loc['min','Magfield'].round(2)).grid(row=7,column=4)

    # sound

    tkinter.Label(windows, text="Sound",font = "Helvetica 10 bold").grid(row=8,column=0)
    tkinter.Label(windows,text=df['sound'].iat[-1]).grid(row=8,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','sound'].round(2)).grid(row=8,column=2) 
    tkinter.Label(windows,text=stats.loc['max','sound'].round(2)).grid(row=8,column=3) 
    tkinter.Label(windows,text=stats.loc['min','sound'].round(2)).grid(row=8,column=4)

    # reed

    tkinter.Label(windows, text="Reed",font = "Helvetica 10 bold").grid(row=9,column=0)
    tkinter.Label(windows,text=df['reed'].iat[-1]).grid(row=9,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','reed'].round(2)).grid(row=9,column=2) 
    tkinter.Label(windows,text=stats.loc['max','reed'].round(2)).grid(row=9,column=3) 
    tkinter.Label(windows,text=stats.loc['min','reed'].round(2)).grid(row=9,column=4)

    # Air

    tkinter.Label(windows, text="Air",font = "Helvetica 10 bold").grid(row=10,column=0)
    tkinter.Label(windows,text=df['Air'].iat[-1]).grid(row=10,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','Air'].round(2)).grid(row=10,column=2) 
    tkinter.Label(windows,text=stats.loc['max','Air'].round(2)).grid(row=10,column=3) 
    tkinter.Label(windows,text=stats.loc['min','Air'].round(2)).grid(row=10,column=4)

    # Touch sensor	

    tkinter.Label(windows, text="Touch sensor",font = "Helvetica 10 bold").grid(row=11,column=0)
    tkinter.Label(windows,text=df['Touch sensor'].iat[-1]).grid(row=11,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','Touch sensor'].round(2)).grid(row=11,column=2) 
    tkinter.Label(windows,text=stats.loc['max','Touch sensor'].round(2)).grid(row=11,column=3) 
    tkinter.Label(windows,text=stats.loc['min','Touch sensor'].round(2)).grid(row=11,column=4)

    # Rad uSv/hr

    tkinter.Label(windows, text="Rad uSv/hr",font = "Helvetica 10 bold").grid(row=12,column=0)
    tkinter.Label(windows,text=df['Rad uSv/hr'].iat[-1]).grid(row=12,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','Rad uSv/hr'].round(2)).grid(row=12,column=2) 
    tkinter.Label(windows,text=stats.loc['max','Rad uSv/hr'].round(2)).grid(row=12,column=3) 
    tkinter.Label(windows,text=stats.loc['min','Rad uSv/hr'].round(2)).grid(row=12,column=4)

    # sonar distance

    tkinter.Label(windows, text="Sonar distance",font = "Helvetica 10 bold").grid(row=13,column=0)
    tkinter.Label(windows,text=df['sonar distance'].iat[-1]).grid(row=13,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','sonar distance'].round(2)).grid(row=13,column=2) 
    tkinter.Label(windows,text=stats.loc['max','sonar distance'].round(2)).grid(row=13,column=3) 
    tkinter.Label(windows,text=stats.loc['min','sonar distance'].round(2)).grid(row=13,column=4)

    # interaction

    tkinter.Label(windows, text="interaction",font = "Helvetica 10 bold").grid(row=14,column=0)
    tkinter.Label(windows,text=df['interaction'].iat[-1]).grid(row=14,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','interaction'].round(2)).grid(row=14,column=2) 
    tkinter.Label(windows,text=stats.loc['max','interaction'].round(2)).grid(row=14,column=3) 
    tkinter.Label(windows,text=stats.loc['min','interaction'].round(2)).grid(row=14,column=4)

    # Anomoly

    tkinter.Label(windows, text="Anomoly",font = "Helvetica 10 bold").grid(row=15,column=0)
    tkinter.Label(windows,text=df['Anomoly'].iat[-1]).grid(row=15,column=1)     
    tkinter.Label(windows,text=stats.loc['mean','Anomoly'].round(2)).grid(row=15,column=2) 
    tkinter.Label(windows,text=stats.loc['max','Anomoly'].round(2)).grid(row=15,column=3) 
    tkinter.Label(windows,text=stats.loc['min','Anomoly'].round(2)).grid(row=15,column=4)

    windows.after(900, cal_stats) # 15 min = 900 sec
    


    # l1.grid(column=1,row=2)
    # l1 = tkinter.Label(windows, text=hum)
    # l1.grid(column=1,row=3)
    



tkinter.Label(windows, text="current",font = "Helvetica 10 bold").grid(row=0,column=1,padx=20, pady=5)
tkinter.Label(windows, text="Average",font = "Helvetica 10 bold").grid(row=0,column=2,padx=20, pady=5)
tkinter.Label(windows, text="High",font = "Helvetica 10 bold").grid(row=0,column=3,padx=20, pady=5)
tkinter.Label(windows, text="low",font = "Helvetica 10 bold").grid(row=0,column=4,padx=20, pady=5)

windows.after(0, cal_stats)  # add_letter will run as soon as the mainloop starts.
windows.mainloop()

