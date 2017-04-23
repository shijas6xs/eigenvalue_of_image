import Image, numpy, cv2, cv
from PIL import Image
from numpy import linalg as LA

################                                              making square image                            ######################

###################################################################################################################################

########## read input image ##################
xfname = '1'
fname = xfname+'.jpg'

pK = cv2.imread(fname)  # main input image

############## find row or column is larger   ######################
r = len(pK)    # 3 rows in your example
c = len(pK[0]) # 2 columns in your example
if r >= c:
	m = r
else:
	m = c

#################### making a square image of largest of row and column and saving as file name of input #######


im = Image.new("RGB", (m, m))
pix = im.load()
for x in range(m):
    for y in range(m):
        pix[x,y] = (0,0,255)
#cv.SaveImage("100.jpg",im)
im.save("temp_sq.jpg")


##############

##### finding eigen value and vector #############3
######################################
im2 = numpy.asarray(Image.open('temp_sq.jpg').convert('L'))
sqimg = cv2.resize(pK, im2.shape, interpolation=cv2.INTER_LINEAR)


cv2.imwrite("sq_images/"+fname,sqimg)

K = numpy.asarray(Image.open(fname).convert('L'))
L, v = LA.eig(K)


print '\n\nInput Image Matrix: \n\n'
print K
print '\n\nEigen values : \n\n'
print L

#######################
#  sort eigen values
##########################
S = numpy.sort(-L)
print '\n\nSorted Eigen values : \n\n'
print -S
numpy.savetxt("text_codes/"+xfname+'.txt', S, delimiter=',') 
##############

print '\n\nEigen vectors : \n\n'
print v

"""
L = Matrix([[ 2, -1, -1,  0,  0,  0,],
     [-1,  3,  0, -1,  0, -1,],
     [-1,  0,  2, -1,  0,  0,],
     [ 0, -1, -1,  3, -1,  0,],
     [ 0,  0,  0, -1,  2, -1,],
     [ 0, -1,  0,  0, -1,  2,]])




print "eigenvalues:"
print pretty(L.eigenvals())
print
print "eigenvectors:"
print pretty(L.eigenvects(), num_columns=132)
"""
