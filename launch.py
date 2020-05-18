import tkinter, sys, os
import subprocess, shlex
from tkinter import Toplevel, Canvas, Button, Scrollbar,Frame, HORIZONTAL, SUNKEN, E, N, S, W
#from PIL import Image


def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)


m = tkinter.Tk()
m.title("Cheetah or Elephant?")
m.geometry("400x300+100+100")


# DEFAULTS
script_path_ = os.getcwd()
script_ = 'mouse_tunnel_base_2AFC.py'

# scrollbar = Scrollbar(m)
# scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)



def mouseID_callback():
    mouseID_ = mouseID_s.get()



def script_path_callback():
    mouseID_ = mouseID_s.get()


L4 = tkinter.Label(m, text="Script Path")
L4.grid(row=0, column=0)
script_path_s = tkinter.StringVar(value=script_path_)
script_path = tkinter.Entry(m, text='Script Path', textvariable=script_path_s,
                            validate="focusout", validatecommand=script_path_)
script_path.grid(row=0, column=1)


def script_callback():
    mouseID_ = mouseID_s.get()


L5 = tkinter.Label(m, text="Script Name")
L5.grid(row=1, column=0)
script_s = tkinter.StringVar(value=script_)
script = tkinter.Entry(m, text='Script Name', textvariable=script_s,
                       validate="focusout", validatecommand=script_path_)
script.grid(row=1, column=1)


def create_consent():
    top = Toplevel(m)
    top.title("Consent Form")
    top.geometry("600x600+100+100")

    frame = Frame(top, bd=2, relief=SUNKEN)
    xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
    xscrollbar.grid(row=1, column=0, sticky=E+W)

    yscrollbar = Scrollbar(frame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
   
    canvas = Canvas(frame, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)

    # File = "consent_form.png"
    img = tkinter.PhotoImage(file='consent_form.png')
    canvas.create_image(430,475,image=img, anchor="nw")

    xscrollbar.config(command=canvas.xview)
    yscrollbar.config(command=canvas.yview)

    # canvas = Canvas(frame, width=600, height=600)
    # canvas.pack()
    # img = tkinter.PhotoImage(file='consent_form.png')

    # canvas.create_image(430, 475, image=img)
    # canvas.image = img

    button = Button(top, text="Accept", command=lambda: accept_consent(top))
    button.pack()

    button = Button(top, text="Reject", command=lambda: reject_consent(top))
    button.pack()


def accept_consent(top):
    top.destroy()
    subprocess_cmd('cd ' + script_path.get())
    subprocess_cmd('python ' + script.get() )


def reject_consent(top):
    top.destroy
    sys.exit(0)


def button_callback():
    create_consent()


startButton = tkinter.Button(m, text='START', activebackground='green',background='green',highlightbackground='green', command=button_callback)
startButton.place( x=20, y = 100)
startButton.config(width=40, height=10)
startButton.flash()

m.mainloop()