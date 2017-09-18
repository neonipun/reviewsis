from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile,asksaveasfile
from tkinter import messagebox
import pandas
import reviewsis_module
import visualstats_module


root = Tk()
root.resizable(width=False, height=False)
Title = root.title("Reviewsis")
file_name = ""
adf = []

def open_file():
    analysis_button.config(state = NORMAL)
    #ftypes = [('CSV Files','*.csv')]
    file = askopenfile(mode='rt', filetypes=[('CSV Files','*.csv')])
    global file_name
    file_name = file.name
    if file_name:
        select_label.config(text = " CSV File Selected ")
    root.update()

def analysis():
    global adf
    print("Performing Analysis")
    analysis_content.config(text = "....Performing Analysis....")
    adf = []
    root.update()
    if not file_name:
        messagebox.showwarning("Open File", "No File Selected")
        analysis_content.config(text = "Brief Analysis Content")
        root.update()
    else:
        analysis_content.config(text = "....Performing Analysis....")
        analysis_button.config(state = DISABLED)
        root.update()
        x = reviewsis_module.perform_analysis(str(file_name))
        if x[1]:
            analysis_content.config(text = x[0])
            b1.config(state = NORMAL)
            b2.config(state = NORMAL)
            b3.config(state = NORMAL)
            adf = x[2]
            select_label.config(text = "Analysis Complete")
        else:
            analysis_content.config(text = x[0])
            
            
    root.update()

def save_analysis():
    file = asksaveasfile(mode='w', defaultextension=".csv", filetypes=[('CSV Files','*.csv')])
    print(file.name, "save file name")
    reviewsis_module.generateCSV(adf,file.name)
    root.update()
    messagebox.showinfo("Copy Brief Analysis Content", "Successfully Generated and Saved File to :\n" + file.name)

def view_stats():
    print("Viewing Stats")
    visualstats_module.show_visuals(adf)


def copy_content():
    root.clipboard_clear()
    root.clipboard_append(analysis_content['text'])
    root.update()
    messagebox.showinfo("Copy Brief Analysis Content", "Successfully Copied to Clipboard.")

def open_twitterment():
    print("Twitterment Opened")
    os.system("python Twitterment.py") 
    

    
#Defining Widgets and binding commands wherever required
select_label = ttk.Label(root, text = "Select CSV file Containing Review Content                              --->")
open_button = ttk.Button(root, text = "Open File", command = open_file)
analysis_button = ttk.Button(root, text = "Perform Sentiment Analysis", command = analysis)
analysis_content_frame = ttk.Frame(root, borderwidth=5, relief="sunken", width=500, height=300).grid(column=0, row=5, columnspan=3, rowspan=4)
analysis_content = ttk.Label(analysis_content_frame, text = "Brief Analysis Content", anchor=W, wraplength=495)
b1 = ttk.Button(root, text = "Generate and Save Analysis \n\t as CSV ", command = save_analysis, state=DISABLED)
b2 = ttk.Button(root, text = "View Visual Stats",state=DISABLED, command = view_stats)
#b3 = ttk.Button(root, text = "Save Visual Stats",state=DISABLED)
b3 = ttk.Button(root, text = "  Copy Brief Analysis \nContent to Clipboard", command = copy_content, state=DISABLED)
twitter_label = ttk.Label(root, text = "Gain insight on Twitter Tweets - ")
space = ttk.Frame(root, borderwidth=5, relief="flat", width=400, height=10).grid(column=0, row=9, columnspan=5, rowspan=2)
twitterment_button = ttk.Button(root, text = "Twitterment Window", command = open_twitterment)

#Setting Layout 
select_label.grid(column=0, row=0, columnspan=3, rowspan=2)
open_button.grid(column=3, row=0, columnspan=3, rowspan=2)
analysis_button.grid(column=1, row=3, columnspan=4, rowspan=2)
analysis_content.grid(column=0, row=5, columnspan=3, rowspan=4)
b1.grid(column=3, row=5, columnspan=3, rowspan=1)
b2.grid(column=3, row=6, columnspan=3, rowspan=1)
#b3.grid(column=3, row=7, columnspan=3, rowspan=1)
b3.grid(column=3, row=7, columnspan=3, rowspan=2)
twitter_label.grid(column=0, row=11, columnspan=3, rowspan=2)
twitterment_button.grid(column=3, row=11, columnspan=3, rowspan=2)

root.mainloop()
