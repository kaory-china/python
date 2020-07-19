def incomodam(n):
    if n == 1:
      return 'incomodam '
    elif n > 0:
      return 'incomodam '+ incomodam(n-1)
    else:
        return ' '
    

def elefantes(n, x=1):
    if x == n:
        if x == 1:
            print('Um elefante incomoda muita gente')
        else:
            print(str(n), 'elefantes ', incomodam(n), 'muito mais')
    elif x != n and n > 2:
        if x == 1:
            print('Um elefante incomoda muita gente')
        else:
            print(str(x), 'elefantes ', incomodam(n), 'muito mais')
            print (str(x), 'elefantes incomodam muita gente')
        return elefantes(n, x+1)
    else:
        return ' '

