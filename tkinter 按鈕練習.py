import tkinter as tk
import tkinter.messagebox
def ClickMe():
    tkinter.messagebox.showinfo(title = "小提示",message = "點進來是你人生最大的錯誤!>_<")
window = tk.Tk()
window.title("伯穎的專屬視窗")
window.geometry("500x150")
label = tk.Label(window,text="哈樓~我是伯穎!!", fg = "#00ffff")
label.pack()
entry = tk.Entry(window,width = 40)
entry.pack()
button = tk.Button(window,text = "按我!按我! CLICK ME!", command = ClickMe)
button.pack()
window.mainloop()
