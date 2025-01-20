from data.scales import *

class Survey():

    def __init__(self, answers):
        self.__number_of_answers = len(answers)
        if len(answers) == 90:
            self.__answers_dict = self.__generate_answers_dict(answers)
        
    def __generate_answers_dict(self, answers):
        #...marrying the scales to the actual answers here:
        result_dict = {}

        for scale in scales:   #comes from scales.py
            answers_per_scale = []
            for i in scales[scale]:
                answers_per_scale.append(answers[i-1])

            result_dict[scale] = answers_per_scale


        return result_dict

    #Metric 1: Sum per scale
    def __get_sum_per_scale(self):
        result_dict = {}
        for scale in self.__answers_dict:
            result_dict[scale] = sum(self.__answers_dict[scale])
        return result_dict
    
    #Metric 2: "Scale Value" = Average. As per manual, not for items in "ZUSATZ"
    def __get_average_per_scale(self):
        result_dict = {}
        for scale in self.__answers_dict:
            if scale != "ZUSATZ":
                result_dict[scale] = sum(self.__answers_dict[scale])/float(len(scale))

        return result_dict
    
    #Metric 3: # of answers > 0
    def __get_items_greater_zero_per_scale(self):
        result_dict = {}

        for scale in self.__answers_dict:
            no_of_items = 0
            for item in self.__answers_dict[scale]: #"scale" would just return the key, we need the values
                if item > 0:
                    no_of_items += 1

            result_dict[scale] = no_of_items
                
        return result_dict


    def __get_psdi(self, gs, pst):
        if pst != 0:
            return gs/pst
        else:
            return 0.0 #no exception, so caller can display nice values


    def get_basic_results(self):
        if self.__number_of_answers == 90:
            gs = sum(self.__get_sum_per_scale().values())
            pst = sum(self.__get_items_greater_zero_per_scale().values())
            result_dict = {
                "S":    self.__get_sum_per_scale(),
                "G":    self.__get_average_per_scale(),
                "P":    self.__get_items_greater_zero_per_scale(),
                "GS":   gs,
                "GSI":  sum(self.__get_sum_per_scale().values())/self.__number_of_answers,
                "PST":  pst,
                "PSDI": self.__get_psdi(gs, pst)
            }
            return result_dict
        else:
            return None

def scales_gte(t_values, value):
    #t_values is a dict of t values, sublist "S" contains the scales
    return list(filter(lambda x: x >= value, t_values['S'].values()))