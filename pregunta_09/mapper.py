#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

#map
for linea in sys.stdin:
  letra = linea.split("  ")[0]
  fecha = linea.split("  ")[1]
  num = int(linea.split("  ")[2])
  sys.stdout.write("{}\t{}\t{}\n".format(letra,fecha,num))
