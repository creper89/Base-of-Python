def find_element(list, a):
    for i in range(len(list)):
        if list[i] is a:
            return i
    return None


def element_count(list, a):
    s = 0
    for i in range(len(list)):
        if list[i] is a:
            s += 1
    return s