import tkinter as tk
import tkinter.font as tkFont
import random, string
# from password_strength import PasswordPolicy
# import keyboard
 
def first():
    length = GLineEdit_780.get()
    if length.isdigit():
        length = int(length)
        chars = string.digits + "!@#$%_-[{^&*()`~}].,:" + string.ascii_letters
        return ''.join(random.choice(chars) for _ in range(length))
    else:
        return "check, Is your input is correct"


def result():
    password = GLineEdit_382.get()
    length = len(password)
    if length < 8:
        return "Weak: Password length should be at least 8 characters"
    
    # Check for uppercase, lowercase, digits, and special characters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    # Determine strength
    if has_upper and has_lower and has_digit and has_special:
        return "Your Password is :Strong"
    elif (has_upper and has_lower and has_digit) or (has_upper and has_lower and has_special) or (has_upper and has_digit and has_special) or (has_lower and has_digit and has_special):
        return "Your Password is :Medium"
    else:
        return "Your Password is :Weak "
            
class App:
    def __init__(self, root):
        #setting title
        root.title("PASSWORD MANAGER")
        #setting window size
        # root.iconbitmap("biresh.ico")
        width=600
        height=600
        root.configure(background="#1F1D1D")
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_496=tk.Label(root)
        GLabel_496["bg"] = "#343333"
        ft = tkFont.Font(family='Times',size=16)
        GLabel_496["font"] = ft
        GLabel_496["fg"] = "white"
        GLabel_496["justify"] = "center"
        GLabel_496["text"] = "password manager"
        GLabel_496.place(x=180,y=20,width=251,height=30)

        GMessage_891=tk.Label(root)
        GMessage_891["bg"] = "#343333"
        ft = tkFont.Font(family='Times',size=13)
        GMessage_891["font"] = ft
        GMessage_891["fg"] = "white"
        GMessage_891["justify"] = "center"
        GMessage_891["text"] = "Length of your password"
        GMessage_891.place(x=40,y=80,width=225,height=42)

        global GLineEdit_780
        GLineEdit_780=tk.Entry(root)
        GLineEdit_780["bg"] = "#343333"
        GLineEdit_780["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_780["font"] = ft
        GLineEdit_780["fg"] = "white"
        GLineEdit_780["justify"] = "center"
        GLineEdit_780["text"] = ""
        GLineEdit_780.place(x=360,y=80,width=110,height=40)

        GButton_42=tk.Button(root)
        GButton_42["bg"] = "#c4c1c1"
        ft = tkFont.Font(family='Times',size=16)
        GButton_42["font"] = ft
        GButton_42["fg"] = "#000000"
        GButton_42["justify"] = "center"
        GButton_42["text"] = "Generate"
        GButton_42.place(x=230,y=150,width=161,height=36)
        GButton_42["command"] = self.GButton_42_command

        

        GLabel_162=tk.Label(root)
        GLabel_162["bg"] = "#343333"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_162["font"] = ft
        GLabel_162["fg"] = "white"
        GLabel_162["justify"] = "center"
        GLabel_162["text"] = "check strength of your password"
        GLabel_162.place(x=60,y=280,width=475,height=51)

        GMessage_706=tk.Label(root)
        GMessage_706["bg"] = "#343333"
        ft = tkFont.Font(family='Times',size=17)
        GMessage_706["font"] = ft
        GMessage_706["fg"] = "white"
        GMessage_706["justify"] = "center"
        GMessage_706["text"] = "Enter your password"
        GMessage_706.place(x=40,y=340,width=217,height=34)

        global GLineEdit_382
        GLineEdit_382=tk.Entry(root)
        GLineEdit_382["bg"] = "#343333"
        GLineEdit_382["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=16)
        GLineEdit_382["font"] = ft
        GLineEdit_382["fg"] = "white"
        GLineEdit_382["justify"] = "center"
        GLineEdit_382["text"] = "Entry"
        GLineEdit_382.place(x=300,y=340,width=253,height=36)
        # keyboard.on_press(result())
        # keyboard.wait()
        
        GButton_722=tk.Button(root)
        GButton_722["bg"] = "#c4c1c1"
        ft = tkFont.Font(family='Times',size=15)
        GButton_722["font"] = ft
        GButton_722["fg"] = "#000000"
        GButton_722["justify"] = "center"
        GButton_722["text"] = "check strength"
        GButton_722.place(x=230,y=390,width=137,height=30)
        GButton_722["command"] = self.GButton_722_command


    def GButton_42_command(self):
        # first()
        GMessage_165=tk.Label(root)
        GMessage_165["bg"] = "#343333"
        ft = tkFont.Font(family='Times',size=18)
        GMessage_165["font"] = ft
        GMessage_165["fg"] = "white"
        GMessage_165["justify"] = "center"
        GMessage_165["text"] = first()
        GMessage_165.place(x=110,y=210,width=396,height=40)
        
    def GButton_722_command(self):
        GMessage_91=tk.Message(root)
        GMessage_91["bg"] = "#343333"
        ft = tkFont.Font(family='Times',size=18)
        GMessage_91["font"] = ft
        GMessage_91["fg"] = "white"
        GMessage_91["justify"] = "center"
        GMessage_91["text"] = result()
        GMessage_91.place(x=120,y=425,width=355,height=105)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
