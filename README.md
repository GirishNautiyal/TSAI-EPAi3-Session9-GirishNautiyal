# Session 9
Session 9 - Tuples and Named Tuples

### Description of the module:
This is for session 9 assignment on the tuples and Named Tuples. It includes some of the concepts from previous sessions as well.

### Problem Statement

Write separate decorators that:
1. Use Faker library to get 10000 random profiles. Using named tuple , calculate the largest blood type, mean-current_location, oldest_person_age and average age (add proper doc-strings). - 250 pts (including 5 test cases)  
2. Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250 pts (including 5 test cases)  
3. Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value stock market started at, what was the highest value during the day and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. - 500 pts (including 10 test cases)  

**note 1** : Please write a readme file that can help me understand your code.  
**note 2** : Your github code must have cleared all the 20 tests that you're writing. 
**note 3** : Add the notebook as well to your github where logs can be visible. 

### Implementation

**timed_dec:** This is a decorator which can run a function n times and returns the avg run time ( n times ).  

**profile_generator_nt:** This function generates random fake user profiles. Each of those profiles is stored as a namedtuple and a tuple of namedtuples is returned. The Function takes an integere as an input denoting the number of profiles to be genearted. It returns a tuple of namedtuples containing the generated profiles.  

**calc_profile_stats_nt:** This function returns the follwoing stats - largest blood type, mean-current_location, oldest_person_age and average age for a provided namedtuple. The function returns the stats in the form of a namedtuple.  

**profile_generator_dict:** This function generates random fake user profiles. Each of those profiles is stored as a dictionary and a disctionary of dictionaries is returned. The Function takes an integere as an input denoting the number of profiles to be genearted. It returns a disctionary of dictionaries containing the generated profiles.  

**calc_profile_stats_dict:** This function returns the follwoing stats - largest blood type, mean-current_location, oldest_person_age and average age for a provided dictionary. The function returns the stats in the form of a namedtuple.  

**companies_generator:** This function generates random companies. The Function takes an integere as an input denoting the number of companies to be genearted It returns a list of namedtuples containing the generated companies.  

**imaginary_stock_exchange:** This function generates an imaginary stock exchange and gives the Index open, high and close of a small stock exchange simulation of the listed stocks. The Function takes an integere as an input denoting the number of companies to be listed in the stock exchange. It returns a namedtuple containing the generated companies.  


### Test Cases:

Some basic test cases are written to test README (number of words, keywords covered, proper headings for README), naming standards, indentations, docstrings and annotations. Function wise test cases have also been added as instructed.