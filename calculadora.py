num1 = input("Digite o número que você deseja converter: ")
num2 = int(input("Digite o tipo de número que você deseja converter: \n 1- Binário \n 2- Octal \n 3- Decimal \n 4- Hexadecimal \n"))

#Binário

if num2 == 1 :

  if num1 != 0 and num1 != 1 :

    print("Isso não é um número binário")

  else :

    num3 = int(input("Digite o tipo de conversão que deseja:\n 1- Octal \n 2- Decimal \n 3- Hexadecimal \n"))

    if num3 == 1 :
      octal = oct(int(num1))
      print("O seu número convertido para octal fica: ",octal)

    if num3 == 2 :
      decimal = (int(num1))
      print("O seu número convertido para decimal fica: ",decimal)

    if num3 == 3 :
      hexadecimal = hex(int(num1))
      print("O seu número convertido para hexadecimal fica: ",hexadecimal)

    if num3 > 3 :
      print("Essa opção não existe")

#Octal

if num2 == 2 :

  num3 = int(input("Digite o tipo de conversão que deseja: \n 1- Binário \n 2- Decimal \n 3- Hexadecimal \n"))

  if num3 == 1 :
    binario = bin(int(num1, 8))
    print("O seu número convertido para binario fica: ",binario)

  if num3 == 2 :
    decimal = (int(num1, 8))
    print("O seu número convertido para decimal fica: ",decimal)

  if num3 == 3 :
    hexadecimal = hex(int(num1))
    print("O seu número convertido para hexadecimal fica: ",hexadecimal)

  if num3 > 3 :
    print("Essa opção não existe")

#Decimal

if num2 == 3 :

  num3 = int(input("Digite o tipo de conversão que deseja: \n 1- Binário \n 2- Octal \n 3- Hexadecimal \n"))

  if num3 == 1 :
    binario = bin(int(num1))
    print("O seu número convertido para binario fica: ",binario)

  if num3 == 2 :
    octal = oct(int(num1))
    print("O seu número convertido para octal fica: ",octal)

  if num3 == 3 :
    hexadecimal = hex(int(num1))
    print("O seu número convertido para hexadecimal fica: ",hexadecimal)

  if num3 > 3 :
    print("Essa opção não existe")

#Hexadecimal

if num2 == 4 :

  num3 = int(input("Digite o tipo de conversão que deseja: \n 1- Binário \n 2- Octal \n 3- Decimal \n"))

  if num3 == 1 :
    binario = bin(int(num1, 16))
    print("O seu número convertido para binario fica: ",binario)

  if num3 == 2 :
    octal = oct(int(num1, 16))
    print("O seu número convertido para octal fica: ",octal)

  if num3 == 3 :
    decimal = int(num1, 16)
    print("O seu número convertido para decimal fica: ",decimal)

  if num3 > 3 :
    print("Essa opção não existe")


if num3 > 4 :
  print("Essa opção não existe")