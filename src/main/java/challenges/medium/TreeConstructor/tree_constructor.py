import re


FIRST_NUMBER = re.compile("(?<=\\()\\d+(?=\\,)")
SECOND_NUMBER = re.compile("(?<=\\,)\\d+(?=\\))")


def TreeConstructor(strArr):

    # code goes here
    numArray = unpack_to_integers(strArr)
    print(numArray)
    return numArray


def unpack_to_integers(strArray):
    return [[int(FIRST_NUMBER.search(x).group(0)), int(SECOND_NUMBER.search(x).group(0))] for x in strArray]


'''
# keep this function call here
print(TreeConstructor(input()))
'''
