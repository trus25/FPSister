import tkinter as tk
from FinalProject.client.maingame import Maingame
import Pyro4

class Regis(object):
    def __init__(self, top=None, client=None):
        self.top = top
        self.client = client
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {UD Digi Kyokasho NP-R} -size 28 -weight " \
                 "normal -slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 20 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"

        top.geometry("797x712+607+188")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("Tic Tac Toe")
        top.configure(background="#645cf8")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.EntryNama = tk.Entry(top)
        self.EntryNama.place(relx=0.326, rely=0.267, height=40, relwidth=0.314)
        self.EntryNama.configure(background="white")
        self.EntryNama.configure(disabledforeground="#a3a3a3")
        self.EntryNama.configure(font="TkFixedFont")
        self.EntryNama.configure(foreground="#000000")
        self.EntryNama.configure(insertbackground="black")
        self.EntryNama.insert(0, self.client.name)


        self.EntryAddr = tk.Entry(top)
        self.EntryAddr.place(relx=0.326, rely=0.435, height=40, relwidth=0.314)
        self.EntryAddr.configure(background="white")
        self.EntryAddr.configure(disabledforeground="#a3a3a3")
        self.EntryAddr.configure(font="TkFixedFont")
        self.EntryAddr.configure(foreground="#000000")
        self.EntryAddr.configure(highlightbackground="#d9d9d9")
        self.EntryAddr.configure(highlightcolor="black")
        self.EntryAddr.configure(insertbackground="black")
        self.EntryAddr.configure(selectbackground="#c4c4c4")
        self.EntryAddr.configure(selectforeground="black")
        self.EntryAddr.insert(0, self.client.address)

        self.LblNama = tk.Label(top)
        self.LblNama.place(relx=0.326, rely=0.211, height=40, width=250)
        self.LblNama.configure(background="#645cf8")
        self.LblNama.configure(disabledforeground="#a3a3a3")
        self.LblNama.configure(font=font9)
        self.LblNama.configure(foreground="#000000")
        self.LblNama.configure(text='''Username''')

        self.LblAddress = tk.Label(top)
        self.LblAddress.place(relx=0.326, rely=0.379, height=40, width=250)
        self.LblAddress.configure(activebackground="#f9f9f9")
        self.LblAddress.configure(activeforeground="black")
        self.LblAddress.configure(background="#645cf8")
        self.LblAddress.configure(disabledforeground="#a3a3a3")
        self.LblAddress.configure(font="-family {Segoe UI} -size 20")
        self.LblAddress.configure(foreground="#000000")
        self.LblAddress.configure(highlightbackground="#d9d9d9")
        self.LblAddress.configure(highlightcolor="black")
        self.LblAddress.configure(text='''Host Name''')

        self.BtnGo = tk.Button(top,command=self.get_atribute)
        self.BtnGo.place(relx=0.389, rely=0.632, height=80, width=150)
        self.BtnGo.configure(activebackground="#51ff51")
        self.BtnGo.configure(activeforeground="#ffffff")
        self.BtnGo.configure(background="#00ff00")
        self.BtnGo.configure(borderwidth="0")
        self.BtnGo.configure(disabledforeground="#a3a3a3")
        self.BtnGo.configure(font=font10)
        self.BtnGo.configure(foreground="#ffffff")
        self.BtnGo.configure(highlightbackground="#d9d9d9")
        self.BtnGo.configure(highlightcolor="black")
        self.BtnGo.configure(pady="0")
        self.BtnGo.configure(text='''GO!''')

    def connect(self, name, address):
        self.client.role = "1"
        _uri = "PYRONAME:game_server@" + self.client.address + ":7777"
        _server = Pyro4.Proxy(_uri)
        _response = _server.register_client(self.client.name, self.client.role)
        self.client.name = _response.get("data")
        root = tk.Tk()
        Maingame(root, self.client, _server)
        self.top.destroy()
        return _uri, _server, _response

    def get_atribute(self):
        self.client.name = self.EntryNama.get()
        self.client.address = self.EntryAddr.get()
        self.connect(self.client.name,self.client.address)


