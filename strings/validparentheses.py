# coding:utf-8


def is_parentheses_valid(parentheses):
    plist = [s for s in parentheses]
    tokens = {('(', ')'): 1, ('[', ']'): 1, ('{', '}'): 1}
    temp_list = []
    while len(plist) > 0:
        token = plist.pop(0)
        if len(temp_list) > 0:
            if (temp_list[0], token) in tokens:
                temp_list.pop(0)
            else:
                temp_list.insert(0, token)
        else:
            temp_list.insert(0, token)
    return 0 == len(temp_list)

PARENTHESES = '{}[{]'
print "result", is_parentheses_valid(PARENTHESES)

