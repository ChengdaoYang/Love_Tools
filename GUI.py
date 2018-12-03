import tkinter as tk
 
window = tk.Tk() 
window.title('my first window') 
window.geometry('400x150')  
 
window.mainloop()

l = tk.Label(window, text = 'hihi', bg = 'yellow', font = ('song',15),
             width = 12, height = 2)
l.pack()


var = tk.StringVar()
l = tk.Label(window, textvariable = var, bg = 'yellow', font = ('song',10),
             width = 12, height = 2)
l.pack()

hit = False
def cc():
    global on_hit
    if hit:
        hit = False
        var.set('')
    else:
        hit = True
        var.set('hihi')
b = tk.Button(window, text = 'click me', width = 10, height =1 , command = cc)
b.pack()


