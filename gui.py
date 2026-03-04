from db import *
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        self.geometry("1000x1000")
        self.title("Inventory Sync")
        
window = App()
window.mainloop()