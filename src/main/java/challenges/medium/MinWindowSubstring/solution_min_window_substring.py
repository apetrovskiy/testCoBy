def MinWindowSubstring(strArr):
    # code goes here
    result = ""
    if strArr is None or len(strArr[1]) == 0:
        return result
    if len(strArr[1]) == 1:
        return result if strArr[1] not in strArr[0] else strArr[1]
    for index in range(0, len(strArr[1])):
        if strArr[0].find(strArr[1][index]) == -1:
            return result
    full_search_list = []
    for char_num in range(0, len(strArr[1])):
        position = 0
        search_list = []
        while strArr[0].find(strArr[1][char_num], position) > -1:
            search_list.append(strArr[0].find(strArr[1][char_num], position))
            position += 1
        # print(f"for char {strArr[1][char_num]}")
        # print(f"list {search_list}")
        search_list = set(search_list)
        full_search_list.append(search_list)
    # print(full_search_list)
    all_min = max([min(x) for x in full_search_list])
    # print(all_min)
    all_max = min([max(x) for x in full_search_list])
    # print(all_max)
    return strArr[0][all_max:all_min + 1]


'''
# keep this function call here
# print(MinWindowSubstring(input()))
'''
