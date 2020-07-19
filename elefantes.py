def incomodam(n):
    if n == 1:
      return 'incomodam '
    elif n > 0:
      return 'incomodam '+ incomodam(n-1)
    else:
        return ' '

def elefantes(n, x=1):
    text = ''
    if x == n:
        if x == 1:
            return 'Um elefante incomoda  muita gente' + '\n'
        else:
            return str(x) + ' elefantes ' + incomodam(x) + 'muito mais' + '\n'
    elif x != n and n > 1:
        if x == 1:
            text += 'Um elefante incomoda muita gente' + '\n'
        else:
            text += str(x) + ' elefantes ' + incomodam(x) + 'muito mais' + '\n'
            text += str(x+1) + ' elefantes incomodam muita gente' + '\n'
        return text + elefantes(n, x+1)
    else:                                                                                                                                                                                                                          
        return ' '
