#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
  #armar las listas  
  
import sys 
lista=[]  

for line in sys.stdin:
   key, fecha, valor = line.split("\t") 
   valor=int(valor) 
   lista.append([key, fecha, valor]) 

#ordenar
lista = sorted(lista, key=lambda x: (x[2]))  
lista= lista[0:6] 
for linea in lista: 
   sys.stdout.write("{}   {}   {}\n".format(linea[0], linea[1], linea[2]))
