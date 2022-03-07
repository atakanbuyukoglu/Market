import tkinter as tk
from . import Base as B
import pickle as pk
from .src.Company import PublicCompany
from .src.DataBase import ArrayData
from .src.Const import COMPANIES_FILE


class CompaniesPage(B.Frame):

    def __init__(self, master: B.Container, cnf=None, **kw):
        # First init
        super().__init__(master, cnf, **kw)

        # Data Load
        self.company_data = ArrayData(file_name=COMPANIES_FILE)
        self.companies = self.company_data.load()

        # Buttons
        self.company_buttons = {}
        self.add_company_button = None

        # Configuration
        # self.pack(fill='both')
        self.grid(row=0, column=0, sticky='nsew')
        self.create_widgets()

    def create_widgets(self):
        # TODO: Connect database to here for buttons
        for company in self.companies:
            button = tk.Button(master=self, text=company.ticker, command=lambda: self.company_button_cb(company))
            button.pack(side='top')
            self.company_buttons[company.ticker] = button
        self.add_company_button = tk.Button(master=self, text='Add New Company', command=self.add_company_cb)
        self.add_company_button.pack(side='top')

    def company_button_cb(self, company):
        self.master.show_frame(CompanyPage, company)

    def add_company_cb(self):
        self.master.show_frame(AddCompanyPage)


class CompanyPage(B.Frame):

    def __init__(self, master, company: PublicCompany, cnf=None, **kw):
        super().__init__(master, cnf, **kw)
        self.company = company

        # Labels
        self.company_label = None

        # Configuration
        # self.pack(fill='both')
        self.grid(row=0, column=0, sticky='nsew')
        self.create_widgets()        

    def create_widgets(self):
        self.company_label = tk.Label(master=self, text=self.company.ticker)
        self.company_label.pack(side='top')

class AddCompanyPage(B.Frame):

    def __init__(self, master, cnf=None, **kw):
        super().__init__(master, cnf, **kw)

        # Entries
        self.name_entry = None
        self.ticker_entry = None

        # Buttons
        self.add_button = None


        # Configuration
        # self.pack(fill='both')
        self.grid(row=0, column=0, sticky='nsew')
        self.create_widgets()   


    def create_widgets(self):
        self.name_entry = B.Entry(master=self, text='Name:')
        self.name_entry.pack(side='top')

        self.ticker_entry = B.Entry(master=self, text='Ticker')
        self.ticker_entry.pack(side='top')

        self.add_button = tk.Button(master=self, text='Add', command=self.add_company)
        self.add_button.pack(side='top')

    def add_company(self):
        company_data = ArrayData(COMPANIES_FILE)
        companies = company_data.load()

        name = self.name_entry.get()
        ticker = self.ticker_entry.get()
        company = PublicCompany(name=name, ticker=ticker)

        companies.append(company)
        company_data.save(companies)
        


