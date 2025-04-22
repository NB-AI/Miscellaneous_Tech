winStr = "Your string comes here\0"

def win2unix(winStr):
    unixStr = '' # start with an empty string that is filled with help of the for-loop
    r_before_n = False

    for symbols in winStr:
        if symbols is '\r':
            r_before_n=True
        elif r_before_n is True and symbols is '\n': # if '\n' follows after '\r'
            unixStr = unixStr + symbols # append unixStr by the current symbol (here '\n')
            r_before_n = False
        elif symbols is not '\n' and symbols is not '\r': # any other symbol besides '\n', '\r'
            unixStr = unixStr + symbols
        elif r_before_n is True and symbols is not '\n': # there is '\r' but no '\n' follows
            raise AttributeError('There is a single "\\r" in the input string!')
        elif r_before_n is False and symbols is '\n': # there is no '\r' in front of '\n'
            raise AttributeError('There is a single "\\n" in the input string!')
    return unixStr

win2unix(winStr)
