import tkinter as tk
from main import Company
import time

window = tk.Tk()
window.title('my window')
window.geometry('800x600')

# 这里是窗口的内容

#set var:
var = tk.StringVar()    # 这时文字变量储存器

#functions:
def get_ticker():
    name_ = input_box.get()
    text_box.insert('end',name_+'\n')
    var.set(Company(name_).ticker)

def get_keyword():
    name_ = input_box.get()
    text_box.insert('end',name_+'\n')
    var.set(Company(name_).keyword)

def get_price():
    name_ = input_box.get()
    text_box.insert('end',name_+'\n')
    var.set(Company(name_).price().head(7))
       
def get_summary():
    name_ = input_box.get()
    text_box.insert('end', 'getting'+name_+'\'s summarys...\n')
#     text_box.insert('end',name_+'\n')
    var.set(Company(name_).summary())
#     text_box.insert('end',name_+':\n')
#     text_box.insert('end',name_+' summary:')
    
def get_monitor():
    name_ = input_box.get()
    c = Company(name_)
    text_box.insert('end','sending email to '+c.email_list[0]+'\n')
    var.set('sending email to '+c.email_list[0]+'\n')
    for i in range(1,10):
        time.sleep(2)
        var.set('sending email to '+c.email_list[0]+str(i)+'\n')
    c.monitor()


    
    
    
    
    
#create 
input_box = tk.Entry(window)
input_box.pack()


text_box = tk.Text(window,height=2)
text_box.pack()


#ticker_button   
button_ = tk.Button(window, 
    text='ticker',      # 显示在按钮上的文字
    width=15, height=2 
    ,command=get_ticker   # 点击按钮式执行的命令
             )     
button_.pack()    # 按钮位置


#keyword
button_ = tk.Button(window, 
    text='name',      # 显示在按钮上的文字
    width=15, height=2 
    ,command=get_keyword   # 点击按钮式执行的命令
             )     
button_.pack()    # 按钮位置


#price
button_ = tk.Button(window, 
    text='price',      # 显示在按钮上的文字
    width=15, height=2 
    ,command=get_price   # 点击按钮式执行的命令
             )     
button_.pack()    # 按钮位置


#summary
button_ = tk.Button(window, 
    text='summary',      # 显示在按钮上的文字
    width=15, height=2 
    ,command=get_summary   # 点击按钮式执行的命令
             )     
button_.pack()    # 按钮位置


#monitor
button_ = tk.Button(window, 
    text='monitor',      # 显示在按钮上的文字
    width=15, height=2 
    ,command=get_monitor   # 点击按钮式执行的命令
             )     
button_.pack()    # 按钮位置



canvas = tk.Canvas(window, bg='blue', height=100, width=200)
canvas.pack()

# image_file = tk.PhotoImage(file='ins.gif')
# image = canvas.create_image(10, 10, anchor='nw', image=image_file)


l = tk.Label(window,           
#     text='OMG! this is TK!',    # 标签的文字
    textvariable=var,  # 使用 textvariable 替换 text, 因为这个可以变化
    bg='green',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=100, height=200  # 标签长宽
    )
l.pack()    # 固定窗口位置

window.mainloop()

