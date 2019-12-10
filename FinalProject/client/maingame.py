import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *


class Maingame(object):
    def __init__(self, top=None, client=None, server=None):
        self.client = client
        self.server = server
        self.top = top
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font12 = "-family {Segoe UI} -size 72 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("797x732+607+188")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("New Toplevel")
        top.configure(background="#645cf8")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.213, rely=0.765,height=120, relwidth=0.565)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.BtnExitMenu = tk.Button(top, command=self.goToDisconnect)
        self.BtnExitMenu.place(relx=0.841, rely=0.874, height=50, width=100)
        self.BtnExitMenu.configure(activebackground="#ff6666")
        self.BtnExitMenu.configure(activeforeground="#ffffff")
        self.BtnExitMenu.configure(background="#ff0000")
        self.BtnExitMenu.configure(disabledforeground="#a3a3a3")
        self.BtnExitMenu.configure(font="-family {UD Digi Kyokasho NP-R} -size 14")
        self.BtnExitMenu.configure(foreground="#ffffff")
        self.BtnExitMenu.configure(highlightbackground="#d9d9d9")
        self.BtnExitMenu.configure(highlightcolor="black")
        self.BtnExitMenu.configure(pady="0")
        self.BtnExitMenu.configure(text='''EXIT''')

        self.LblTurn_3 = tk.Label(top)
        self.LblTurn_3.place(relx=0.376, rely=0.041, height=40, width=190)
        self.LblTurn_3.configure(activebackground="#f9f9f9")
        self.LblTurn_3.configure(activeforeground="black")
        self.LblTurn_3.configure(background="#000000")
        self.LblTurn_3.configure(disabledforeground="#a3a3a3")
        self.LblTurn_3.configure(font="-family {UD Digi Kyokasho NP-R} -size 14")
        self.LblTurn_3.configure(foreground="#ffffff")
        self.LblTurn_3.configure(highlightbackground="#d9d9d9")
        self.LblTurn_3.configure(highlightcolor="black")
        self.LblTurn_3.configure(text=self.server.get_currentmv())

        self.Button0_0 = tk.Button(top, command=lambda: self.fill_board(0 , 0, self.Button0_0))
        self.Button0_0.place(relx=0.213, rely=0.123, height=150, width=150)
        self.Button0_0.configure(activebackground="#ececec")
        self.Button0_0.configure(activeforeground="#000000")
        self.Button0_0.configure(background="#000000")
        self.Button0_0.configure(disabledforeground="#a3a3a3")
        self.Button0_0.configure(font=font12)
        self.Button0_0.configure(foreground="#ffffff")
        self.Button0_0.configure(highlightbackground="#d9d9d9")
        self.Button0_0.configure(highlightcolor="black")
        self.Button0_0.configure(pady="0")
        self.Button0_0.configure(text=self.server.get_grid(0,0).get("data"))

        self.Button0_1 = tk.Button(top, command=lambda: self.fill_board(0 , 1, self.Button0_1))
        self.Button0_1.place(relx=0.402, rely=0.123, height=150, width=150)
        self.Button0_1.configure(activebackground="#ececec")
        self.Button0_1.configure(activeforeground="#000000")
        self.Button0_1.configure(background="#000000")
        self.Button0_1.configure(disabledforeground="#a3a3a3")
        self.Button0_1.configure(font=font12)
        self.Button0_1.configure(foreground="#ffffff")
        self.Button0_1.configure(highlightbackground="#d9d9d9")
        self.Button0_1.configure(highlightcolor="black")
        self.Button0_1.configure(pady="0")
        self.Button0_1.configure(text=self.server.get_grid(0,1).get("data"))

        self.Button0_2 = tk.Button(top, command=lambda: self.fill_board(0 , 2, self.Button0_2))
        self.Button0_2.place(relx=0.59, rely=0.123, height=150, width=150)
        self.Button0_2.configure(activebackground="#ececec")
        self.Button0_2.configure(activeforeground="#000000")
        self.Button0_2.configure(background="#000000")
        self.Button0_2.configure(disabledforeground="#a3a3a3")
        self.Button0_2.configure(font=font12)
        self.Button0_2.configure(foreground="#f9f9f9")
        self.Button0_2.configure(highlightbackground="#d9d9d9")
        self.Button0_2.configure(highlightcolor="black")
        self.Button0_2.configure(pady="0")
        self.Button0_2.configure(text=self.server.get_grid(0,2).get("data"))

        self.Button1_0 = tk.Button(top, command=lambda: self.fill_board(1 , 0, self.Button1_0))
        self.Button1_0.place(relx=0.213, rely=0.314, height=150, width=150)
        self.Button1_0.configure(activebackground="#ececec")
        self.Button1_0.configure(activeforeground="#000000")
        self.Button1_0.configure(background="#000000")
        self.Button1_0.configure(disabledforeground="#a3a3a3")
        self.Button1_0.configure(font=font12)
        self.Button1_0.configure(foreground="#ffffff")
        self.Button1_0.configure(highlightbackground="#d9d9d9")
        self.Button1_0.configure(highlightcolor="black")
        self.Button1_0.configure(pady="0")
        self.Button1_0.configure(text=self.server.get_grid(1,0).get("data"))

        self.Button1_1 = tk.Button(top, command=lambda: self.fill_board(1, 1, self.Button1_1))
        self.Button1_1.place(relx=0.402, rely=0.314, height=150, width=150)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#000000")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font=font12)
        self.Button1_1.configure(foreground="#ffffff")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text=self.server.get_grid(1, 1).get("data"))

        self.Button1_2 = tk.Button(top, command=lambda: self.fill_board(1, 2, self.Button1_2))
        self.Button1_2.place(relx=0.59, rely=0.314, height=150, width=150)
        self.Button1_2.configure(activebackground="#ececec")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#000000")
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(font=font12)
        self.Button1_2.configure(foreground="#ffffff")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text=self.server.get_grid(1, 2).get("data"))

        self.Button2_0 = tk.Button(top, command=lambda: self.fill_board(2 , 0, self.Button2_0))
        self.Button2_0.place(relx=0.213, rely=0.505, height=150, width=150)
        self.Button2_0.configure(activebackground="#ececec")
        self.Button2_0.configure(activeforeground="#000000")
        self.Button2_0.configure(background="#000000")
        self.Button2_0.configure(disabledforeground="#a3a3a3")
        self.Button2_0.configure(font=font12)
        self.Button2_0.configure(foreground="#ffffff")
        self.Button2_0.configure(highlightbackground="#d9d9d9")
        self.Button2_0.configure(highlightcolor="black")
        self.Button2_0.configure(pady="0")
        self.Button2_0.configure(text=self.server.get_grid(2,0).get("data"))

        self.Button2_1 = tk.Button(top, command=lambda: self.fill_board(2 , 1, self.Button2_1))
        self.Button2_1.place(relx=0.402, rely=0.505, height=150, width=150)
        self.Button2_1.configure(activebackground="#ececec")
        self.Button2_1.configure(activeforeground="#000000")
        self.Button2_1.configure(background="#000000")
        self.Button2_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1.configure(font=font12)
        self.Button2_1.configure(foreground="#ffffff")
        self.Button2_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1.configure(highlightcolor="black")
        self.Button2_1.configure(pady="0")
        self.Button2_1.configure(text=self.server.get_grid(2,1).get("data"))

        self.Button2_2 = tk.Button(top, command=lambda: self.fill_board(2 , 2, self.Button2_2))
        self.Button2_2.place(relx=0.59, rely=0.505, height=150, width=150)
        self.Button2_2.configure(activebackground="#ececec")
        self.Button2_2.configure(activeforeground="#000000")
        self.Button2_2.configure(background="#000000")
        self.Button2_2.configure(disabledforeground="#a3a3a3")
        self.Button2_2.configure(font=font12)
        self.Button2_2.configure(foreground="#ffffff")
        self.Button2_2.configure(highlightbackground="#d9d9d9")
        self.Button2_2.configure(highlightcolor="black")
        self.Button2_2.configure(pady="0")
        self.Button2_2.configure(text=self.server.get_grid(2,2).get("data"))

        self.LblTurn_1 = tk.Label(top)
        self.LblTurn_1.place(relx=0.113, rely=0.041, height=40, width=190)
        self.LblTurn_1.configure(activebackground="#f9f9f9")
        self.LblTurn_1.configure(activeforeground="black")
        self.LblTurn_1.configure(background="#000000")
        self.LblTurn_1.configure(disabledforeground="#a3a3a3")
        self.LblTurn_1.configure(font="-family {UD Digi Kyokasho NP-R} -size 14")
        self.LblTurn_1.configure(foreground="#ffffff")
        self.LblTurn_1.configure(highlightbackground="#d9d9d9")
        self.LblTurn_1.configure(highlightcolor="black")
        if len(self.server.get_player_names()) > 0:
            self.LblTurn_1.configure(text=self.server.get_player_names()[0]+" "+self.server.get_symbol(self.server.get_player_index(self.server.get_player_names()[0])))

        self.LblTurn_2 = tk.Label(top)
        self.LblTurn_2.place(relx=0.64, rely=0.041, height=40, width=190)
        self.LblTurn_2.configure(activebackground="#f9f9f9")
        self.LblTurn_2.configure(activeforeground="black")
        self.LblTurn_2.configure(background="#000000")
        self.LblTurn_2.configure(disabledforeground="#a3a3a3")
        self.LblTurn_2.configure(font="-family {UD Digi Kyokasho NP-R} -size 14")
        self.LblTurn_2.configure(foreground="#ffffff")
        self.LblTurn_2.configure(highlightbackground="#d9d9d9")
        self.LblTurn_2.configure(highlightcolor="black")
        if len(self.server.get_player_names()) > 1:
            self.LblTurn_2.configure(text=self.server.get_player_names()[1]+" "+self.server.get_symbol(self.server.get_player_index(self.server.get_player_names()[1])))

        self.BtnExitMenu_3 = tk.Button(top, command=self.goToStart)
        self.BtnExitMenu_3.place(relx=0.841, rely=0.765, height=50, width=100)
        self.BtnExitMenu_3.configure(activebackground="#ff6666")
        self.BtnExitMenu_3.configure(activeforeground="#ffffff")
        self.BtnExitMenu_3.configure(background="#45dd04")
        self.BtnExitMenu_3.configure(disabledforeground="#a3a3a3")
        self.BtnExitMenu_3.configure(font="-family {UD Digi Kyokasho NP-R} -size 14")
        self.BtnExitMenu_3.configure(foreground="#ffffff")
        self.BtnExitMenu_3.configure(highlightbackground="#d9d9d9")
        self.BtnExitMenu_3.configure(highlightcolor="black")
        self.BtnExitMenu_3.configure(pady="0")
        self.BtnExitMenu_3.configure(text='''START''')

    def goToDisconnect(self):
        _response = self.server.remove_client(self.client.name, self.client.role)
        self.top.destroy()

    def set_all_label(self):
        self.LblTurn_3.configure(text=self.server.get_currentmv())
        self.Button0_0.configure(text=self.server.get_grid(0, 0).get("data"))
        self.Button0_1.configure(text=self.server.get_grid(0, 0).get("data"))
        self.Button0_2.configure(text=self.server.get_grid(0, 0).get("data"))
        self.Button1_0.configure(text=self.server.get_grid(0, 0).get("data"))
        self.Button1_1.configure(text=self.server.get_grid(0, 0).get("data"))
        self.Button1_2.configure(text=self.server.get_grid(0, 0).get("data"))
        self.Button2_0.configure(text=self.server.get_grid(0, 0).get("data"))
        self.Button2_1.configure(text=self.server.get_grid(0, 0).get("data"))
        self.Button2_2.configure(text=self.server.get_grid(0, 0).get("data"))
        if len(self.server.get_player_names()) > 0:
            self.LblTurn_1.configure(text=self.server.get_player_names()[0]+" "+self.server.get_symbol(self.server.get_player_index(self.server.get_player_names()[0])))
        if len(self.server.get_player_names()) > 1:
            self.LblTurn_2.configure(text=self.server.get_player_names()[1]+" "+self.server.get_symbol(self.server.get_player_index(self.server.get_player_names()[1])))



    def goToStart(self):
        _response = self.server.start_game(self.client.name)
        _message = _response.get("message")
        tk.messagebox.showinfo("TicTacToe", _message)

    def fill_board(self, y: int, x: int, button):
        _response = self.server.fill_board(self.client.name, y, x)
        _message = _response.get("message")
        _code = _response.get("code")
        self.set_all_label()
        if _code == '201':
            tk.messagebox.showinfo("TicTacToe", _response)
        if _code == "202":
            # ntar taro broadcasting buat clear board disini
            pass

    def get_spectators(self):
        spectators_list = self.server.get_spectator_only()
        print(spectators_list)
        for x in spectators_list:
            self.Entry1.insert(tk.END, x)