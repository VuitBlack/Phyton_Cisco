# Archivo para Python-2, para usarlo en Python-3 se necesita poner paréntesis en los prints
import os, sys

r, w = os.pipe()
processid = os.fork()

if processid:
    os.close(w)
    r = os.fdopen(r)
    print "Padre leyendo"
    str = r.read()
    print "texto:", str  
    sys.exit(0)
else:
    os.close(r)
    w = os.fdopen(w, 'w')
    print "Hijo escribiendo"
    w.write("Hello World")
    w.close()
    print "Hijo Cierra"
    sys.exit(0)            