#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

#map
for fil in sys.stdin:
  separada = fil.split(",")
  sys.stdout.write(separada[0]+","+separada[1])
