#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#map

import sys
for separar in sys.stdin:
  separar = separar.strip().split('   ')
  sys.stdout.write('{}\n'.format(separar[0]))
