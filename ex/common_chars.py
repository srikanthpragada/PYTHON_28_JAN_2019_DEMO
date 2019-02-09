def unique_chars(srclst, ignorecase=False):
    trglst = []
    if ignorecase:
        for v in srclst:
            chars = "".join(trglst).upper()
            if v.upper() not in chars:
                trglst.append(v)
    else:
        for v in srclst:
            if v not in trglst:
                trglst.append(v)

    return trglst


# print( unique_chars(['a','b','b','A','B','c','a'],True))

def get_common_chars(st1, st2, ignorecase=False):
    chars = []
    if ignorecase:
        st2 = st2.upper()
    for c in st1:
        if ignorecase:
            if c.upper() in st2:
                chars.append(c)
        else:
            if c in st2:
                chars.append(c)

    return unique_chars(chars, ignorecase)


print(get_common_chars('aBcdba', 'abfD', True))
