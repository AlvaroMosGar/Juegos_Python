# Juego de guerreros y mazmorras para practicar las clases
# Y las clases heredadas.
import random as rd

# Clases:
class Personaje:
    def __init__(self, nombre: str, vida: float, dano: float) -> None:
        self.nombre = nombre
        self.vida = vida
        self.dano = dano

    def atacar(self, enemigo: object):
       enemigo.vida = enemigo.vida - self.dano
       Textos.texto_dano("ataque",self.nombre,enemigo.nombre,self.dano)
        
    
    def escudo(self, enemigo: object):
        self.vida += enemigo.dano
    
    def muerto(self) -> bool:
        if self.vida <= 0:
            return True
        else:
            return False
        
    def set_cura(self):
        self.vida *= 1.58
    
#Heroes
class Guerrero(Personaje):
    def __init__(self, nombre: str, vida: float, dano: float) -> None:
        super().__init__(nombre, vida, dano)

    def golpe_espada(self, enemigo: object):
        enemigo.vida = enemigo.vida - (self.dano*1.15)
        Textos.texto_dano("golpe de espada",self.nombre,enemigo.nombre,self.dano*1.15)
    
    def ataque_furia(self, enemigo: object):
        enemigo.vida = enemigo.vida - (self.dano*1.20)
        Textos.texto_dano("ataque de furia",self.nombre,enemigo.nombre,self.dano*1.20)

class Mago(Personaje):
    def __init__(self, nombre: str, vida: float, dano: float) -> None:
        super().__init__(nombre, vida, dano)

    def bola_fuego(self, enemigo: object):
        enemigo.vida = enemigo.vida - (self.dano*1.20)
        Textos.texto_dano("bola de fuego",self.nombre,enemigo.nombre,self.dano*1.20)
    
    def rayo_hielo(self, enemigo: object):
        enemigo.vida = enemigo.vida - (self.dano*1.45)
        Textos.texto_dano("rayo de hielo",self.nombre,enemigo.nombre,self.dano*1.45)

class Picaro(Personaje):
    def __init__(self, nombre: str, vida: float, dano: float) -> None:
        super().__init__(nombre, vida, dano)

    def estocada(self, enemigo: object):
        enemigo.vida = enemigo.vida - (self.dano*1.18)
        Textos.texto_dano("estocada",self.nombre,enemigo.nombre,self.dano*1.18)

    def ataque_sorpresa(self, enemigo: object):
        enemigo.vida = enemigo.vida - (self.dano*1.30)
        Textos.texto_dano("ataque sorpresa",self.nombre,enemigo.nombre,self.dano*1.30)

#Enemigos
DRAGON = Personaje("Dragón",200,50)
ORCO = Personaje("Orco",150,30)
ESQUELETO = Personaje("Esqueleto",100,20)
LICHE = Personaje("Liche",170,40)
GOBLIN = Personaje("Goblin",80,15)

#Tuplas necesarias
ene = (GOBLIN,ESQUELETO,ORCO,LICHE,DRAGON)
guerrero = ("Atacar","Golpe de espada","Ataque de Furia","Escudo")
mago = ("Atacar","Bola de Fuego","Rayo de Hielo","Escudo")
picaro = ("Atacar","Estocada","Ataque Sorpresa","Escudo")

# Textos que salen en pantalla.
class Textos:
    @staticmethod
    def texto_ini(enemigo:object):
        print(f"Te has encontrado con un {enemigo.nombre}, tiene {enemigo.vida} de vida y hace {enemigo.dano} de daño.")

    @staticmethod
    def turno_ene(enemigo:object):
        print(f"Es turno del {enemigo.nombre}.")

    @staticmethod
    def fallo_ene():
        print("El enemigo ha fallado el ataque.")
    
    @staticmethod
    def truno_jug(jugador:object):
        print(f"Es tu turno {jugador.nombre}.")

    @staticmethod
    def texto_muerte():
        print("Has muerto, se acabó la partida, bien jugado <3")
    
    @staticmethod
    def texto_dano(ataque:str,jugador:str, enemigo:str, dano:float):
        print(f"{jugador} ha lanzado un {ataque} a {enemigo} y le ha hecho {dano} de daño.")

    @staticmethod
    def ataque_no():
        print("Ya no puedes utilizar este ataque en este combate, has gastado sus usos.")
    
    @staticmethod
    def ataque_elige():
        print("Que ataque quieres elegir???")

    @staticmethod
    def no_existe_ataque():
        print("No existe ese ataque")
    
    @staticmethod
    def cura(vida:float):
        print(F"Te has encontrado una seta curativa y te la has comido.\nEsa seta te ha curado y ahora tienes {vida} de vida.")
    
    @staticmethod
    def escudo():
        print("Has elegido un escudo que te va ha parar el ataque del enemigo.")
    
    @staticmethod
    def identificar_clase(objeto):
        if isinstance(objeto, Guerrero):
            print(f"Eres un Guerrero que tiene {objeto.vida} de vida y {objeto.dano} de daño.")
        elif isinstance(objeto, Mago):
            print(f"Eres un Mago que tiene {objeto.vida} de vida y {objeto.dano} de daño.")
        elif isinstance(objeto, Picaro):
            print(f"Eres un Picaro que tiene {objeto.vida} de vida y {objeto.dano} de daño.")
    
    @staticmethod
    def muerte_ene(enemigo:object):
        print(f"Has derrotado al {enemigo.nombre}.")
    
    @staticmethod
    def win():
        print("Enhorabuena has podido derrotar a todos los enemigos.")
    
    @staticmethod
    def decora():
        print()
        print("           *********************************")
        print()

