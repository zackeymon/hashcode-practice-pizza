from pizza import Pizza
from parser import parse

p = parse("small.in")



input = p.grid

r = p.R
c = p.C
l = p.L
h = p.H

f = [[0 for x in range(c+1)] for y in range(r+1)]

def validSlice(start_i,start_j,end_i,end_j,input,L,H): 
    T = 0 
    M = 0 
    for ii in range(start_i,end_i+1): 
        for jj in range(start_j,end_j+1): 
            if input[ii][jj] == 0: 
                T += 1 
            else:
                M += 1 
    return T >= L and M >= L and T+M <= H

# Loop for calculating the DP matrix.
for i in range(r):
    for j in range(c):
        ii = i + 1
        jj = j + 1
        localMax = max(max(f[ii-1][jj], f[ii][jj-1]), f[ii-1][jj-1])

        # Loop for creating the current slice.
        for width in range(1, h+1):
            for height in range(1, h+1):
                area = width * height
                topEdge = i - height
                leftEdge = j - width
                if (area > 1
                    and area <= h
                    and leftEdge >= -1 
                    and topEdge >= -1 
                    and validSlice(topEdge+1, leftEdge+1, i, j, input, l, h)
                    and area + max(max(f[topEdge+1][jj], f[ii][leftEdge+1]), f[topEdge+1][leftEdge+1]) > localMax):
                        # There is a case misssed, where the remainder of the cropped space can be reused somehow.
                        localMax = area + max(max(f[topEdge+1][jj], f[ii][leftEdge+1]), f[topEdge+1][leftEdge+1])
        f[ii][jj] = localMax

res = 0
print(f)
for i in range(r+1):
    for j in range(c+1):
        if (f[i][j] > res): res = f[i][j]

print(res)