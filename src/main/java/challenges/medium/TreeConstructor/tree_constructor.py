import re
from collections import Counter


FIRST_NUMBER = re.compile("(?<=\\()\\d+(?=\\,)")
SECOND_NUMBER = re.compile("(?<=\\,)\\d+(?=\\))")


def TreeConstructor(strArr):

    # code goes here
    num_array = unpack_to_integers(strArr)
    result_dict = dict(Counter([item[1] for item in num_array]))
    return str(not any([x for x in result_dict if result_dict[x] > 2]) and any([x for x in result_dict if result_dict[x] == 2])).lower()


def unpack_to_integers(str_array):
    return [[int(FIRST_NUMBER.search(x).group(0)), int(SECOND_NUMBER.search(x).group(0))] for x in str_array]


'''
# keep this function call here 
print(TreeConstructor(input()))
'''
