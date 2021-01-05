def MinWindowSubstring(strArr):
    # code goes here
    if strArr is None or len(strArr[1]) == 0:
        return ""
    if len(strArr[1]) == 1:
        return "" if strArr[1] not in strArr[0] else strArr[1]
    return "ququ"

# keep this function call here 
# print(MinWindowSubstring(input()))
