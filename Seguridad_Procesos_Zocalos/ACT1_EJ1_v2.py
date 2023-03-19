import os, sys                  #os es una interface que provee de una manera versatil funcionalidades dependientes del sistema operativo
                                #sys es un módulo que provee acceso a variables usadas por el interprete y a funciones que interactuan fuertemente con el interprete.

r, w = os.pipe()                #Crea una tubería, devuelve un par de descriptores (r,w) que se usaran para leer y escribir
processid = os.fork()           #Bifurca el proceso hijo, retorna un 0 en el hijo y la identificación del proceso hijo en el padre.

if processid:
    os.close(w)                 #cierra el descriptor del archivo (w)
    r = os.fdopen(r)            #retorna un objeto abierto conectado al descriptor del archivo(r)
    print ("Padre leyendo")    #imprime "Padre leyendo"  
    str = r.read()              #Lee el contenido del archivo (r) y lo devuelve a la cadena str
    print ("texto:", str)       #Imprime "texto:"
    sys.exit(0)                 #sys.exit(0) es terminación exitosa del programa
else:
    os.close(r)                 #cierra el descriptor del archivo (r)
    w = os.fdopen(w, 'w')       #retorna un objeto abierto conectado al descriptor del archivo(w)
    print ("Hijo escribiendo")  #imprime "Hijo escribiendo"
    w.write("Hello World")      #retorna el número de caracteres que fueron agregados al archivo (w)
    w.close()                   #cierra el archivo (w)
    print ("Hijo Cierra")       #imprime "Hijo Cierra"
    sys.exit(0)                 #sys.exit(0) es terminación exitosa del programa