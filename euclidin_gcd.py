def ggd(a, b):
    if b > a:
        a, b = b, a
    lookup = {}
    rest = 1
    while rest != 0:
        rest = a % b
        times = a // b
        lookup[str(rest)] = (str(a), str(times), str(b))
        a, b = b, rest

    return a, lookup



def rewrite(lookup):
    first_entry = list(lookup.values())[0]
    new_lookup = {}
    new_lookup[first_entry[0]] = (1, 0)
    new_lookup[first_entry[2]] = (0, 1)
    for step in lookup:
        if step != "0":
            record = lookup[step]

            factor = lookup[step][1]
            factor = int(factor)
            a, b = new_lookup[record[0]][0] - factor * new_lookup[record[2]][0], new_lookup[record[0]][1] - factor * new_lookup[record[2]][1]
            new_lookup[step] = (a, b)

    return a, b


x, lookup = ggd(123354514667, 2462357572346)

a, b = rewrite(lookup)
print(a, b, x)
