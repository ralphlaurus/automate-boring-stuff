

def commaCode(items):
    if len(items) == 0:
        return
    elif len(items) == 1:
        print(items[0], end="")
        return
    elif len(items) == 2:
        print(items[0] + ' and ' + items[1], end="")
        return
    # elif len(items) > 2:
    items[len(items) - 1] = 'and ' + items[len(items) - 1]

    for i in range(len(items) - 1):
        print(items[i], end=", ")
    print(items[len(items) - 1], end="")
    # return ', '.join(items)

# print(commaCode(['a', 'b', 'c', 'd', 'e']))
commaCode(['a', 'b', 'c', 'd', 'e'])

