import tkinter as tk
import random
import numpy
import pandas as pd    
   
class RandomWordChooserApp:
    def __init__(self, root,spec):
        self.spec=spec
        print(self.spec)
        self.root = root
        self.root.title(f"{spec}")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Click the button to choose a random player")
        self.label.pack(pady=10)


        self.choose_button = tk.Button(root, text="Choose Random Player", command=lambda:self.choose_random_word(0))
        self.choose_button.pack(pady=10)
        self.random_word_label = tk.Label(root, text="")
        self.random_word_label.pack()
        self.warning_label = tk.Label(root, text="")
        self.warning_label.pack()
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        self.sold_button = tk.Button(self.button_frame, text="Sold", command=lambda:self.choose_option(1,self.random_player))
        self.sold_button.pack(side='left',padx=10)
        self.sold_button.pack_forget()
        self.unsold_button = tk.Button(self.button_frame, text="Unsold", command=lambda:self.choose_option(2,self.random_player))
        self.unsold_button.pack(side="left",padx=10)
        self.unsold_button.pack_forget()
        
        self.selected=1
        self.player = self.load_player()
        self.random_player=""
        self.sold =[]
        self.unsold=[]

    def load_player(self):
        try:
            df = pd.read_excel('Players.xlsx')
            if self.spec in df.columns:
                df=df[~df[self.spec].isna()]
                player = df[self.spec].tolist()
            else:
                print("Error: column not found in the Excel file.")
                player = []
        except FileNotFoundError:
            print("Error: Players.xlsx file not found.")
            player = []

        return player

    def choose_random_word(self,case):
        if self.selected==1:
            self.warning_label.config(text="") 
            if self.player:
                random_player = random.choice(self.player)
                self.player.remove(random_player)
                self.random_word_label.config(text=f"Random Word: {random_player}\nRemaining: {len(self.player)}")
                self.random_player= random_player
                self.unsold_button.pack(side="left",padx=10)
                self.sold_button.pack(side='left',padx=10)
                self.choose_button.config(text="Next Player")
                self.selected=0
            else:
                self.warning_label.config(text="No words loaded. Please check words.xlsx file.")
        else:
          self.warning_label.config(text="No Option Selected. Please select below buttons")  
    def choose_option(self,case,random_player):
        if case==1:
            if random_player in self.sold:
                self.warning_label.config(text=f"{random_player} is already sold")
            elif random_player in self.unsold:
                self.warning_label.config(text=f"{random_player} is already unsold")
            else:
                self.sold.append(random_player)
                print(self.sold)
                self.warning_label.config(text=f"{random_player} is sold")
        elif case==2 :
            if random_player in self.sold:
                self.warning_label.config(text=f"{random_player} is already sold")
            elif random_player in self.unsold:
                self.warning_label.config(text=f"{random_player} is already unsold")
            else:
                self.unsold.append(random_player)
                print(self.unsold)
                self.warning_label.config(text=f"{random_player} is unsold")
        self.selected=1
 
class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Player Chooser")
        self.root.geometry("400x400")

        self.label = tk.Label(root, text="Choose a player type:")
        self.label.pack(pady=10)

        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack()

        self.batsmen_button = tk.Button(self.menu_frame, text="Batsmen", command=lambda: self.choosingWindow('Batsmen'))
        self.batsmen_button.pack(pady=10)

        self.spinner_button = tk.Button(self.menu_frame, text="Spinner", command=lambda: self.choosingWindow('Spinners'))
        self.spinner_button.pack(pady=10)

        self.seamers_button = tk.Button(self.menu_frame, text="Seamers", command=lambda: self.choosingWindow('Seamers'))
        self.seamers_button.pack(pady=10)

        self.wk_button = tk.Button(self.menu_frame, text="Wicketkeepers", command=lambda: self.choosingWindow('Wicketkeepers'))
        self.wk_button.pack(pady=10)

        self.allrounders_button = tk.Button(self.menu_frame, text="All-rounders", command=lambda: self.choosingWindow('Allrounders'))
        self.allrounders_button.pack(pady=10)
        
    def choosingWindow(self,spec):
        app_root=tk.Toplevel()
        app = RandomWordChooserApp(app_root,spec)
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()