import re
def readwords( filename ):
    f = open(filename)
    words = [ line.rstrip() for line in f.readlines()]
    return words
d1 = readwords('input.txt')

d1 = [element.lower() for element in d1]
