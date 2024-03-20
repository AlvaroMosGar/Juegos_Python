#Calcladora simple

# Hacer un programa que muestre el siguiente menú al usuario:
# 1. Suma
# 2. Resta
# 3. Multiplicaión
# 4. División
# 5. Factorial
# 6. Potencia
# 7. Es primo.
# 8. Salir

# 1
def suma ():
  a = int(input("Introduce un número: "))
  b = int(input("Introduce un número: "))
  sum = a + b
  return sum
# 2
def resta ():
  a = int(input("Introduce un número: "))
  b = int(input("Introduce un número: "))
  rest = a - b
  return rest
# 3
def multi ():
  a = int(input("Introduce un número: "))
  b = int(input("Introduce un número: "))
  multi = a * b
  return multi
# 4
def divi ():
  a = int(input("Introduce un número: "))
  b = int(input("Introduce un número: "))
  if b == 0:
    print("No se puede dividir entre 0.")
  else:
    divi = a / b
    print("El resultado de la división es: {0}".format(divi))

# 5
def factorial():
  n = int(input("Introduce un número: "))
  fac = 1
  for i in range(1,n + 1):
    fac = fac * i
  return fac

# 6
def poten():
  a = int(input("Introduce la base: "))
  b = int(input("Introduce el exponente: "))
  cont = a
  for i in range(1,b):
    cont = cont * a
  return cont
# 7
def primo():
  num = int(input("Introduce un número: "))
  contador = 0
  for i in range(1,num + 1):
    if num % i == 0:
      contador += 1

  if contador == 2:
    print("El número {0} es primo.".format(num))
  else:
    print("El número {0} no es primo.".format(num))

# Funcion main del programa
def menu():
  while True:
    calculo = int(input("1. Suma\n2. Resta\n3. Multiplicaión\n4. División\n5. Factorial\n6. Potencia\n7. Es primo\n8. Salir: "))
    if calculo == 8:
      break

    elif calculo == 1:
      resultado = suma()
      print("El resultado de la suma es: {0}".format(resultado))
    elif calculo == 2:
      resultado = resta()
      print("El resultado de la resta es: {0}".format(resultado))
    elif calculo == 3:
      resultado = multi()
      print("El resultado de la multiplicación es: {0}".format(resultado))
    elif calculo == 4:
      divi()
    elif calculo == 5:
      resultado = factorial()
      print("El resultado del factorial es: {0}".format(resultado))
    elif calculo == 6:
      resultado = poten()
      print("El resultado de la potencia es: {0}".format(resultado))
    elif calculo == 7:
      primo()

menu()