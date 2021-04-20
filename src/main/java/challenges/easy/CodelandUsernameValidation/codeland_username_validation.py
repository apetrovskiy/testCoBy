def CodelandUsernameValidation(strParam):

    # code goes here
    result = "false"
    if len(strParam) < 4 and len(strParam) > 25:
        return result
    if not strParam[0].isalpha():
        return result
    test = set([False for x in strParam
                if x.isalpha() or x.isnumeric() or x == "_"])
    if not test:
        return result
    # print
    if strParam[len(strParam) - 1:] == '_':
        return result
    return "true"

# keep this function call here
# print(CodelandUsernameValidation(input()))
