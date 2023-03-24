import numpy
def inverseMatrix():
    x = numpy.array([[1,2], [3,4]])

    y = numpy.linalg.inv(x)

    print(x)

    print (y)
inverseMatrix()
print("inverse matrix")