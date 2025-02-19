# Create empty set
empty_set = set()
print(empty_set)  # Output: set()
print(type(empty_set))
print("")

empty_dict = {}
print(type(empty_dict))  # Output: <class 'dict'>, this is a dictionary, not a set!
print("")

dict1 = {'1':1,'2':2,'3':3}
set = {'1','2','3',1,2,3}
print(type(dict)) 
print(dict) 
print(type(set)) 
print(set) 

# dict_new = dict('1' = 1, '2' = 2, '3' = 3)
# dict_new = dict(1 = 1, 2 = 2, 3 = 3)
# dict_new = dict("do" = 1, "re" = 2, "mi" = 3)
dict_new = dict(do = 1, re = 2, mi = 3)
print(dict_new) 
# when using dict() with keyword arguments, keys must be valid identifiers (like variable names), not strings with quotes.
# Why Numbers (int, float) / Lists, tuples, or other types / Strings with quotes