import pandas as pd
import os
import json
import random

class TValues():
    def __init__(self, age, gender):
        if not isinstance(age, int) or age < 16 or age > 74:
            raise ValueError("Age must be a positive integer between 16 and 74")
        if not isinstance(gender, str) or gender not in ["male", "female"]: 
            raise ValueError("Gender must be 'male' or 'female'")
        self.__age = age
        self.__gender = gender
        self.__t_val_dataframes = self.__load_data(self.__age, gender)


    def __load_data(self, age, gender):
        table_base_path = "./data"
        table_path = table_base_path + "/" + gender
        t_val_dataframe_dict = {}
       
        # list of all files in folder
        csv_files = [file for file in os.listdir(table_path) if file.endswith('.csv')]

        # read all csv and append to list
        for file in csv_files:
            filepath = os.path.join(table_path, file)
            df = pd.read_csv(filepath, delimiter=';', index_col=0)
            key = os.path.splitext(file)[0].upper() #the left part of the filename, but in uppercase...so it matches the keys from the base_results dictionary
            t_val_dataframe_dict[key] = df[str(age)]


        return t_val_dataframe_dict


    def __round_to_nearest(self, value, step=0.025):
        #the inner round makes sure that we meet the step size; the outer round truncates to 3 decimals...so the table lookup works
        return round(round(value / step) * step, 3)


    def get_t_values(self, basic_results):
        if basic_results:
            t_values_dict = {}
            t_values_dict['S'] = {}
            lookup_scales = ['AGGR', 'ANGS', 'DEPR', 'PARA', 'PHOB', 'PSYC', 'SOMA', 'UNSI', 'ZWAN']

            # Using 3 separate lookup loops, because the dict is so nested:
            for metric in lookup_scales:
                t_values_dict['S'][metric] = self.__get_single_t_value(metric, basic_results['S'][metric])

            #to avoid rounding errors, AND because the gsi is always GS/90 (no unanswered question allowed), looking up the GS value here
            t_values_dict['GSI'] = self.__get_single_t_value('GSI', basic_results['GS'])
            t_values_dict['PST'] = self.__get_single_t_value('PST', basic_results['PST'])
            #PSDI only has lookup values with 0.025 steps. Doing a bit of rounding stunts here:
            t_values_dict['PSDI'] = self.__get_single_t_value('PSDI', self.__round_to_nearest(basic_results['PSDI']))

            return t_values_dict
        else:
            return None
    
    def __get_single_t_value(self, metric, value):
        
        try:
            return int(self.__t_val_dataframes[metric].at[value])
        except KeyError:
            print(f"For {metric}, the specified entry ({value}) does not exist.")
             