def is_palindrom(s):
    for i in range(stroke_len(s)):
        if s[i] != s[-(i+1)]:
            return False
    return True


def stroke_len(s):
    l = 0
    for i in s:
        l += 1
    return l


def lower_register(s):
    return s.lower()
