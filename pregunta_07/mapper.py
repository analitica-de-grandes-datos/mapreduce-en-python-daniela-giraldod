#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys
if __name__ == "__main__":
    for line in sys.stdin:
        fila = line.split()
        sys.stdout.write("{}\t{}\n".format(fila[0], fila[2]))
