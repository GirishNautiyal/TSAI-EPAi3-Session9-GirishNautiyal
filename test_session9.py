import pytest
import random
import string
import session9
import os
import inspect
import re
import math
from decimal import Decimal
from random import randint
from faker import Faker


FUNCTIONS_TO_CHECK_FOR = [
    'timed_dec'
    ,'profile_generator_nt'
    ,'calc_profile_stats_nt'
    ,'profile_generator_dict'
    ,'calc_profile_stats_dict'
    ,'companies_generator'
    ,'imaginary_stock_exchange'

]

WORDS_TO_CHECK_FOR = [
    'tuple'
    ,'namedtuple'
    ,'Faker'
    ,'fake'
    ,'stock'
    ,'dictionary'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in WORDS_TO_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_function_are_listed():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    AllFUNCTIONSDEFINED = True
    for c in FUNCTIONS_TO_CHECK_FOR:
        if c not in content:
            AllFUNCTIONSDEFINED = False
            pass
    assert AllFUNCTIONSDEFINED == True, "You have not defined all the required functions"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session9)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_all_functions_with_docstrings():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert not function.__doc__ is None, f"You dont have docstring defined for {function}"

def test_all_functions_with_annotations():
    functions = [session9.timed_dec
                 , session9.calc_profile_stats_dict, session9.profile_generator_dict
                 , session9.calc_profile_stats_nt, session9.profile_generator_nt
                 , session9.companies_generator, session9.imaginary_stock_exchange]
    for function in functions:
        assert not function.__annotations__ is None, "You dont have annotations defined for {}".format(function.__name__)

fake = Faker()

# Test cases for Ques. 1

def test_timed(capsys):
    @session9.timed_dec
    def adder(a,b):
        return a+b
    
    adder(1,3)
    captured = capsys.readouterr()
    assert "Run time: " in captured.out, "Check the timed_dec decorator, print statements"

def test_profile_generator_nt_len():
    fake_profiles = session9.profile_generator_nt(10)
    assert len(fake_profiles) == 10, "The profile_generator_nt function does not work properly."
    
def test_profile_generator_nt_field():
    fake_profiles = session9.profile_generator_nt(10)
    assert fake_profiles[randint(0, 9)]._fields == tuple((fake.profile()).keys()), "The profile_generator_nt function does not work properly."

def test_profile_generator_nt_float():
    with pytest.raises(TypeError):
        session9.profile_generator_nt(10.0)

def test_profile_generator_nt_str():
    with pytest.raises(TypeError):
        session9.profile_generator_nt("10")

def test_profile_generator_nt_decimal():
    with pytest.raises(TypeError):
        session9.profile_generator_nt(Decimal('10'))

# Test cases for Ques. 2

def test_profile_generator_dict_len():
    fake_profiles = session9.profile_generator_dict(10)
    assert len(fake_profiles) == 10, "The profile_generator_dict function does not work properly."
    
def test_profile_generator_dict_field():
    fake_profiles = session9.profile_generator_dict(10)
    assert sorted(list(fake_profiles[randint(0, 9)].keys())) == sorted(list((fake.profile()).keys())), "Something wrong with the profile_generator_dict function."

def test_profile_generator_dict_float():
    with pytest.raises(TypeError):
        session9.profile_generator_dict(10.0)

def test_profile_generator_dict_str():
    with pytest.raises(TypeError):
        session9.profile_generator_dict("10")

def test_profile_generator_dict_decimal():
    with pytest.raises(TypeError):
        session9.profile_generator_dict(Decimal('10'))

# Test cases for Ques. 3

def test_companies_generator_len():
    fake_companies = session9.companies_generator(10)
    assert len(fake_companies) == 10, "The companies_generator function does not work properly."
    
def test_companies_generator_field():
    fake_companies = session9.companies_generator(10)
    assert fake_companies[randint(0, 9)]._fields == ('Name', 'Symbol', 'Open', 'High', 'Close', 'Weight'), "The companies_generator function does not work properly."

def test_companies_generator_float():
    with pytest.raises(TypeError):
        session9.companies_generator(10.0)

def test_companies_generator_str():
    with pytest.raises(TypeError):
        session9.companies_generator("10")

def test_companies_generator_decimal():
    with pytest.raises(TypeError):
        session9.companies_generator(Decimal('10'))

def test_imaginary_stock_exchange_se_len():
    fake_se_1 = session9.imaginary_stock_exchange(10)
    fake_se_2 = session9.imaginary_stock_exchange(20)
    assert len(fake_se_1) == len(fake_se_2), "The imaginary_stock_exchange function does not work properly."
    
def test_imaginary_stock_exchange_len():
    fake_se = session9.imaginary_stock_exchange(10)
    assert len(fake_se) == 3, "The imaginary_stock_exchange function does not work properly."

def test_imaginary_stock_exchange_float():
    with pytest.raises(TypeError):
        session9.imaginary_stock_exchange(10.0)

def test_imaginary_stock_exchange_str():
    with pytest.raises(TypeError):
        session9.imaginary_stock_exchange("10")

def test_imaginary_stock_exchange_decimal():
    with pytest.raises(TypeError):
        session9.imaginary_stock_exchange(Decimal('10'))