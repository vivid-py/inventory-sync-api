from db import *
import customtkinter as ctk

class App2(ctk.CTk):
    def __init__(self):
        super().__init()
        self.geometry("200x400")
        self.title("New Product in inventory")
class App1(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.theme = "light"
        self.geometry("500x500")
        self.title("Inventory Sync")
        self.configure(fg_color="#ade4ed")

        self.headerLabel = ctk.CTkLabel(self, text="API synced Inventory Management app", text_color="black", font=("Chiron GoRound TC",20))
        self.label1 = ctk.CTkLabel(self,text="here you can create new product in DB, which will sync with API", text_color="black",font=("Chiron GoRound TC",15))
        self.switchThemeButton = ctk.CTkButton(self, text="☾/☼", width=5,height=5, command=self.changeTheme)
        self.switchThemeButton.pack(side="top", anchor="ne", pady=5, padx=5)
        self.headerLabel.pack()
        self.label1.pack()
    def changeTheme(self):
        if self.theme == "light":
            self.theme = "dark"
            self.configure(fg_color="#284e54")
        elif self.theme == "dark":
            self.theme = "light"
            self.configure(fg_color="#ade4ed")


        




        
window = App1()
window.mainloop()