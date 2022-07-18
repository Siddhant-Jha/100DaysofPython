import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

firstLabel = tkinter.Label(text="First Label")
firstLabel.pack()



window.mainloop()