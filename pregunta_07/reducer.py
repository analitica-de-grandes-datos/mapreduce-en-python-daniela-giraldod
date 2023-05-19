#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys
if __name__ == '__main__':

    word = []
    num = []

    for line in sys.stdin:
        word.append(line.split("\t")[0])
        num.append(int(line.split("\t")[2]))

    ky_value = zip(word, num)

    ky_value_2 = sorted(ky_value,key=lambda x:(x[0],x[1]))

    for word, date, num in ky_value_2:
      sys.stdout.write("{}   {}   {}\n".format(word, num))
