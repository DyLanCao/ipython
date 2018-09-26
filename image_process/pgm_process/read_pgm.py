#python3
# -- coding: utf-8 --

import math

def read_pgm(pgmf):
    """Return a raster of integers from a PGM as a list of lists."""
    p_value=pgmf.readline()
    print("p_value:",p_value)
    assert p_value == 'P5\n'
    (width, height) = [int(i) for i in pgmf.readline().split()]
    depth = int(pgmf.readline())
    print("width: height:",width,height)
    print("depth:",depth)
    assert depth <= 255

    raster = []
    for y in range(height):
        row = []
        for y in range(width):
            row.append(ord(pgmf.read(1)))
        raster.append(row)
    #print(raster)
    return raster

f = open('f002.pgm','rb')

read_pgm(f)
#print(read_pgm(f))
