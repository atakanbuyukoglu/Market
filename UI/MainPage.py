import tkinter as tk
from . import Base as B
from .CompanyPages import CompaniesPage

class MainPage(B.Frame):
    def __init__(self, master: B.Container):
        # First init
        super().__init__(master)

        # Buttons
        self.quit_button = None
        self.companies_button = None

        # Configuration
        # self.pack(fill='both')
        self.grid(row=0, column=0, sticky='nsew')
        self.create_widgets()

    def create_widgets(self):

        self.companies_button = tk.Button(master=self, text='Companies', command=self.companies_button_cb)
        self.companies_button.pack(side='top')

        self.quit_button = tk.Button(master=self, text='Quit', command=self.destroy_root)
        self.quit_button.pack(side='top')

    def companies_button_cb(self):
        self.master.show_frame(CompaniesPage)


# The Root Module
class RootPage(tk.Tk):

    def __init__(self, *args, **kwargs):
        # First init
        tk.Tk.__init__(self, *args, **kwargs)
        self.master = None

        # Frame container to keep track of page history
        self.container = B.Container(master=self)
        self.container.show_frame(MainPage)

        self.start_ui(window_size='400x400')

    def start_ui(self, title=None, window_size=None):
        # Set the window size
        if window_size is None:
            sc_width = self.winfo_screenwidth()-100
            sc_height = self.winfo_screenheight()-100
            sc_fullscreen = str(sc_width) + 'x' + str(sc_height)
            self.geometry(newGeometry=sc_fullscreen)
        else:
            self.geometry(newGeometry=window_size)
        # Set the title
        if title is None:
            self.title('Root')
        else:
            self.title(title)

    def destroy_root(self):
        self.destroy()
