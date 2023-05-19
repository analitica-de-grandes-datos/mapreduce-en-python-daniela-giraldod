#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    total = 0
    minimo = 0
    maximo = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            if val > maximo:
                maximo = val
            elif val < minimo:
                minimo = val
        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo))

            curkey = key
            total = val
            minimo = val
            maximo = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo))
