'it takes a int input and prints the ten digit'

NumeroInteiro = int(input("Digite um número inteiro:")) 
DigitoDezena = (NumeroInteiro // 10) % 10
print("O dígito das dezenas é", DigitoDezena)
