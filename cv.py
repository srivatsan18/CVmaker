import sys
import tkinter as tk
from makeCertificate import makePDF
def callGUI():
    def makeThePDF():
        name = nameContent.get()
        dob = dobContent.get()
        hs = hsContent.get()
        hsmark = hsMarkContent.get()
        cgpa = cgpaContent.get()
        ph = phoneContent.get()
        em = emailContent.get()
        li = LIContent.get()
        we = WEContent.get()
        sk1 =skill1Content.get()
        sk2 =skill2Content.get()
        sk3 =skill3Content.get()
        im = imContent.get()
        if(im==""):
            im="prateekImg.jpeg"
        
        makePDF(name,dob,hs,hsmark,cgpa,ph,em,li,we,sk1,sk2,sk3,im)
        exit(0)
    def startThis():
        a = vara.get()
        sys.stdout.write(str(a))
        exit(0)

    def updateTheGUI():
        sys.stdout.write(str(updateReturnVal))
        exit(0)

    root = tk.Tk()
    root.title("CV maker")

    namelabel = tk.Label(root, text="Name  : ").grid(row = 0,column = 0)
    nameContent=tk.StringVar()
    nameEntryField = tk.Entry(root, textvariable = nameContent).grid(row = 0,column = 1)
    
    dobLabel = tk.Label(root, text="D.O.B  : ").grid(row = 1,column = 0)
    dobContent=tk.StringVar()
    dobEntryField = tk.Entry(root, textvariable = dobContent).grid(row = 1,column = 1)
    
    hsLabel = tk.Label(root, text="High School  : ").grid(row = 2,column = 0)
    hsContent=tk.StringVar()
    hsEntryField = tk.Entry(root, textvariable = hsContent).grid(row = 2,column = 1)
    
    hsMarkLabel = tk.Label(root, text="High School Marks : ").grid(row = 3,column = 0)
    hsMarkContent=tk.StringVar()
    hsMarkEntryField = tk.Entry(root, textvariable = hsMarkContent).grid(row = 3,column = 1)
    
    cgpaLabel = tk.Label(root, text="Agg CGPA : ").grid(row = 4,column = 0)
    cgpaContent=tk.StringVar()
    cgpaEntryField = tk.Entry(root, textvariable = cgpaContent).grid(row = 4,column = 1)
    
    phoneLabel = tk.Label(root, text="Contact NO : ").grid(row = 5,column = 0)
    phoneContent=tk.StringVar()
    phoneEntryField = tk.Entry(root, textvariable = phoneContent).grid(row = 5,column = 1)
     
    emailLabel =  tk.Label(root, text="Email : ").grid(row = 6,column = 0)
    emailContent=tk.StringVar()
    emailEntryField = tk.Entry(root, textvariable = emailContent).grid(row = 6,column = 1)
     

    LILabel =  tk.Label(root, text="Linked IN : ").grid(row = 7,column = 0)
    LIContent=tk.StringVar()
    LIEntryField = tk.Entry(root, textvariable = LIContent).grid(row = 7,column = 1)


    WELabel =  tk.Label(root, text="Work Exp : ").grid(row = 8,column = 0)
    WEContent=tk.StringVar()
    WEEntryField = tk.Entry(root, textvariable = WEContent).grid(row = 8,column = 1)

    skill1Label = tk.Label(root, text="Skill 1 : ").grid(row = 9,column = 0)
    skill1Content=tk.StringVar()
    skill1EntryField = tk.Entry(root, textvariable = skill1Content).grid(row = 9,column = 1)


    skill2Label = tk.Label(root, text="Skill 2 : ").grid(row = 10,column = 0)
    skill2Content=tk.StringVar()
    skill2EntryField = tk.Entry(root, textvariable = skill2Content).grid(row = 10,column = 1)


    skill3Label = tk.Label(root, text="Skill 3 : ").grid(row = 11,column = 0)
    skill3Content=tk.StringVar()
    skill3EntryField = tk.Entry(root, textvariable = skill3Content).grid(row = 11,column = 1)

    imLabel = tk.Label(root, text="Profile impath : ").grid(row = 12,column = 0)
    imContent=tk.StringVar()
    imEntryField = tk.Entry(root, textvariable = imContent).grid(row = 12,column = 1)


    makeIt = tk.Button(root, text="    START WIH THESE DETAILS    ", fg="blue", command=makeThePDF).grid(row = 13,column = 1)
    quitButton = tk.Button(root, text="QUIT", fg="red", command=quit).grid(row = 13,column = 0)

    root.mainloop()



if __name__ == "__main__":
    callGUI()
