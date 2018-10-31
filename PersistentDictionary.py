import os
import sys
try:
    import dill as pickle
except ModuleNotFoundError:
    import pickle

class PersistentDictionary(dict):
    
    def __init__(self, store_file, verbose=True, *args, **kwargs):
        
        self.store_file = store_file
        self.verbose = verbose
        
        if self.store_file:
            if os.path.exists(self.store_file):
                if self.verbose: print("Loading data from existing store {}".format(self.store_file))
                data_dict = self.load()
                self.update(data_dict)
            else:
                if self.verbose: print("Will create new data store {}".format(self.store_file))
                os.makedirs(os.path.dirname(self.store_file), exist_ok=True)
        else:
            print("Warining: Storage not specified.")
                
        super().__init__(*args, **kwargs)

    def __check_storage(self):
        
        if self.store_file is None:
            raise ValueError("Storage Error: self.store_file not specified.")
        
    def write(self, new_store_file=None):
        
        if new_store_file:
            self.store_file = new_store_file
        try:
            self.__check_storage()
            os.makedirs(os.path.dirname(self.store_file), exist_ok=True)
            with open(self.store_file, 'wb') as fp:
                pickle.dump(self, fp)
                if self.verbose: print("Stored data to {}".format(self.store_file))
        except:
            print("Error: Failed to write data.")
            raise
            
        return self
                
    def erase(self):
        
        if new_store_file:
            self.store_file = new_store_file
        try:
            self.__check_storage()
            with open(self.store_file, 'wb') as fp:
                pickle.dump(dict(), fp)
                if self.verbose: print("Erasing data from {}".format(self.store_file))
        except:
            print("Error: Failed to erase data.")
            raise
        return self
            
    def load(self, new_store_file=None):
        
        if new_store_file:
            self.store_file = new_store_file
        try:
            self.__check_storage()
            with open(self.store_file, 'rb') as fp:
                if self.verbose: print("Loading data from {}".format(self.store_file))
                return pickle.load(fp)
        except:
            print("Error: Failed to read data.")
            raise
        
    def load_update(self, new_store_file=None):
        
        if new_store_file:
            self.store_file = new_store_file
            
        data_dict = self.load(self.store_file)
        self.update(data_dict)
        return self
    