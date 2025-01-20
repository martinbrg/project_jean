from t_values import TValues
import pytest


def test_empty_input():
    t_values = TValues(16, "female") 
    result = t_values.get_t_values({})
    assert result is None


def test_survey_all_zero():
    basic_values = {
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
    expected_result = {
        "S": {
            "AGGR": 35,
            "ANGS": 36,
            "DEPR": 33,
            "PARA": 39,
            "PHOB": 42,
            "PSYC": 40,
            "SOMA": 30,
            "UNSI": 35,
            "ZWAN": 32
        },
        "GSI": 28,
        "PST": 28,
        "PSDI": 34
        }
    t_values = TValues(16, "female") 
    result = t_values.get_t_values(basic_values)
    assert result == expected_result


def test_survey_all_four():
    basic_values = {
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
    
    expected_result = {
        "S": {
            "AGGR": 80,
            "ANGS": 80,
            "DEPR": 80,
            "PARA": 80,
            "PHOB": 80,
            "PSYC": 80,
            "SOMA": 80,
            "UNSI": 80,
            "ZWAN": 80
        },
        "GSI": 80,
        "PST": 80,
        "PSDI": 80
        }
    
    t_values = TValues(74, "male") 
    result = t_values.get_t_values(basic_values)
    assert result == expected_result


@pytest.mark.parametrize("invalid_age_inputs", [
    -1,      # Valid range is (Int) 16-74
    0,       
    15,
    75,
    "age",   
    None,    
    17.5,     
    [],      
    {}       
])


def test_age_invalid(invalid_age_inputs):
    with pytest.raises(ValueError, match="Age must be a positive integer between 16 and 74"):
        TValues(invalid_age_inputs, "female")


@pytest.mark.parametrize("invalid_genders", [
    1,      # Valid genders are "male", "female"
    0,       
    "Mann",
    "Frau",
    "männlich",
    "weiblich",
    None,    
    [],      
    {}       
])

def test_gender_not_in_list(invalid_genders):
    with pytest.raises(ValueError, match="Gender must be 'male' or 'female'"):
        TValues(16, invalid_genders)