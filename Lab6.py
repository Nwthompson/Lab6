def encode(pw):
    epw = ''
    for val in pw:
        nval = int(val) + 3
        if nval >=10:
            nval = nval-10
        nval = str(nval)
        epw += nval
    return epw
pw = str(input('Enter Number:'))

print(encode(pw))