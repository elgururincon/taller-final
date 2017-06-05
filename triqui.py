
tablero = [1,2,3,4,5,6,7,8,9]                               # creacion del tablero

def impTablero ():                                          # presentacion del tablero 
  print tablero [0],'|',tablero[1],'|',tablero[2]  
  print '---------'
  print tablero [3],'|',tablero[4],'|',tablero[5]
  print '---------'
  print tablero [6],'|',tablero[7],'|',tablero[8]

impTablero()                                                # imprime tablero


                                                            # 0 es el valor del empate
MAX = 1                                                     # valor para cuando gana la CPU
MIN = -1                                                    # valor para cuando gana el usuario
global jugadaCpu                                            # define una variable global que se utiliza en todo el codigo
 
def valor(tablero, jugador):
    global jugadaCpu
    if finJuego(tablero):                                   # este pregunta si hay  ganador?
        return [ganador(tablero), 0]
    movimientos=[]                                          # crea un grupo donde se pueden guardar las  posibles jugadas
    for jugada in range(0,len(tablero)):                    #para cada jugada en el tablero se crea un tablero auxiliar
        if tablero[jugada] == 0:                            #-- mantiene la posible jugada dependiendo del jugador, funciona
            tableroaux=tablero[:]                           #--igual que el bubblesort , divide el tablero en 2 y busca la 
            tableroaux[jugada] = jugador                    #--jugada maas cercana a la jugada del usuario
 
            puntuacion = valor(tableroaux, jugador*(-1))
            movimientos.append([puntuacion, jugada])        # Guarda la jugada dentro del grupo de posiblies jugadas
  
    if jugador == MAX:                                       
        movimiento = max(movimientos)
        jugadaCpu = movimiento[1]
        return movimiento
    else:
        movimiento = min(movimientos)
        return movimiento[0]
 
 
def finJuego(tablero):                                      # funcion que busca el ganador
    empate = False                                          # empate ?
    for i in range(0,len(tablero)):                         
        if tablero[i] == 0:
            empate = True

    if ganador(tablero) == 0 and empate:                    # ganador ?
        return False
    else:
        return True
 
def ganador(tablero):                                       # funcion que recopila las combinaciones ganadoras
    lineas = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    ganador = 0                                             # contador
    for linea in lineas:
        if tablero[linea[0]] == tablero[linea[1]] and tablero[linea[0]] == tablero[linea[2]] and tablero[linea[0]] != 0:
            ganador = tablero[linea[0]]                     # busca si alguna de las combinaciones existe
    return ganador                                          # declara ganador
 
def dibujatablero(tablero):                                 # ingresa una x en el espacio que selecciona el usuario
    for i in range(0,3):                                    #--- y ingresa una o en el espacio que la cpu seleccione
        for j in range(0,3):                                #--- de caso contrario deja un punto (.)
            if tablero[i*3+j] == MAX:                       
                print 'O',
            elif tablero[i*3+j] == MIN:
                print 'X',
            else:
                print '.',
        print ''
 
def turnoUsuario(tablero):                                  # decalara funcion de jugada del usuario
    turno1=False
    while not turno1:
        espacio = input ("selecciona uno de los espacios: ")
        if str(espacio) in '0123456789' and len(str(espacio)) == 1 and tablero[espacio-1] == 0:
            if espacio == 0:
                break;                                      # termina con el turno del jugador
            tablero[espacio-1]=MIN                          # testa una opcion del tablero para la cpu
            turno1=True                                     # declara que el turno del jugador termina
    return tablero                                          # retorna tablero
 
def turnoCpu(tablero):                                      # declara funcion de jugada de la cpu
    global jugadaCpu                                        
    puntuacion = valor(tablero[:], MAX)
    tablero[jugadaCpu] = MAX
    return tablero

def inicioJuego():
    print 'Introduce una de los espacios o 0 para salir'
    tablero = [0,0,0,0,0,0,0,0,0]
 
### aca se declara la repintada el tablero con los ingresos de la cpu y del usuario
### repinta el tablero cada turno
    while (True):
        dibujatablero(tablero)                              
        tablero = turnoUsuario(tablero)
        if finJuego(tablero):
            break;
        tablero = turnoCpu(tablero)
        if finJuego(tablero):
            break;
 
    dibujatablero(tablero)
    resultado = ganador(tablero)
    if resultado == 0:
        gana = 'Empate'
    elif resultado == MIN:
        gana = 'Gana usuario'
    else:
        gana = 'Gana Cpu' 
    print 'Resultado:' + gana

inicioJuego()
