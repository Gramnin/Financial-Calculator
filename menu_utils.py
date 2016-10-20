def menu(list, head=None, foot=None):
    options = {}
    l = max(len(str(item[0])) for item in list)
    for line in list:
        options[str(line[0])] = line[2:]
        print("%*d : %s" % (l, line[0], line[1]))
    try:
        num = input("> ")
    except KeyboardInterrupt as e:
        return e
    while num not in options:
        print("Invalid Option")
        try:
            num = input("> ")
        except KeyboardInterrupt as e:
            return e
    print()
    return line[2](*line[3:])

def menu_loop(list, head=None, foot=None):
    while True:
        out = menu(list, head, foot)
        if isinstance(out, KeyboardInterrupt):
            print()
            break
        elif out is not None:
            print(out)
        print()
