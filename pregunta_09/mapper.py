#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

#map
for linea in sys.stdin:
  base = linea.strip().split("  ")
  sys.stdout.write("{}\t{}\t{}\n".format(base[0], base[1] ,base[2]))
