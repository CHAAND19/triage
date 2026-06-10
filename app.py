
import tkinter as tk
from triworx.ui.triworx_gui import TriWorXGUI

def launch():
    root = tk.Tk()
    TriWorXGUI(root)
    root.mainloop()

if __name__ == "__main__":
    launch()
