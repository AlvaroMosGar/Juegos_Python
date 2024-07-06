#ejercicio ahorcado

# print("-----\n|   |\n|   O  \n| --|--\n|   |\n|  / \ ")

#Funcion para que vaya pintando el dibujo dependiendo
# de los fallos.
def aorca(nf):
  if nf == 0:
    return "-----\n|   |\n|\n|\n|\n|"
  elif nf == 1:
    return "-----\n|   |\n|   O  \n|\n|\n|"
  elif nf == 2:
    return "-----\n|   |\n|   O  \n|   |  \n|   |\n|"
  elif nf == 3:
    return "-----\n|   |\n|   O  \n| --|\n|   |\n|"
  elif nf == 4:
    return "-----\n|   |\n|   O  \n| --|--\n|   |\n|"
  elif nf == 5:
    return "-----\n|   |\n|   O  \n| --|--\n|   |\n|  /"
  elif nf == 6:
    return "-----\n|   |\n|   O  \n| --|--\n|   |\n|  / \ "

#Funcion que quita los espacios
def quitar_caracter(cad):
  a = ""
  for i in range(len(cad)):
    if cad[i].lower() != " ":
      a = a + cad[i]
  return a

#Funcion que cambia el _ por la letra correspondiente
def reemplazar_caracter(txt,cad,ltr):
  a = ""
  cad = quitar_caracter(cad)
  for i in range(len(cad)):
      if txt[i].lower() == ltr.lower():
        a = a + txt[i] + " "
      elif cad[i] != "_":
        a = a + cad[i] + " "
      else:
        a = a + "_ "
  return a

# Funcion que comprueba si la letra introducida está en la palabra
# a adivinar.
def encontrar_caracter(txt,c):
  for i in range(len(txt)):
    if txt[i].lower() == c.lower():
      return True
  return False

# Funcion que solo se ejecuta al principio
# Su funcion es ocultar la palabra por guiones
def inicio(txt):
  a = ""
  for i in range(len(txt)):
    if txt[i] != " ":
      a = a + "_ "
    else:
      a = a + " "
  return a

# Esta funcion nos sirve para comprobar si el usuario
# esta introduciendo un caracter repetido o no
def p_repes(txt,c):
  for i in range(len(txt)):
    if c == txt[i]:
      return False
  return True

# La Funcion main del juego
def app_ahorcado(txt):
  fallos = 0
  new = ""
  rep = ""

  print("Empieza el juego, jugador 2 intenta adivinar la palabra.")
  print("Tienes 6 intentos. Mucha suerte")
  new = inicio(txt)
  print(aorca(fallos))
  print(new)

  while fallos < 6:
    ply2 = str(input("Introduce un caracter o la palabra: "))

    if len(ply2) > 1:
      if ply2.lower() == txt.lower():
        print("Enhorabuena!!!! Has acertado la palabra")
        break
    else:
      if p_repes(rep,ply2):
        rep = rep + ply2
        if encontrar_caracter(txt,ply2):
            new = reemplazar_caracter(txt,new,ply2)
            print(aorca(fallos))
            print(new)
        else:
            fallos += 1
            print("Fallaste :(")
            print(aorca(fallos))
            print(new)
      else:
        print("Has introducido una letra repetida, prueba con otra.")

      if txt == quitar_caracter(new):
        print("Enhorabuena!!!! Has acertado la palabra")
        break

  if fallos == 6:
    print("Se te han acabado los intentos.")
    print("Has perdido :( otra vez será.")
    print("La palabra era:",txt)



ply1=str(input("Introdce una palabra que quieras que adivine el Jugador2: "))
app_ahorcado(ply1)