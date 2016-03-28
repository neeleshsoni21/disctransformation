'''
Copyright (C) 2012 Neelesh Soni <neelesh.soni@alumni.iiserpune.ac.in>
This file is part of DiscTransformation.

DiscTransformation is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

DiscTransformation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with DiscTransformation.  If not, see <http:#www.gnu.org/licenses/>.
'''
import math
class discstructure:
    def __init__(self):
        #Coordinates of the discs centre and one of the po on the circumference
        self.__p = 0.0
        self.__q = 0.0
        self.__r = 0.0
        self.__s = 0.0
        #Direction cosines
        self.__l = 0.0
        self.__m = 0.0
        #Direction of the vector perpendicular to the surface
        self.__dvec = 0

        self.__fixed = 0;
        
        
        self.__theta1 = 0.0
        self.__theta2 = 0.0
        self.__shear = 0.0
        self.__aphase = 0.0
        

        return
    
    
    '''
    * This method initialised the initial disc with coordinates.
    * @param x x position
    * @param y y position
    * @param drad disc radius
    * @param vec disc vector 0/1
    '''
    def initdisc(self,x, y, drad, vec):
        #Describes two pos of the radius vector
        self.__p=x;self.__q=y;self.__r=x;self.__s=y-drad;
        
        
        
        return
    
    '''
    * This method initialises all the discs except the first disc. This is because
    * all the disc except the first one should be initialised with respect to the previous disc.
    * @param d discstructure object
    * @param drad disc radius
    * @param x x position
    * @param y y position
    * @param vec next disc vector
    '''
    def initnxtdisc(self, d,  drad,  dbwd,  x,  y, vec):
        
        disb=dbwd;
        self.__p=d.p() + (2*drad+disb)*d.l();self.__q=d.q() + (2*drad+disb)*d.m();
        self.__r=d.r() + (2*drad+disb)*d.l();self.__s=d.s() + (2*drad+disb)*d.m();
        self.__l=d.l();self.__m=d.m();
        self.__dvec=vec;
        
        #this.drad=drad;
        
        return
    
    '''
    * This method calculates the direction cosines of the radius vector of the disc
    '''
    def getdc(self):
        self.__l=(self.__r-self.__p)/(math.sqrt(math.pow((self.__r-self.__p), 2)+math.pow((self.__s-self.__q), 2)));
        self.__m=(self.__s-self.__q)/(math.sqrt(math.pow((self.__r-self.__p), 2)+math.pow((self.__s-self.__q), 2)));
        
        return
    
    '''
    * This method defines the shape and length of the disc radius vector as polygon
    * @return the shape of the discs
    '''
    '''public Shape defineshape():
        [] pXs = { () p, () rreturn;
        [] pYs = { () q, () sreturn;
        Shape shape = new Polygon(pXs, pYs, pXs.length);
        return shape;
    return
    '''
    '''
    * This method initialises the disc without giving the relative disc. 
    * It takes the disc position as arguments  
    * @param g2d Graphics object
    * @param d discstructure object
    * @param x x position
    * @param y y position
    * @param drad disc radius
    * @param CLR Colour of the disc
    '''
    def init_new_starting_disc(self, d, x, y, drad):
        d.initdisc(x,y,drad,1);
        d.set_dvec(1);
        d.set_aphase(0);
        d.set_shear(0);
        d.getdc();
        d.set_fixed(1);
        return
    
    '''
    * This method calculates the distance between each discs and returns the
    * minimum distance
    * @param d discstructure[], array containing all discs
    * @return dist - the minimum distance between all discs.
    '''
    '''Calculate_dist([] d) {
         dist=100000;
        #loop over all disc disc distances and return the least one
        for ( i=0;i<eger.valueOf(argsg[0]);i++):
            for ( j=i+1;j<eger.valueOf(argsg[0]);j++):
                 dis=distance(d[i],d[j]);
                if (dis < dist):
                    dist=dis;
                return
            return
        return
        return dist;
    return'''
    
    def theta1(self):
        return self.__theta1
    
    def theta2(self):
        return self.__theta2
        
    def shear(self):
        return self.__shear
    
    def aphase(self):
        return self.__aphase
    
    def p(self):
        return self.__p
    
    def q(self):
        return self.__q
    def r(self):
        return self.__r
    def s(self):
        return self.__s
        
    def l(self):
        return self.__l
    def m(self):
        return self.__m
    
    def dvec(self):
        return self.__dvec
    
        
    
    def set_theta1(self,val):
        self.__theta1=val
    
    def set_theta2(self,val):
        self.__theta2=val
        
    def set_shear(self,val):
        self.__shear=val
    
    def set_aphase(self,val):
        self.__aphase=val
    
    def set_p(self,val):
        self.__p=val
    
    def set_q(self,val):
        self.__q=val
    def set_r(self,val):
        self.__r=val
    def set_s(self,val):
        self.__s=val
        
    def set_l(self,val):
        self.__l=val
    def set_m(self,val):
        self.__m=val
    
    def set_dvec(self,val):
        self.__dvec=val
    def set_dcolor(self,val):
        self.__dcolor=val

    def set_fixed(self,flag):
        self.__fixed=flag

    def fixed(self):
        return self.__fixed


        
