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

def decode(epw):
    pw = ""
    for x in range(0, len(epw)): # from 0 to length of the encoded password
        if epw[x] == "2":
            pw += "9"
        elif epw[x] == "1":
            pw += "8"
        elif epw[x] == "0":
            pw += "7"
        else:
            pw += str(int(epw[x])-3)
    return pw