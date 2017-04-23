import Image, numpy
import cv2
from numpy import linalg as LA
import minieigen as eigen


k = numpy.asarray(Image.open('1.jpg').convert('L'))

print k 

M = eigen.Matrix3(1, 0, 0, 0, 2, 0, 0, 0, 3, 5, 0, 6, 6, 6, 1, 6, 6)
print M.spectralDecomposition()
