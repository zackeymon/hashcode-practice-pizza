from coord import Coord

class Slice:

    def __init__(self, start, end):
        self.start = start
        self.end   = end

    def printSlice(self):
        print "Slice: " + self.start.toString() + " to " + self.end.toString()