#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

curkey = None
total = 0

for line in sys.stdin:
   key, val = line.split("\t")
   val = val.strip()

   if key == curkey:
      nums = nums + "," + str(int(val))
          
   else:
       if curkey is not None:

          sys.stdout.write("{}\t{}\n".format(curkey, nums))

       curkey = key
       nums = str(int(val))
            

sys.stdout.write("{}\t{}\n".format(curkey, nums))
