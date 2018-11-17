import math
import sys


#Finds the distance between the points (x1,y1) and (x2,y2)
def findDistance(x1, y1, x2, y2):
    d1 = (x1-x2) * (x1-x2)
    d2 = (y1-y2) * (y1-y2)
    return math.sqrt(d1 + d2)


#Finds the slope of the line that passess throught (x1,y1) -> (x2,y2)
def findSlope(x1, y1, x2, y2):
    if(x2-x1 == 0):
        slope = 0
    else:
        slope = (y2 - y1) / (x2 - x1)
    return slope


#Finds the inequality for the line passing through (x1,y1), (x2,y2) using the point (x3,y3)
def findInequality(x1, y1, x2, y2, x3, y3):
    slope = findSlope(x1, y1, x2, y2)
    b = y1 - (slope * x1)
    p3Val = (slope * x3) + b
    inequality = ""

    if(y3 >= p3Val):
        inequality = ">="
    else:
        inequality = "<="

    return inequality

#finds the linear equation passing through the points (x1,y1) -> (x2,y2). The third point determines the inequality of the line
def findEquation(x1, y1, x2, y2, x3, y3):
    a = y2 - y1
    b = x1 - x2
    c = (a * x1) + (b * y1)



    inequality = findInequality(x1, y1, x2, y2, x3, y3)
    return("%fx + %fy %s %f,\n" % (a,  b, inequality, c))


class triangle:
    def __init__(self, x1, y1, z1, x2, y2, z2, x3, y3, z3):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.x3 = x3
        self.y3 = y3
        self.z3 = z3

    def getP1P2Inequality(self):
        return findEquation(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)
    def getP1P3Inequality(self):
        return findEquation(self.x1, self.y1, self.x3, self.y3, self.x2, self.y2)
    def getP2P3Inequality(self):
        return findEquation(self.x2, self.y2, self.x3, self.y3, self.x1, self.y1)

    def get3DEquation(self):
        dx = self.x1 - self.x3
        dy = self.y1 - self.y3
        dz = self.z1 - self.z3

        tx = self.x2 - self.x3
        ty = self.y2 - self.y3
        tz = self.z2 - self.z3


        a = (dy * tz) - (dz * ty)
        b = (dz * tx) - (dx * tz)
        c = (dx * ty) - (dy * tx)
        d = (a * self.x1) + (b * self.y1) + (c * self.z1)



        return("%fx + %fy + %fz = %f.\n\n" % (a, b, c, d))


if(len(sys.argv) < 2):
    print("Error: Must Specify Input TIN File")
    quit()
else:
    inFile = open(sys.argv[1],'r')
    outFile = open("TIN_Relation.txt",'w')
    id = 1

    outFile.write("begin%TIN%\n\n")
    for i in inFile.readlines():
        outFile.write("TIN(id,x,y,z) :- id = %d,\n" %id)
        vals = i.split()
        t = triangle(int(vals[0]), int(vals[1]), int(vals[2]), int(vals[3]), int(vals[4]), int(vals[5]), int(vals[6]), int(vals[7]), int(vals[8]))
        outFile.write(t.getP1P2Inequality())
        outFile.write(t.getP1P3Inequality())
        outFile.write(t.getP2P3Inequality())
        outFile.write(t.get3DEquation())

        id = id + 1
    outFile.write("\n\nend%TIN%\n\n")




