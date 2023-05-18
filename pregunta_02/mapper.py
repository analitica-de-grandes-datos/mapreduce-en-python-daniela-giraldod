#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    print('%s, %s' % (fields[3], fields[4]))
