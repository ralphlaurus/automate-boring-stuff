

def commaCode(items):
    items[len(items) - 1] = 'and ' + items[len(items) - 1]

    # for i in items:
    #     print(i, end=", ")
    return ', '.join(items)

print(commaCode(['a', 'b', 'c', 'd', 'e']))
# commaCode(['a', 'b', 'c', 'd', 'e'])

