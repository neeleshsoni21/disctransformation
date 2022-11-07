""""""
#####################################################################################
#   Copyright (C) 2016 Neelesh Soni <neeleshsoni03@gmail.com>, <neelrocks4@gmail.com>
#   
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#####################################################################################from numpy import log,exp,sqrt,mean,std,pi

'''
This function returns the Principal eigen vector, 
which is the best fit line to the coordinates of CA atoms.
The method returns the Direction Cosines of the unit 
vector in the direction of best fit line

Arguments: coordinate set of a chain

'''

def getorientation(coord_X):
    """Summary
    
    Args:
        coord_X (TYPE): Description
    
    Returns:
        TYPE: Description
    """
    from numpy.linalg import eig
    from numpy import array
    
    #Allocating coordinates and mean of coordinates
    x,y,z=[],[],[]
    mean_coord=[]
    
    #Extracting x,y,z values from coordinates to array
    for i in range(1,len(coord_X)):
        
        x.append(float(coord_X[i][0]))
        y.append(float(coord_X[i][1]))
        z.append(float(coord_X[i][2]))
    X,Y,Z=array(x),array(y),array(z)
    
    #Getting the mean coordinates
    x1=sum(X)/len(X);y1=sum(Y)/len(Y);z1=sum(Z)/len(Z)
    
    #Creating Sum of square matrix. Its Principal eigen\
    # vector will give best fit line unit vector
    T=array([[sum((X-x1)*(X-x1)),sum((X-x1)*(Y-y1)),sum((X-x1)*(Z-z1))],\
        [sum((Y-y1)*(X-x1)),sum((Y-y1)*(Y-y1)),sum((Y-y1)*(Z-z1))],\
        [sum((Z-z1)*X),sum((Z-z1)*Y),sum((Z-z1)*(Z-z1))]])
    
    #print T
    #Getting set of eigen value and eigen vectors
    evals,evects=eig(T)
    
    #getting the maximum eigen value from the set
    i = (evals).argmax()
    
    #extracting the eigen vector correspondind to the\
    # maximum eigen value
    pv = evects[:, i]
    #Getting the mean of X,Y,Z. This point will be the\
    # inital point for the best fit line
    mean_coord=[x1,y1,z1]
    return [pv,mean_coord]
    
    
