from ctypes import CDLL
import tkinter as tk
import os
so_file_path=os.getcwd()+"\cal.so"
so_file=CDLL(so_file_path)
def printcalendar():
    T.config(state="normal")
    T.delete(1.0,"end")
    year=int(d.get())
    so_file.printCalendar(year)
    f=open("calendar_text.txt","r")
    a=f.read()
    t=tk.StringVar()
    t.set(a)
    T.insert(tk.END,a)
    T.config(state="disabled")
root=tk.Tk()
d=tk.StringVar()
tk.Entry(root,textvariable=d,font=("Lucida Console",20,"bold")).pack(side="top",pady=10,ipady=10)
tk.Button(root,text="Print",command=printcalendar,font=("Lucida Console",20,"bold")).pack(side="top",pady=10)
T=tk.Text(root,font=("Lucida Console",20,"bold"),bg="yellow",height=50,width=37)
T.pack(side="top",pady=10)
root.geometry("700x500")
root.title("Calendar")
root.resizable(0,0)
root.mainloop()
