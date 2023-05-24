#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
   clave, val = line.split("\t")
   val = list(val.strip().split(",")
                 
for letra in val:
            
    sys.stdout.write("{}\t{}\n".format(letra, clave))