# Funcionamiento del juego
def eleccion_arma(ataques:dict) -> int:
    while True:
        cont = 1
        Textos.decora()
        Textos.ataque_elige()
        for i in ataques:
            print(cont,") ",i)
            cont += 1
        arm = int(input(":"))
        if arm <= 4 and arm > 0:
            return arm
        else:
            Textos.no_existe_ataque()

def combate(enemigo:object, jug:object, indi: int,ata1: int, ata2:int, esc:3) -> int:
    if indi == 1:
        while True:
            g = eleccion_arma(guerrero)
            if g == 1:
                jug.atacar(enemigo)
                break
            elif g == 2:
                if ata1 <=2:
                    jug.golpe_espada(enemigo)
                    ata1 += 1
                    break
                else:
                    Textos.ataque_no()
            elif g == 3:
                if ata2 <=1:
                    jug.ataque_furia(enemigo)
                    ata2 += 1
                    break
                else:
                    Textos.ataque_no()
            elif g == 4:
                if esc <=1:
                    jug.escudo(enemigo)
                    esc += 1
                    break
                else:
                    Textos.ataque_no()
        return ata1,ata2,esc
    elif indi == 2:
        while True:
            m = eleccion_arma(mago)
            if m == 1:
                jug.atacar(enemigo)
                break
            elif m == 2:
                if ata1 <=2:
                    jug.bola_fuego(enemigo)
                    ata1 += 1
                    break
                else:
                    Textos.ataque_no()
            elif m == 3:
                if ata2 <= 1:
                    jug.rayo_hielo(enemigo)
                    ata2 += 1
                    break
                else:
                    Textos.ataque_no()
            elif m == 4:
                if esc <=1:
                    jug.escudo(enemigo)
                    esc += 1
                    break
                else:
                    Textos.ataque_no()
        return ata1,ata2,esc
    else:
        while True:
            p = eleccion_arma(picaro)
            if p == 1:
                jug.atacar(enemigo)
                break
            elif p == 2:
                if ata1 <=2:
                    jug.estocada(enemigo)
                    ata1 += 1
                    break
                else:
                    Textos.ataque_no()
            elif p == 3:
                if ata2 <= 1: 
                    jug.ataque_sorpresa(enemigo)
                    ata2 += 1
                    break
                else:
                    Textos.ataque_no()
            elif p == 4:
                if esc <=1:
                    jug.escudo(enemigo)
                    esc += 1
                    break
                else:
                    Textos.ataque_no()
        return ata1,ata2,esc

def combates(jugador: object, indi: int) -> bool:
    cont = 0
    ata1 = 0
    ata2 = 0
    esc = 0
    for i in ene:
        Textos.decora()
        Textos.texto_ini(i)
        while True:
            a = rd.randint(0,6)
            Textos.decora()
            Textos.turno_ene(i)
            if a%2==0:
                i.atacar(jugador)
            else:
                Textos.fallo_ene()

            if jugador.muerto():
                return True

            Textos.decora()
            Textos.truno_jug(jugador)
            ata1,ata2,esc = combate(i,jugador,indi,ata1,ata2,esc)
            if i.muerto():
                Textos.decora()
                Textos.muerte_ene(i)
                break

        if jugador.muerto():
            return True
        cont += 1
        if cont%2 == 0:
            ata1 = 0
            ata2 = 0
            esc = 0
            Textos.decora()
            jugador.set_cura()
            Textos.cura(jugador.vida)
            

def inicio_de_personaje():
    nombre = str(input("Cual va ha ser tu nombre??? "))
    while True:
        clase = int(input("Que clase quieres ser??\n1)Guerrero\n2)Mago\n3)Picaro\n:"))
        if clase == 1:
            pl1 = Guerrero(nombre,200,50)
            ind = 1
            return pl1,ind
        elif clase == 2:
            pl1 = Mago(nombre,150,60)
            ind = 2
            return pl1,ind
        elif clase == 3:
            pl1 = Picaro(nombre,180,55)
            ind = 3
            return pl1,ind
        else:
            print("Este numero no está en el rango")

def juego() -> None:
    ply1,indi = inicio_de_personaje()
    Textos.decora()
    Textos.identificar_clase(ply1)
    if combates(ply1,indi) == True:
        Textos.texto_muerte()

    Textos.decora()
    Textos.win()

    Textos.decora()
    relo = str(input("Quieres volver a jugar?? SI o NO:"))
    if relo.lower() == "si":
        juego()

juego()