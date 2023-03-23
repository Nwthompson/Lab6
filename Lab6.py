def encode(pw):
    epw = ''
    for val in pw: #Converts string values into encoded string values
        nval = int(val) + 3 #Adds 3
        if nval >=10: #If value is 10 or more then subtract 10
            nval = nval-10
        nval = str(nval)
        epw += nval
    return epw

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
            pw += str(int(epw[x])-3) #subtracts 3 from encoded password
    return pw


if __name__ == '__main__':
    x = True
    while x == True:
        print('Menu') #Menu printout
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit \n')
        opt = int(input('Please enter an option: ')) #select option
        if opt == 1: #get password and encodes
            pw = input('Please enter your password to encode: ')
            epw = encode(pw)
            print('Your password has been encoded and stored!')
        elif opt == 2: #decodes password and displays encoded and decoded
            dpw = decode(epw)
            print('The encoded password is', epw, end = ', ')
            print('and the original password is', dpw, end = '. \n')
        elif opt == 3: #ends program
            x = False