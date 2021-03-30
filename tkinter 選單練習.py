import tkinter as tk
window = tk.Tk()
window.title("Game")
window.geometry("450x450")
MenuBar = tk.Menu(window)
FileMenu = tk.Menu(MenuBar, tearoff=False)
FileMenu.add_command(label= "Open New Game")
FileMenu.add_command(label= "Tutorial(How To Play)")
FileMenu.add_separator()
FileMenu.add_command(label= "Like & Subcribe!")
MenuBar.add_cascade(label="Basic Opitons", menu=FileMenu)

FileMenu2 = tk.Menu(MenuBar, tearoff = False)
FileMenu2.add_command(label= "Store")
FileMenu2.add_separator()
FileMenu2.add_command(label= "Buy Coins")
MenuBar.add_cascade(label= "Deposit", menu=FileMenu2)

SubMenu2 = tk.Menu(MenuBar,tearoff = False)
SubMenu2.add_command(label= "Sniper")
SubMenu2.add_command(label= "Assasin")
SubMenu2.add_command(label= "Sorcerer")
SubMenu2.add_command(label= "Assist")
FileMenu2.add_cascade(label="Buy Characters", menu= SubMenu2)


FileMenu3 = tk.Menu(MenuBar, tearoff = False)
FileMenu3.add_command(label= "Report Issue to Costumer Service")
MenuBar.add_cascade(label= "Problems", menu=FileMenu3)


SubMenu3 = tk.Menu(MenuBar, tearoff = False)
SubMenu3.add_command(label= "No sound")
SubMenu3.add_command(label= "Can't Open Mic")
SubMenu3.add_command(label= "Characters Reset")
SubMenu3.add_command(label= "Can't Type")
SubMenu3.add_command(label= "Internet Issue")
SubMenu3.add_command(label= "Server Can't Stop Uploading")
SubMenu3.add_command(label= "Trouble Signing in to Another Account")
SubMenu3.add_command(label= "Account Has Been Reset")
FileMenu3.add_cascade(label="Usual Problems", menu= SubMenu3)

FileMenu4 = tk.Menu(MenuBar, tearoff = False)
FileMenu4.add_command(label= "Turn On/Shut Off Reminder")
MenuBar.add_cascade(label= "Settings", menu=FileMenu4)

SubMenu4As1 = tk.Menu(MenuBar, tearoff = False)
SubMenu4As1.add_command(label= "Perfect(Large Amount of Battery)")
SubMenu4As1.add_command(label= "Normal")
SubMenu4As1.add_command(label= "Awful(Low Battery)")
FileMenu4.add_cascade(label="Picture Quality", menu= SubMenu4As1)

SubMenu4As2 = tk.Menu(MenuBar, tearoff = False)
SubMenu4As2.add_command(label= "Turn On/Shut Off Background Music")
SubMenu4As2.add_command(label= "Turn On/Shut Off Microphones")
SubMenu4As2.add_command(label= "Turn On/Shut Off Characters Lines")
FileMenu4.add_cascade(label="Sound Quality", menu= SubMenu4As2)



window.config(menu=MenuBar)
window.mainloop()


