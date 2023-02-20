def zero(items, left, middle, right):
    if items[0] == 'MINID':
        return left
    if items[0] == 'IOKE':
        return middle
    if items[0] == 'FLUX':
        return right

def four(items, left, right):
    if items[4] == 2016:
        return left
    if items[4] == 1957:
        return right

def three(items, left, middle, right):
    if items[3] == 'AWK':
        return left
    if items[3] == 'ELM':
        return middle
    if items[3] == 'EJS':
        return right

def one(items, left, right):
    if items[1] == 1984:
        return left
    if items[1] == 1992:
        return right

def main(items):
    return one(items,
               three(items,
                     four(items,
                          zero(items, 0, 1, 2),
                          zero(items, 3, 4, 5)),
                     four(items, 6, zero(items, 7, 8, 9)), 10), 11)


print(main(['MINID', 1992, 'NIT', 'ELM', 1957]))
print(main(['MINID', 1984, 'NIT', 'ELM', 1957]))
print(main(['MINID', 1984, 'NIT', 'EJS', 1957]))
print(main(['FLUX', 1984, 'NINJA', 'AWK', 2016]))
print(main(['MINID', 1984, 'NIT', 'ELM', 2016]))
