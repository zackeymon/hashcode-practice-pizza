from slice import Slice
from pizza import Pizza
from parser import parse
from coord import Coord

input_m = [
    [ 1, 0, 1, 0, 1, 0 ],
    [ 0, 1, 0, 1, 0, 1 ],
    [ 1, 0, 1, 0, 1, 0 ],
    [ 0, 1, 0, 1, 0, 1 ],
    [ 1, 0, 1, 0, 1, 0 ],
    [ 0, 1, 0, 1, 0, 1 ]
]

def isValidSlice(valA, valB):
    if (valA + valB) == 1:
        return True
    return False

def visitSlices(matrix, slices):
    for line in matrix:
        pass


def maxSlices(pizza):
    matrix = pizza.grid
    print "matrix:"
    print matrix
    # Output Data Type
    slices = []

    iMax = pizza.R
    jMax = pizza.C
    i = 0
    while (i < (iMax - 1)):
        j = 0
        while (j < (jMax - 1)):
            startVal   = matrix[i][j]
            endVal     = matrix[i][j+1]
            if (isValidSlice(startVal, endVal)):
                startCoord = Coord(i, j)
                endCoord   = Coord(i, j + 1)
                currSlice  = Slice(startCoord, endCoord)
                slices.append(currSlice)
                j+=2
            else:       
                j+=1
        i+=1

    # print matrix
    for currSlice in slices:
        currSlice.printSlice()
    visitSlices(matrix, slices)



mypizza = parse("example.in")
print "mypizza.grid:"
print mypizza.grid
maxSlices(mypizza)