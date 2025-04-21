from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Cognito Banking")

#icon = PhotoImage(file="https://img.wattpad.com/cover/335644642-256-k510095.jpg")
#window.iconphoto(True, icon)
window.config(background="#5cff5c")

welcome_label = Label(window, text="Welcome to Cognito Banking", font=("Arial", 20), bg="#5cff5c")

window.mainloop()
