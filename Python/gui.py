import tkinter as tk
 
window = tk.Tk()
window.title("Padding in Tkinter")
window.geometry("400x400")
window.config(background = "Light Blue")
 
button = (window, 
                text = "Click me",
                bg = "white",
                fg = "red",
                border = 10,
                font = ("Arial", 30))
 
button.pack(padx = 100)
 
window.mainloop()