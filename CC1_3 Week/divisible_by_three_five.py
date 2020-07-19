'it checks if the number is divisible by 3 and 5'

NumInt = int(input("Numero: "))
if NumInt % 5 == 0 and NumInt % 3 == 0:
  print("FizzBuzz")
else:
  print(NumInt)
