#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
    #map

import sys

if __name__ == "__main__":
    for line in sys.stdin:
      fecha = line.strip().split('  ')[1]
      month = fecha.strip().split('-')[1]
      sys.stdout.write("{}\t1\n".format(month))
    
    
