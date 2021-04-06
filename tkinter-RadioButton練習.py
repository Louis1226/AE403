import tkinter as tk
window = tk.Tk()
window.geometry("700x700")
window.title("Create your own profile!")

Text1 = tk.StringVar()
Text2 = tk.StringVar()
def selection():
    label.config(text ="I am"+Text2.get()+"My blood type is"+Text1.get())
    
label = tk.Label(window, text = " You can buy these characters")
label.pack()

radio1 = tk.Radiobutton(window,
                        text="Aries(白羊座)"
                        ,variable=Text1
                        ,value= "Aries"
                        ,command = selection)
radio1.pack()

radio2 = tk.Radiobutton(window,
                        text="Taurus(金牛座)"
                        ,variable=Text1
                        ,value="Taurus"
                        ,command = selection)
radio2.pack()

radio3 = tk.Radiobutton(window,
                        text="Gemini(雙子座)"
                        ,variable=Text1
                        ,value="Gemini"
                        ,command = selection)
radio3.pack()

radio4 = tk.Radiobutton(window,
                        text="Cancer(巨蟹座)"
                        ,variable=Text1
                        ,value="Cancer"
                        ,command = selection)

radio4.pack()

radio5 = tk.Radiobutton(window,
                        text="Leo(獅子座)"
                        ,variable=Text1
                        ,value="Leo"
                        ,command = selection)
radio5.pack()

radio6 = tk.Radiobutton(window,
                        text="Virgo(處女座)"
                        ,variable=Text1
                        ,value="Virgo"
                        ,command = selection)
radio6.pack()

radio7 = tk.Radiobutton(window,
                        text="Libra(天秤座)"
                        ,variable=Text1
                        ,value="Libra"
                        ,command = selection)
radio7.pack()

radio8 = tk.Radiobutton(window,
                        text="Scorpio(天蠍座)"
                        ,variable=Text1
                        ,value="Scorpio"
                        ,command = selection)
radio8.pack()

radio9 = tk.Radiobutton(window,
                        text="Sagittarius(射手座)"
                        ,variable=Text1
                        ,value="Sagittarius"
                        ,command = selection)
radio9.pack()

radio10 = tk.Radiobutton(window,
                        text="Capricorn(摩羯座)"
                        ,variable=Text1
                        ,value="Capricorn"
                        ,command = selection)
radio10.pack()

radio11 = tk.Radiobutton(window,
                        text="Aquarius(水瓶座)"
                        ,variable=Text1
                        ,value="Aquarius"
                        ,command = selection)
radio11.pack()

radio12 = tk.Radiobutton(window,
                        text="Pisces(雙魚座)"
                        ,variable=Text1
                        ,value="Pisces"
                        ,command = selection)
radio12.pack()




radio13 = tk.Radiobutton(window,
                        text="A"
                        ,variable=Text2
                        ,value="A"
                        ,command = selection)
radio13.pack()

radio14 = tk.Radiobutton(window,
                        text="B"
                        ,variable=Text2
                        ,value="B"
                        ,command = selection)
radio14.pack()

radio15 = tk.Radiobutton(window,
                        text="O"
                        ,variable=Text2
                        ,value="O"
                        ,command = selection)
radio15.pack()

radio16 = tk.Radiobutton(window,
                        text="AB"
                        ,variable=Text2
                        ,value="AB"
                        ,command = selection)
radio16.pack()
window.mainloop()
