from survey import Survey
import pytest

def generate_static_sample(length, value):
    output_list = []
    for i in range(length):
        output_list.append(value)
    return output_list

def test_empty_survey():
    survey = Survey([])
    result = survey.get_basic_results()
    assert result is None

def test_static_survey_all_zero():
    answers_list = generate_static_sample(90, 0) 

    survey = Survey(answers_list)
    result = survey.get_basic_results()
    assert result == {
        "S": {
            "AGGR": 0,
            "ANGS": 0,
            "DEPR": 0,
            "PARA": 0,
            "PHOB": 0,
            "PSYC": 0,
            "SOMA": 0,
            "UNSI": 0,
            "ZWAN": 0,
            "ZUSATZ": 0
        },
        "G": {
            "AGGR": 0.0,
            "ANGS": 0.0,
            "DEPR": 0.0,
            "PARA": 0.0,
            "PHOB": 0.0,
            "PSYC": 0.0,
            "SOMA": 0.0,
            "UNSI": 0.0,
            "ZWAN": 0.0
        },
        "P": {
            "AGGR": 0,
            "ANGS": 0,
            "DEPR": 0,
            "PARA": 0,
            "PHOB": 0,
            "PSYC": 0,
            "SOMA": 0,
            "UNSI": 0,
            "ZWAN": 0,
            "ZUSATZ": 0
        },
        "GS": 0,
        "GSI": 0.0,
        "PST": 0,
        "PSDI": 0.0
    }

def test_static_survey_all_four():
    answers_list = generate_static_sample(90, 4)

    survey = Survey(answers_list)
    result = survey.get_basic_results()
    assert result == {
    "S": {
        "AGGR": 24,
        "ANGS": 40,
        "DEPR": 52,
        "PARA": 24,
        "PHOB": 28,
        "PSYC": 40,
        "SOMA": 48,
        "UNSI": 36,
        "ZWAN": 40,
        "ZUSATZ": 28
    },
    "G": {
        "AGGR": 6.0,
        "ANGS": 10.0,
        "DEPR": 13.0,
        "PARA": 6.0,
        "PHOB": 7.0,
        "PSYC": 10.0,
        "SOMA": 12.0,
        "UNSI": 9.0,
        "ZWAN": 10.0
    },
    "P": {
        "AGGR": 6,
        "ANGS": 10,
        "DEPR": 13,
        "PARA": 6,
        "PHOB": 7,
        "PSYC": 10,
        "SOMA": 12,
        "UNSI": 9,
        "ZWAN": 10,
        "ZUSATZ": 7
    },
    "GS": 360,
    "GSI": 4.0,
    "PST": 90,
    "PSDI": 4.0
}
    
def test_survey_too_long():
    answers_list = [3, 1, 3, 1, 1, 4, 2, 1, 1, 3, 2, 0, 4, 0, 3, 0, 0, 0, 0, 1, 
                    0, 0, 0, 3, 3, 2, 0, 1, 1, 4, 2, 1, 3, 2, 3, 4, 1, 1, 1, 3, 
                    3, 1, 2, 4, 4, 0, 1, 1, 4, 4, 1, 3, 1, 2, 0, 1, 4, 4, 1, 4, 
                    0, 2, 1, 3, 4, 3, 0, 3, 0, 2, 2, 2, 4, 4, 2, 3, 0, 4, 0, 2, 
                    2, 2, 3, 4, 4, 1, 4, 0, 4, 2, 4]
    survey = Survey(answers_list)
    result = survey.get_basic_results()
    assert result is None