#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 10, 2019 11:28:45 AM +07  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font15 = "-family {Segoe UI} -size 48 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font18 = "-family {UD Digi Kyokasho NP-R} -size 24 -weight "  \
            "bold -slant roman -underline 0 -overstrike 0"

        top.geometry("797x652+607+188")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("Tic Tac Toe")
        top.configure(background="#645cf8")

        self.BtnStart = tk.Button(top)
        self.BtnStart.place(relx=0.263, rely=0.69, height=80, width=160)
        self.BtnStart.configure(activebackground="#51ff51")
        self.BtnStart.configure(activeforeground="#ffffff")
        self.BtnStart.configure(background="#00ff00")
        self.BtnStart.configure(borderwidth="0")
        self.BtnStart.configure(disabledforeground="#a3a3a3")
        self.BtnStart.configure(font=font18)
        self.BtnStart.configure(foreground="#ffffff")
        self.BtnStart.configure(highlightbackground="#d9d9d9")
        self.BtnStart.configure(highlightcolor="black")
        self.BtnStart.configure(pady="0")
        self.BtnStart.configure(text='''START''')

        self.BtnExit = tk.Button(top)
        self.BtnExit.place(relx=0.502, rely=0.69, height=80, width=160)
        self.BtnExit.configure(activebackground="#ff6666")
        self.BtnExit.configure(activeforeground="#ffffff")
        self.BtnExit.configure(background="#ff0000")
        self.BtnExit.configure(borderwidth="0")
        self.BtnExit.configure(disabledforeground="#a3a3a3")
        self.BtnExit.configure(font=font18)
        self.BtnExit.configure(foreground="#ffffff")
        self.BtnExit.configure(highlightbackground="#d9d9d9")
        self.BtnExit.configure(highlightcolor="black")
        self.BtnExit.configure(padx="11")
        self.BtnExit.configure(pady="0")
        self.BtnExit.configure(text='''EXIT''')

        self.TitleLabel = tk.Label(top)
        self.TitleLabel.place(relx=0.251, rely=0.092, height=161, width=384)
        self.TitleLabel.configure(background="#645cf8")
        self.TitleLabel.configure(disabledforeground="#a3a3a3")
        self.TitleLabel.configure(font=font15)
        self.TitleLabel.configure(foreground="#000000")
        self.TitleLabel.configure(text='''Tic Tac Toe''')

if __name__ == '__main__':
    vp_start_gui()





