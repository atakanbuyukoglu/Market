import tkinter as tk
from . import Base as B

class CompaniesPage(B.Frame):

    def __init__(self, master: B.Container, cnf=None, **kw):
        # First init
        super().__init__(master, cnf, **kw)

        # Buttons
        self.company_buttons = []

        # Configuration
        # self.pack(fill='both')
        self.grid(row=0, column=0, sticky='nsew')
        self.create_widgets()

    def create_widgets(self):
        # TODO: Connect database to here for buttons
        pass

