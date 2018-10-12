import os
import sys

with open(sys.argv[1], 'rb') as lines:
     with open(sys.argv[2], 'wb') as outfile:
         for line in lines:
            line = line.replace(os.linesep, "") + ',' + os.linesep
            outfile.write(line)

