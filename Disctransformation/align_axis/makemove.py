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

import numpy as np

'''
This function generates the table for the X links satisfied for
different conformations originated by shear and rotation of each chain
Here axisA[0] argument gives unit vector along the orientation axis 
and axisA[1] gives the starting point of that vector
'''
def move(mdl,OM):
    """Summary
    
    Args:
        mdl (TYPE): Description
        OM (TYPE): Description
    
    Returns:
        TYPE: Description
    """
    minx=1000000;
    miny=1000000;
    minz=1000000;
    #maxx=-1000000;
    #maxy=-1000000;
    #maxz=-1000000;
    
    for i in range(0,mdl.iter_length()):
        coord=np.array([float(mdl.x()[i]),float(mdl.y()[i]),float(mdl.z()[i])])
        coord_A=coord*OM;
        mdl.x()[i]=coord_A.item(0);
        mdl.y()[i]=coord_A.item(1);
        mdl.z()[i]=coord_A.item(2);
        if mdl.x()[i] < minx:
            minx=mdl.x()[i];
        if mdl.y()[i] < miny:
            miny=mdl.y()[i];
        if mdl.z()[i] < minz:
            minz=mdl.z()[i];
        #if mdl.x()[i] > maxx:
        #    maxx=mdl.x()[i];
        #if mdl.y()[i] > maxy:
        #    maxy=mdl.y()[i];
        #if mdl.z()[i] > maxz:
        #    maxz=mdl.z()[i];
    
    #print (maxx,minx)
    #print (maxy,miny)
    #print (maxz,minz)
    
    for i in range(0,mdl.iter_length()):
        mdl.x()[i]=round(mdl.x()[i]-minx,3);
        mdl.y()[i]=round(mdl.y()[i]-miny,3);
        mdl.z()[i]=round(mdl.z()[i]-minz,3);
    
    return mdl
        
