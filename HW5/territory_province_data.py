PROVINCE_NAMES = ["Alberta", "British Columbia", "Manitoba", 
                 "New Brunswick", "Newfoundland and Labrador", 
                 "Northwest Territories", "Nova Scotia", "Nunavut", "Ontario", 
                 "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon"]

POPULATION = [4262635, 5000879, 1342153, 775610, 510550, 41070, 
              969383, 36858, 14223942, 154331, 8501833, 1132505, 40232]


AREA = [640330.46, 922503.01, 552370.99, 71388.81, 370514.08, 1143793.86, 
        52942.27, 1877778.53, 908699.33, 5686.03, 1356625.27, 588243.54, 474712.68]

"""
for calculation purposes you should know that 
these areas are given in square kilometers. 
"""

IS_PROVINCE = [True, True, True, True, True, False, True, 
               False, True, True, True, True, False]

HEADERS = ["Province or Territory Name", "Population", "Area", "Is Province?"]

"""
The constant "headers" are sometimes called "categories" in the text below, 
and the names you use for the parameters has to match exactly 
what we have asked for to pass the autograder. 
Call the constant "Headers", but be sure to name the parameter as specified. 
"""