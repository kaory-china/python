Num = int(input("Digite um número:"))
soma = 0
i = 10
while Num % i > 0:
  soma = soma + Num % i
  Num = Num - Num % i
  i = i * 10
print ("A soma dos dígitos é", soma)



#1. What do I want to repeat?
#  -> %
#2. What do I want to change each time?
#  -> *10
#3. How long should we repeat?
#  -> até acabarem os dígitos
