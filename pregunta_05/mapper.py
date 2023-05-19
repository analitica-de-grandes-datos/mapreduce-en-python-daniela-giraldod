#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
    #map

import sys

if __name__ == "__main__":
for fec in sys.stdin:
  fecha = fec.strip().split("  ")[1]
  month =   fecha.strip().split('-')[1]
  sys.stdout.write("{}\t1\n".format(month))
