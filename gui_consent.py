import tkinter, sys, os
import subprocess, shlex
from tkinter import Toplevel, Canvas, Button
#from PIL import Image


def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)


m = tkinter.Tk()
m.title("Mouse Tunnel")

# DEFAULTS
mouseID_ = 'Enter Mouse ID'
rewardVolume_ = '10'
rewardWindow_ = '1.0'
script_path_ = os.getcwd()
script_ = 'mouse_tunnel_base_2AFC.py'


def mouseID_callback():
    mouseID_ = mouseID_s.get()


L1 = tkinter.Label(m, text="Mouse ID")
L1.grid(row=0, column=0)
mouseID_s = tkinter.StringVar(value=mouseID_)
mouseID = tkinter.Entry(m, text='Mouse ID', textvariable=mouseID_s,
                        validate="focusout", validatecommand=mouseID_callback)
mouseID.grid(row=0, column=1)


def rewardVolume_callback():
    rewardVolume_ = rewardVolume_s.get()


L2 = tkinter.Label(m, text="Reward Vol (uL)")
L2.grid(row=1, column=0)
rewardVolume_s = tkinter.StringVar(value=rewardVolume_)
rewardVolume = tkinter.Entry(m, text='Reward Volume', textvariable=rewardVolume_s,
                             validate="focusout", validatecommand=rewardVolume_callback)
rewardVolume.grid(row=1, column=1)

L3 = tkinter.Label(m, text="Reward Window (s)")
L3.grid(row=2, column=0)
rewardWindow_s = tkinter.StringVar(value=rewardWindow_)
rewardWindow = tkinter.Entry(m, text='Reward Window', textvariable=rewardWindow_s,
                             validate="focusout", validatecommand=rewardVolume_callback)
rewardWindow.grid(row=2, column=1)


def script_path_callback():
    mouseID_ = mouseID_s.get()


L4 = tkinter.Label(m, text="Script Path")
L4.grid(row=0, column=0)
script_path_s = tkinter.StringVar(value=script_path_)
script_path = tkinter.Entry(m, text='Script Path', textvariable=script_path_s,
                            validate="focusout", validatecommand=script_path_)
script_path.grid(row=3, column=1)


def script_callback():
    mouseID_ = mouseID_s.get()


L5 = tkinter.Label(m, text="Script Name")
L5.grid(row=0, column=0)
script_s = tkinter.StringVar(value=script_)
script = tkinter.Entry(m, text='Script Name', textvariable=script_s,
                       validate="focusout", validatecommand=script_path_)
script.grid(row=4, column=1)


def create_consent():
    top = Toplevel()
    top.title("Consent Form")
    top.minsize(width=860, height=900)

    canvas = Canvas(top, width=860, height=900)
    canvas.pack()
    img = tkinter.PhotoImage(file='consent_form.png')

    canvas.create_image(430, 475, image=img)
    canvas.image = img

    button = Button(top, text="Accept", command=lambda: accept_consent(top))
    button.pack()

    button = Button(top, text="Reject", command=lambda: reject_consent(top))
    button.pack()


def accept_consent(top):
    top.destroy

    print('activate panda3d;\
    #    cd C:\github\mouse_tunnel;\
    cd ' + script_path.get() + ';' \
                               'python ' + script.get() + ' ' + mouseID_s.get() + ' ' + rewardVolume_s.get() + ' ' + rewardWindow_s.get())
    subprocess_cmd('activate panda3d')
    subprocess_cmd('cd ' + script_path.get())
    subprocess_cmd(
        'python ' + script.get() + ' ' + mouseID_s.get() + ' ' + rewardVolume_s.get() + ' ' + rewardWindow_s.get())


def reject_consent(top):
    top.destroy
    sys.exit(0)


def button_callback():
    create_consent()


startButton = tkinter.Button(m, text='START', bg='green', command=button_callback)
startButton.grid(row=3, columnspan=1)

m.mainloop()