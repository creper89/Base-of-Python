def len_dict(d):
    l = 0
    for i in d:
        l += 1
    return l


def key_in_dict(d, key):
    for i in d:
        if i is key:
            return True
    return False
