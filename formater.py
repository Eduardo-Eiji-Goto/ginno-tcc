#!/usr/bin/env python3
import sys

# This formater exists because some of the datasets available had ';' to separate
# columns, which wasn't accepted by pandas as a readable CSV format.

# replaces ';' for ','
def main(inFile, outFile = 'datasets/corrected.csv'):
    f = open(inFile,'r')
    correctedString = f.read().replace(';',',')
    f.close()

    f = open(outFile, 'w')
    f.write(correctedString)
    f.close()

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        main(args[1])
    if len(args) == 3:
        main(args[1],args[2])
