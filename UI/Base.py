import tkinter as tk


class Frame(tk.Frame):

    def __init__(self, master, cnf=None, **kw):
        # First init
        if cnf is None:
            cnf = {}
        super(Frame, self).__init__(master=master, cnf=cnf, **kw)
        self.master = master
        self.name = type(self).__name__

    def show(self):
        self.tkraise()
        print(self.name)

    def destroy_root(self):
        self.master.destroy_root()


class Container(Frame):
    def __init__(self, master):
        # First init
        super(Container, self).__init__(master)
        self.master = master
        # Frames
        self.frame_queue = []
        self.prev_frame = None
        self.current_frame = None

        # Configuration
        self.pack(anchor='center', expand=True)

    def _add_frame(self, frame, *args, **kwargs):
        # Check the class input
        assert issubclass(frame, Frame)
        # Add the frame
        self.frame_queue.append(frame(master=self, *args, **kwargs))

    def _remove_frame(self, key):
        self.frame_queue.pop(key)

    def show_frame(self, frame, *args, **kwargs):
        self._add_frame(frame, *args, **kwargs)
        self.frame_queue[-1].show()

    def show_back_frame(self):
        self.frame_queue.pop()
        self.frame_queue[-1].show()




class Entry(tk.Label):

    def __init__(self, master, text):
        super(Entry, self).__init__(master=master)
        self.master = master

        # Widget Init
        self.entry_label = None
        self.entry_label_text = text
        self.entry_field = None

        # Configuration
        self.create_widgets()

    def create_widgets(self):
        self.entry_label = tk.Label(master=self, text=self.entry_label_text)
        self.entry_label.grid(row=0, column=0, sticky='W')

        self.entry_field = tk.Entry(master=self)
        self.entry_field.grid(row=0, column=1, sticky='W')

    def __getattr__(self, item):
        return getattr(self.entry_field, item)


