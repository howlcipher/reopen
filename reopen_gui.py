from ast import Lambda
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import ttk
from tracemalloc import stop
from reopen import application_reopen


def save():
    tk.messagebox.showinfo('Configuration Saved', 'Configuration Saved')

root = Tk()
root.title('Reopen')
root.resizable(False, False)
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Applications to Reopen").grid(columnspan=2, column=0, row=0)
ttk.Button(frm, text="Save", command=save).grid(column=2, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=0)

entry1 = tk.StringVar()
ttk.Entry(frm, textvariable=entry1).grid(columnspan=2, column=0, row=1, padx=4, pady=4)

entry2 = tk.StringVar()
ttk.Entry(frm, textvariable=entry2).grid(columnspan=2, column=0, row=2, padx=4, pady=4)

entry3 = tk.StringVar()
ttk.Entry(frm, textvariable=entry3).grid(columnspan=2, column=0, row=3, padx=4, pady=4)

entry4 = tk.StringVar()
ttk.Entry(frm, textvariable=entry4).grid(columnspan=2, column=0, row=4, padx=4, pady=4)

app1 = application_reopen('NONE')
app2 = application_reopen('NONE')
app3 = application_reopen('NONE')
app4 = application_reopen('NONE')

class gui_app:
    def __init__(self, application):
        self.app = application
        print('app created')

    def start(self, entry):
        print('start')
        value = entry.get()
        self.app.application = value
        self.app.loop()

    def stop(self, entry):
        print('end')
        value = entry.get()
        self.app.application = value
        self.app.endloop()

gui_app1 = gui_app(app1)
gui_app2 = gui_app(app2)
gui_app3 = gui_app(app3)
gui_app4 = gui_app(app4)

ttk.Button(frm, text="Start", command= lambda: gui_app1.start(entry1)).grid(column=2, row=1, padx=4, pady=4)
ttk.Button(frm, text="Stop", command= lambda: gui_app1.stop(entry1)).grid(column=3, row=1, padx=4, pady=4)
ttk.Label(frm, textvariable= entry1).grid(column=4, row=1, padx=4, pady=4)


ttk.Button(frm, text="Start", command= lambda: gui_app2.start(entry2)).grid(column=2, row=2, padx=4, pady=4)
ttk.Button(frm, text="Stop", command= lambda: gui_app2.stop(entry2)).grid(column=3, row=2, padx=4, pady=4)
ttk.Label(frm, textvariable= entry2).grid(column=4, row=2, padx=4, pady=4)

ttk.Button(frm, text="Start", command= lambda: gui_app3.start(entry3)).grid(column=2, row=3, padx=4, pady=4)
ttk.Button(frm, text="Stop", command= lambda: gui_app3.stop(entry3)).grid(column=3, row=3, padx=4, pady=4)
ttk.Label(frm, textvariable= entry3).grid(column=4, row=3, padx=4, pady=4)

ttk.Button(frm, text="Start", command= lambda: gui_app4.start(entry4)).grid(column=2, row=4, padx=4, pady=4)
ttk.Button(frm, text="Stop", command= lambda: gui_app4.stop(entry4)).grid(column=3, row=4, padx=4, pady=4)
ttk.Label(frm, textvariable= entry4).grid(column=4, row=4, padx=4, pady=4)

root.mainloop()