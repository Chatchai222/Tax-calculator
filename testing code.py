import tkinter as tk

HEIGHT = 500
WIDTH = 700
root = tk.Tk()

mytext = 'What is up'

def changetext(thelabel, newtext):
    thelabel['text'] = newtext




frame = tk.Frame(root, height=HEIGHT, width=WIDTH)
frame.pack()

label = tk.Label(frame, text='Hello')
label.place(relx=0.1, rely=0.1)

button = tk.Button(frame, text='Press me!', command=lambda: changetext(label, mytext))
button.place(relx=0.2, rely=0.7)

root.mainloop()






