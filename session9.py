# Imports
import math
import operator
import random
import time
from functools import singledispatch, wraps
import datetime
from time import perf_counter
from faker import Faker
from collections import namedtuple
import re
import string

fake = Faker()

# Q.1: Use Faker library to get 10000 random profiles. Using namedtuple,
# calculate the largest blood type, mean-current_location, oldest_person_age
# and average age (add proper doc-strings)

def timed_dec(fn):
    """
    This is a decorator which can run a function n times
    and returns the avg run time ( n times )
    """
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        time_elapsed = (end - start)
        print('Run time: {0:.6f}s'.format(time_elapsed))
        return result
    return inner

def profile_generator_nt(num_profiles: int):
    """
    This function generates random fake user profiles. Each of those profiles is stored
    as a namedtuple and a tuple of namedtuples is returned.
    The Function takes an integere as an input denoting the number of profiles to be genearted
    It returns a tuple of namedtuples containing the generated profiles
    """
    if not isinstance(num_profiles,int):
        raise TypeError("Only integers allowed as num_profiles")

    if num_profiles<0:
        raise ValueError("Please provide a positive integer for the number of profiles")

    profiles_list = []
    profile = namedtuple('profile', " ".join(list((fake.profile()).keys())))
    for i in range(num_profiles):
        profiles_list.append(profile(**fake.profile()))
    profiles_tuple = tuple(profiles_list)
    return profiles_tuple

@timed_dec
def calc_profile_stats_nt() -> "namedtuple":
    """
    This function returns the largest blood type, mean-current_location,
    oldest_person_age and average age for a provided namedtuple
    """
    num_profiles = 10000
    profiles = profile_generator_nt(num_profiles)
    current_date = datetime.date.today()
    blood_grp = dict()
    max_age = 0
    location = [0, 0]
    sum_ages = 0
    for profile in profiles:
        blood_grp[profile.blood_group] = blood_grp[profile.blood_group] + 1 if profile.blood_group in blood_grp else 1
        age = (current_date - profile.birthdate).days
        max_age = max(max_age, age)
        location[0] += profile.current_location[0]
        location[1] += profile.current_location[1]
        sum_ages += int(age/365)

    profile_stat = namedtuple('profile_stat', 'largest_blood_type mean_current_location oldest_person_age average_age')
    bg_largest = max(blood_grp, key=blood_grp.get)
    mean_current_location = (location[0]/num_profiles, location[1]/num_profiles)
    avg_age = round(sum_ages/num_profiles,1)
    oldest_person = round(max_age/365,1)
    return profile_stat(bg_largest, mean_current_location, oldest_person, avg_age)


# Q.2: Do the same thing above using a dictionary. Prove that namedtuple is faster.

def profile_generator_dict(num_profiles: int):
    """
    This function generates random fake user profiles. Each of those profiles is stored
    as a dictionary and a dictionary of dictionaries is returned.
    The Function takes an integere as an input denoting the number of profiles to be genearted
    It returns a dictionary of dictionaries containing the generated profiles
    """
    if not isinstance(num_profiles,int):
        raise TypeError("Only integers allowed as num_profiles")

    if num_profiles<0:
        raise ValueError("Please provide a positive integer for the number of profiles")

    profiles_dict = {}
    for i in range(num_profiles):
        profiles_dict[i] = fake.profile()
    return profiles_dict

@timed_dec
def calc_profile_stats_dict() -> "namedtuple":
    """
    This function returns the largest blood type, mean-current_location,
    oldest_person_age and average age for a provided dictionary
    """
    num_profiles = 10000
    profiles = profile_generator_dict(num_profiles)
    current_date = datetime.date.today()
    blood_grp = dict()
    max_age = 0
    location = [0, 0]
    sum_ages = 0
    for num in profiles:
        blood_grp[profiles[num]['blood_group']] = blood_grp[profiles[num]['blood_group']] + 1 if profiles[num]['blood_group'] in blood_grp else 1
        age = (current_date - profiles[num]['birthdate']).days
        max_age = max(max_age, age)
        location[0] += profiles[num]['current_location'][0]
        location[1] += profiles[num]['current_location'][1]
        sum_ages += int(age/365)

    profile_stat = namedtuple('profile_stat', 'largest_blood_type mean_current_location oldest_person_age average_age')
    bg_largest = max(blood_grp, key=blood_grp.get)
    mean_current_location = (location[0]/num_profiles, location[1]/num_profiles)
    avg_age = round(sum_ages/num_profiles,1)
    oldest_person = round(max_age/365,1)
    return profile_stat(bg_largest, mean_current_location, oldest_person, avg_age)


# Q.3: Create a fake data (you can use Faker for company names) for
# imaginary stock exchange for top 100 companies (name, symbol, open, high, close).
# Assign a random weight to all the companies. Calculate and show
# what value stock market started at, what was the highest value during the day
# and where did it end. Make sure your open, high, close are not totally random.
# You can only use namedtuple.

def companies_generator(num_companies: int):
    """
    This function generates random companies.
    The Function takes an integere as an input denoting the number of companies to be genearted
    It returns a list of namedtuples containing the generated companies
    """
    if not isinstance(num_companies,int):
        raise TypeError("Only integers allowed as num_companies")

    if num_companies<0:
        raise ValueError("Please provide a positive integer for the number of profiles")

    companies_list = []
    weights_ini = [round(random.random(), 5) for x in range(num_companies)]
    sum_weights = sum(weights_ini)
    weights = [round(y/sum_weights, 5) for y in weights_ini]
    symbols = []
    Company = namedtuple('Company', 'Name Symbol Open High Close Weight')
    for z in range(num_companies):
        company_name = fake.company()
        symbol = (''.join([i[0] for i in re.split('[,. ]+', company_name.replace("-", " "))])).lower()
        temp=''
        while True:
            if symbol+temp not in symbols:
                symbols.append(symbol+temp)
                break
            temp = random.choice(string.ascii_lowercase)
        symbol += temp
        open = round(random.randint(10, 4000)*random.uniform(1.0001, 1.0002), 2)
        high = round(open*random.uniform(0.8, 1.2), 2)
        high = high if high > open else open
        close = round(open*random.uniform(0.8, 1.2), 2)
        close = close if high > close else high
        companies_list.append(Company(company_name, symbol, open, high, close, weights[z]))
    return companies_list

def imaginary_stock_exchange(num_companies: int) -> "namedtuple":
    """
    This function generates an imaginary stock exchange and gives the Index open, high and close of a 
    small stock exchange simulation of listed stocks.
    The Function takes an integere as an input denoting the number of companies to be listed in the stock exchange
    It returns a namedtuple containing the generated companies
    """
    if not isinstance(num_companies,int):
        raise TypeError("Only integers allowed as num_companies")

    if num_companies<0:
        raise ValueError("Please provide a positive integer for the number of profiles")

    companies = companies_generator(num_companies)
    index_open = round(sum([c.Open * c.Weight for c in companies]), 2)
    index_high = round(sum([c.High * c.Weight for c in companies]), 2)
    index_close = round(sum([c.Close * c.Weight for c in companies]), 2)
    imaginary_se_nt = namedtuple('imaginary_se_nt', 'Index_Open Index_High Index_Close')
    return imaginary_se_nt(index_open, index_high, index_close)

