try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
#
# tkinter._test()

mainWindow = tkinter.Tk()
mainWindow.title("Hello from the other side")
mainWindow.geometry("640x480+8+400")  # 8 pixels right from the left and 400 pixels down from the top

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='left')

button1 = tkinter.Button(mainWindow, text='button1')
button2 = tkinter.Button(mainWindow, text='button2')

button1.pack(side='top', anchor='n')
button2.pack(side='top', anchor='s')

mainWindow.mainloop()
