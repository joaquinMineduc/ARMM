import pandas as pd
import numpy as np
import math as mat


class Analitics:
    
    def __init__(self, save_location, origin_location):
        self.save_location = save_location
        self.origin_location = origin_location
        self.agent_manipulation = pd
        self.agent_one = np
        self.agent_second = mat
        self.dataFrame = self.create_dataFrame()
        
    def create_dataFrame(self):
        df = self.agent_manipulation.read_excel(self.origin_location, header = 1)
        return df
        
    def create_an_copy(self, df, columns):
        print(df)
        df_copy = df[[columns]].copy()
        return df_copy
    
    
    def split_columns(self, df, columns):
        list_a = []
        list_b = []
        df_filtrated = self.create_an_copy(df, columns)
        for col in df_filtrated:
            parts = col.split(']')
            code = parts[0]
            nom_indicador = parts[1]
            value = value.replace('[','')
            list_a.append(code)
            list_b.append(nom_indicador)
            
    def modificator_columns(df, column, list):
        df.loc[:,column] = list
        return df