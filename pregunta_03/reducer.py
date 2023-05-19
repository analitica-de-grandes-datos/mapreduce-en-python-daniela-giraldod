#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#reduce
import sys

list = []

for linea in sys.stdin:
  separada = linea.split(",")
  list.append((separada[0],separada[1]))
  list.sort(key=lambda x: x[1])

for tupla in list:
  sys.stdout.write(tupla[0] + "," + str(tupla[1])) 
