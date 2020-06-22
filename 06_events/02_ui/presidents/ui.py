import tkinter as tk
from presidents_db import PresidentsDatabase 

class PresidentsApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.presidedents_db = PresidentsDatabase()
        self._load_data()
        self.master = master
        self.master.wm_title("President's UI")

        self.presidents_list = PresidentsList(self)
        self.president_panel = PresidentPanel(self)
        self.presidents_list.pack()
        self.pack()
    
    def show_president(self, president):
        self.presidents_list.pack_forget()
        self.president_panel.show(president)
        self.president_panel.pack()
    
    def show_list(self):
        self.president_panel.pack_forget()
        self.presidents_list.pack()

    def _load_data(self):
        self.presidedents_db.open()
        self.presidedents_db.load_presidents()
        self.presidedents_db.close()

class PresidentsList(tk.Frame):
    def __init__(self, pres_app: PresidentsApplication):
        super().__init__(pres_app)
        self.pres_app = pres_app
        self.make_presidents_list()

    def make_presidents_list(self):
        scrollbar = tk.Scrollbar(self)

        self.listbox = tk.Listbox(self, yscrollcommand=scrollbar.set)
        for president in self.pres_app.presidedents_db.presidents:
            self.listbox.insert(tk.END, president.name)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(fill=tk.BOTH, expand=1)

        scrollbar.config(command=self.listbox.yview)

        select_button_frame = tk.Frame(self)
        select_button_frame.pack(side="bottom")
        select_button = tk.Button(
            select_button_frame, text="View...", command=self.on_list_select)
        select_button.pack(side="right")

    def pack(self, **args):
        super().pack(fill=tk.BOTH, expand=1, **args)

    def on_list_select(self):
        selection = int(self.listbox.curselection()[0])
        president = self.pres_app.presidedents_db.presidents[selection]
        self.pres_app.show_president(president)

class PresidentPanel(tk.Frame):
    def __init__(self, pres_app=None):
        super().__init__(pres_app)
        self.pres_app = pres_app
        self.make_widgets()
    
    def make_widgets(self):
        back_widget = tk.Button(text="< Back", command=self.go_back)
        back_widget.pack()
        self.text_widget = tk.Label()
        self.text_widget.pack()
    
    def president_text(self, president):
        return f"""
                {president.name} served {president.duration.days} days.\n
                He was elected by the {president.party} party.\n
                His vice president was {president.vice_president}.\n
                """

    def show(self, president):
        self.text_widget["text"] = self.president_text(president)
        self.pack()

    def go_back(self):
        self.pres_app.show_list()
 
if __name__ == "__main__":
    root = tk.Tk()
    app = PresidentsApplication(master=root)
    app.mainloop()
