# Maintain the loading and saving of objects
import pickle as pk
import os

class DataBase:

    def __init__(self, file_name, *args, load=True, **kwargs):
        self.file_name = file_name

    def save(self, data):
        with open(self.file_name, 'wb') as f:
            pk.dump(data, f)

    def load(self, *args, **kwargs):
        # TODO: Check file extension
        if os.path.exists(self.file_name):
            with open(self.file_name, 'rb') as f:
                load_obj = pk.load(f)
        else:
            load_obj = None
            # load_obj = type(self)(file_name=self.file_name, *args, load=False, **kwargs)
        return load_obj

class ArrayData(DataBase):

    def __init__(self, file_name, *args, load=True, **kwargs):
        super().__init__(file_name, *args, load=load, **kwargs)

    def load(self, *args, **kwargs):
        loaded_obj = super().load(*args, **kwargs)

        if loaded_obj is None:
            loaded_obj = []
        
        return loaded_obj
