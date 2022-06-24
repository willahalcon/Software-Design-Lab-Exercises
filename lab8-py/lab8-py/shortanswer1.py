import tkinter as tk #importing tkinter
root = tk.Tk() # creating root
root.configure(background='bisque') # background color
def pressed(): #function pressed
    print("Button pressed")

def create_layout(frame): #create layout
    b1=tk.Button(frame, text= "Button 1", bg="grey", command=pressed) #button with command total
    b1.pack(side='top', anchor= "w", pady="20px") #side is top and anchored to west with padding 20px vertically
    b2=tk.Button(frame, text="Button 2", bg="grey", command=pressed, padx= "20px") # button with command total
    b2.pack(side='left')
frame = tk.Frame(root, background='bisque') #frame
create_layout(frame)
frame.place(anchor="nw") #packing frame in the north west
root.geometry("200x200")
root.mainloop()
