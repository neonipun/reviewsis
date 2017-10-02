from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
import pandas
import twitterment_module
import visualstats_module

root = Tk()
Title = root.title("Twitterment")
rdf = []

def search():
    root.update()
    global rdf
    rdf = []
    search_text = search_textbox.get()
    if not search_text:
        messagebox.showwarning("Text Entry", "No Search term entered")
    else:
        print("Performing Analysis")
        analysis_content.config(text = "....Performing Analysis....")
        root.update()
        x = twitterment_module.perform_analysis(search_text)
        analysis_content.config(text = x[0] )
        if x[1]:
            b1.config(state = NORMAL)
            b2.config(state = NORMAL)
            b3.config(state = NORMAL)
            rdf = x[2]
            print(rdf)
        root.update()
                

def save_analysis():
    file = asksaveasfile(mode='w', defaultextension=".csv", filetypes=[('CSV Files','*.csv')])
    print(file.name, "save file name")
    twitterment_module.generateCSV(rdf,file.name)
    root.update()
    messagebox.showinfo("Copy Brief Analysis Content", "Successfully Generated and Saved File to :\n" + file.name)

def view_stats():
    print("Viewing Stats")
    visualstats_module.show_visuals(rdf)

def copy_content():
    root.clipboard_clear()
    root.clipboard_append(analysis_content['text'])
    root.update()
    messagebox.showinfo("Copy Brief Analysis Content", "Successfully Copied to Clipboard.")


        
#Defining Widgets and binding commands wherever required
search_textbox = ttk.Entry(root)
search_button = ttk.Button(root, text = "Search & Perform Sentiment Analysis", command = search)
analysis_content_frame = ttk.Frame(root, borderwidth=5, relief="sunken", width=500, height=300).grid(column=0, row=5, columnspan=3, rowspan=4)
analysis_content = ttk.Label(analysis_content_frame, text = "Brief Analysis Content", anchor=W, wraplength=495)
b1 = ttk.Button(root, text = "Generate and Save Analysis \n\t as CSV ", command = save_analysis, state=DISABLED)
b2 = ttk.Button(root, text = "View Visual Stats",state=DISABLED, command = view_stats)
b3 = ttk.Button(root, text = "  Copy Brief Analysis \nContent to Clipboard", command = copy_content, state=DISABLED)

#Setting Layout 
search_textbox.grid(column=1, row=0, columnspan=4, rowspan=2)
search_button.grid(column=1, row=3, columnspan=4, rowspan=2)
analysis_content.grid(column=0, row=5, columnspan=3, rowspan=4)
b1.grid(column=3, row=5, columnspan=3, rowspan=1)
b2.grid(column=3, row=6, columnspan=3, rowspan=1)
b3.grid(column=3, row=7, columnspan=3, rowspan=2)

root.mainloop()
