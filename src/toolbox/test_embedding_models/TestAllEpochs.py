# IMPORTS ######################################################################
import os
from .TestOneEpoch import TestOneEpoch
import pandas as pd
# SCRIPTS ######################################################################
class TestAllEpochs:
    """
    """
    def __init__(self, foldername) -> None:
        """
        """
        self.__foldername : str = foldername
        self.__n_epochs : int = len(
            [f for f in os.listdir(foldername) if f.startswith("checkpoint")])
        self.__results : list[dict] = []

    def run_tests(self, device : str|None = None, additional_tags : dict = {}):
        """
        """
        for epoch in range(self.__n_epochs) : 
            self.__results.append(
                TestOneEpoch(self.__foldername, epoch, device).\
                    routine(additional_tags)
            )
    
    def save_results(self, filename : str):
        """
        """
        try : 
            df = pd.read_csv(f"{filename}")
            df = pd.concat((df, pd.DataFrame(self.__results)))
        except:
            df = pd.DataFrame(self.__results)
        finally:
            df.to_csv(f"{filename}", index = False)
    
    def routine(self, filename : str, device : str|None = None, 
        additional_tags : dict = {}):
        """
        """
        self.run_tests(device,additional_tags)
        try:
            self.save_results(filename) 
        except Exception as e:
            raise ValueError(f"Test All Epochs failed saving.\n\nError:\n{e}")