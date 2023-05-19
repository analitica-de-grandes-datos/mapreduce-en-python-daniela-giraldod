#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys       

    l = []  
    for separar in sys.stdin:
        separar = separar.strip().split()
        l.append(line)
    for i in sorted(set([i[0] for i in l]),key=lambda x: x[0]):
        sys.stdout.write('{},{}\n'.format(i,l.count([i])))
