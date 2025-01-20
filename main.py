import random, json
from survey import * 
from t_values import *


def generate_static_sample(length, value):
    output_list = []
    for i in range(length):
        output_list.append(value)
    return output_list

def generate_random_sample(length):
    

    output_list = []
    for i in range(length):
        output_list.append(random.choice(possible_answers))

    return output_list


def get_verdict(t_value):
    match t_value:
        case _ if 60 <= t_value <= 64:
            return "leicht erhöht"
        case _ if 65 <= t_value <= 69:
            return "deutlich erhöht"
        case _ if 70 <= t_value <= 74:
            return "stark erhöht"
        case _ if 75 <= t_value <= 80:
            return "sehr stark erhöht"
        case _:
            return "unauffällig"


def get_evaluation(t_values):
    results = {}
    results['S'] = {}
    #t_values is a dict of t values
    #trying to implement a bit of a pipeline pattern here...no need to make an entire class for this 

    if t_values["GSI"] >= 63 or len(scales_gte(t_values, 63)) > 2:
        results["Fall gemäß Falldefinition"] = f"Fall liegt vor, GSI {get_verdict(t_values["GSI"])}"
    else:
        results["Fall gemäß Falldefinition"] = "Fall liegt nicht vor"

    if t_values["GSI"] >= 60 and t_values["PSDI"] >= 60 and t_values["PST"] >= 60:
        results["Analyse der globalen Kennwerte"] = f"Globale Kennwerte auffällig, GSI {get_verdict(t_values["GSI"])}, PSDI {get_verdict(t_values["PSDI"])}, PST {get_verdict(t_values["PST"])}"
    else:
        results["Analyse der globalen Kennwerte"] = "Globale Kennwerte unauffällig"

    if len(scales_gte(t_values, 60)) >= 1:
        results["Analyse der neun Skalen"] = "Eine oder mehr Skalen auffällig"
    else:
        results["Analyse der neun Skalen"] = "Alle Skalen unauffällig"

    for scale in t_values['S']:
        results["S"][scale] = get_verdict(t_values['S'][scale])


    return results


def main():

    #generating sample answers so we have some output
    
    answers_list = generate_static_sample(sample_length, 4) 
    #answers_list = generate_static_sample(sample_length, random.choice(possible_answers))
    #answers_list = generate_random_sample(sample_length)

    survey = Survey(answers_list)
    
    basic_results = survey.get_basic_results()
    print(json.dumps(basic_results, indent=4))
    print("\nBerechnung der T-Werte\n----------------------------")
    #random age 16-74, random gender male/female...to test the data lookups
    test_age = random.randint(16, 74)
    test_gender = random.choice(possible_genders) 
    t_values = TValues(test_age, test_gender) 
    t_values_dict = t_values.get_t_values(basic_results)
    print(json.dumps(t_values_dict, indent=4))
    print("\nAuswertung\n----------------------------")
    print(f"Alter: {test_age} Geschlecht: {test_gender}")
    print(json.dumps(get_evaluation(t_values_dict), indent=4, ensure_ascii=False))


possible_answers = [0, 1, 2, 3, 4]
possible_genders = ["male", "female"]
sample_length = 90

main()