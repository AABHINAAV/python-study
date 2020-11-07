import tkinter as tk
from tkinter import ttk,messagebox as mbox
from pytube import YouTube

root= tk.Tk()
root.title('youtube downloader')
root.geometry('1200x700')

tk.Label(root,text='youtube video downloader',font='arial 40 bold',bg='yellow',fg='red').pack(side=tk.TOP,pady=20)

status_lbl = tk.Label(root,text='enter the link',font='airal 20 bold',fg='green')
status_lbl.pack(side=tk.TOP,pady=20)

entry_box= tk.Entry(root,font='arial 20 normal',fg='red')
entry_box.pack(side=tk.TOP,pady=20)

btn = tk.Button(root,text='download',font='arial 20 bold',fg='crimson',bg='lime')
btn.pack(side=tk.TOP,pady=20)



# functionality:-
def download_video():
    link = entry_box.get()
    if link == '':
        mbox.showerror('error','please enter the link')
    else:
        try:
            status_lbl.set('downloading')
            Youtube(link).streams.first().download()
            mbox.showinfo('complete','downloading complete')
            status_lbl.set('enter the link')
            entry_box.set('')
        except:
            root.update()
            mbox.showerror('error','please enter the valid link')
            status_lbl.set('enter the link')
            entry_box.set('')
btn['command']=download_video


root.mainloop()