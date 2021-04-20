def BracketMatcher(strParam):

    # code goes here
    LEFT_BRACKET = '('
    RIGHT_BRACKET = ')'
    if strParam.find(LEFT_BRACKET) == -1 \
            and strParam.find(RIGHT_BRACKET) == -1:
        return 1
    if strParam.count(LEFT_BRACKET) != strParam.count(RIGHT_BRACKET):
        return 0
    left_brackets = 0
    right_brackets = 0
    while strParam.count(LEFT_BRACKET) + strParam.count(RIGHT_BRACKET) > 0:
        left_position = strParam.find(LEFT_BRACKET)
        right_position = strParam.find(RIGHT_BRACKET)
        if left_position < right_position and left_position >= 0:
            left_brackets += 1
            strParam = strParam[left_position + 1:]
        elif left_position > right_position and right_position >= 0:
            right_brackets += 1
            strParam = strParam[right_position + 1:]
        elif left_position >= 0 and right_position < 0:
            left_brackets += 1
            strParam = strParam[left_position + 1:]
        elif right_position >= 0 and left_position < 0:
            right_brackets += 1
            strParam = strParam[right_position + 1:]
        if right_brackets > left_brackets:
            return 0
        if strParam.count(LEFT_BRACKET) + strParam.count(RIGHT_BRACKET) == 0:
            if left_brackets != right_brackets:
                return 0
            break

    return 1


'''
# keep this function call here
print(BracketMatcher(input()))
'''
