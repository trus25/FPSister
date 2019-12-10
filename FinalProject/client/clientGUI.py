import tkinter as tk
from FinalProject.client.regis import Regis

class Clientdat(object):
    def __init__(self):
        self.name = "player"
        self.role = "1"
        self.address = "127.0.0.1"

def main():
    root = tk.Tk()
    client = Clientdat()
    Regis(root, client)
    root.mainloop()


if __name__ == '__main__':
    main()