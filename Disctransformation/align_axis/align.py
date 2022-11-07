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

def create_orientation_matrix(N):
    """Summary
    
    Args:
        N (TYPE): Description
    
    Returns:
        TYPE: Description
    """
    x = np.array([0,0,1])
    y = np.array([0,1,0])
    return
    
#N is normal vector passing through P
#let Tg be the vector st (Tg-P) is perpendicular to N
#DC's of (Tg-P) are (Tg-P)/np.sqrt(np.dot(Tg-P,Tg-P))
def get_arbitrary_perpendicular_vector(Ng,P):
    """Summary
    
    Args:
        Ng (TYPE): Description
        P (TYPE): Description
    
    Returns:
        TYPE: Description
    """
    #arbitrary point (1,2,z)
    Tg = np.array([1.0,2.0,0.0])
    K=Ng[0]*P[0] + Ng[1]*P[1] + Ng[2]*P[2]
    Tg[2] = (K - Ng[0]*Tg[0] - Ng[1]*Tg[1])/(Ng[2]);
    Tf=Tg-P
    return Tf
    
def main():
    """Summary
    
    Returns:
        TYPE: Description
    """
    v1 = np.array([2.0,2.0,1.0])
    v2 = np.array([3.0,1.0,2.0])
    N = v2-v1
    c=(v1+v2)/2.0
    
    T=get_arbitrary_perpendicular_vector(N,c);
    B=np.cross(T,N);
    #Normalize all vectors
    N = N/np.sqrt(np.dot(N,N));
    T = T/np.sqrt(np.dot(T,T));
    B = B/np.sqrt(np.dot(B,B));
    print (N, T, B, c)
    print(np.dot(T,N));
    print(np.dot(T,B));
    
    '''Z = np.array([0.0,0.0,0.0])
    b = np.array([0.0,0.0,0.0,1.0])
    
    x = np.matrix( ( T, N, B , Z) )
    OM = np.hstack((x, np.atleast_2d(b).T))
    '''
    OM = np.matrix((T, N, B))
    print (v1*OM)
    print ((v1*OM).item(2))
    return

if __name__ == '__main__':
    main()

