'''
Copyright (C) 2012 Neelesh Soni <neelesh.s()oni@alumni.iiserpune.ac.in>
This file is part of DiscTransformation.

DiscTransformation is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

DiscTransformation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with DiscTransformation.  If not, see <http://www.gnu.org/licenses/>.
'''


import math
class transformation :
    '''
     * This method rotates the point C with angle theta with respect to pivot PV
     * @param C Point to rotate
     * @param PV Pivot point
     * @param theta angle to rotate
     * @return C return the new transformed coordinates
     '''
    def rotate(self,C, PV, theta):
        p=C[0]
        q=C[1]
        pvx=PV[0]
        pvy=PV[1];
        
        #Transform the axes
        p = p - pvx;
        q = q - pvy;
        
        #Rotate the point anticlockwise by theta
        pn=p*math.cos(math.radians(-theta)) - q*math.sin(math.radians(-theta));
        qn=p*math.sin(math.radians(-theta)) + q*math.cos(math.radians(-theta));
        #Transform the axes back
        p = pn + pvx;
        q = qn + pvy;
        
        C[0]=p;C[1]=q;
        return C;
    
    
    '''
     * This method translate a given point in the direction of direction cosines DC with distance dist2
     * @param C Point to translate
     * @param DC Direction cosines
     * @param dist2 distance to rotate
     * @return C return the new transformed coordinates 
     '''
    def translate(C, DC, dist2):
        
        #Translate the axes in the direction of Direction Cosines
        C[0]=C[0]+dist2*DC[0];
        C[0]=C[1]+dist2*DC[1];
        
        return C;
    
    
    '''
     * This method creates a mode (a particular orientation) between two disc by transformation
     * @param d discstructure
     * @param j index of the disc1 (first disc)
     * @param i index of the disc (next disc)
     * @param mode mode of orientation
     * @return discstructure return the modified discstructure object 
     '''
    def createmode(self,d, j,i,mode):
        if d[i].fixed()==0:
            if(d[j].dvec()==0):
                PV1 = [d[j].p(),d[j].q()];
                C11 = [d[i].p(),d[i].q()];
                #Rotate C11 wrt PV1 (clockwise)
                C11=self.rotate(C11, PV1, mode[0]);
                C21 = [d[i].r(),d[i].s()];
                #Rotate C21 wrt PV1 (clockwise)
                C21=self.rotate(C21, PV1, mode[0]);
                d[i].set_p(C11[0]);d[i].set_q(C11[1]);d[i].set_r(C21[0]);d[i].set_s(C21[1]);
                
                PV2 = [d[i].p(),d[i].q()];
                C12 = [d[i].r(),d[i].s()];
                #Rotate C12 wrt PV2 (anti-clockwise)
                C12=self.rotate(C12, PV2, 360-mode[1]);
                d[i].set_r(C12[0]);d[i].set_s(C12[1]);
                
                d[i].set_fixed(1);
                
                return d[i];
            else:
                PV1 = [d[j].p(),d[j].q()];
                C11 = [d[i].p(),d[i].q()];
                #Rotate C11 wrt PV1 (anti-clockwise)
                
                C11=self.rotate(C11, PV1, 360-mode[0]);
                C21 = [d[i].r(),d[i].s()];
                #Rotate C21 wrt PV1 (anti-clockwise)
                C21=self.rotate(C21, PV1, 360-mode[0]);
                d[i].set_p(C11[0]);d[i].set_q(C11[1]);d[i].set_r(C21[0]);d[i].set_s(C21[1]);
                
                PV2 = [d[i].p(),d[i].q()];
                C12 = [d[i].r(),d[i].s()];
                #Rotate C12 wrt PV2 (clockwise)
                C12=self.rotate(C12, PV2, mode[1]);
                d[i].set_r(C12[0]);d[i].set_s(C12[1]);
    
                d[i].set_fixed(1);
                
                return d[i];
        else:
            if(d[i].dvec()==0):
                PV1 = [d[i].p(),d[i].q()];
                C11 = [d[j].p(),d[j].q()];
                #Rotate C11 wrt PV1 (anti clockwise)
                C11=self.rotate(C11, PV1, 360-(180-mode[1]));
                C21 = [d[j].r(),d[j].s()];
                #Rotate C21 wrt PV1 (anti clockwise)
                C21=self.rotate(C21, PV1, 360-(180-mode[1]));
                d[j].set_p(C11[0]);d[j].set_q(C11[1]);d[j].set_r(C21[0]);d[j].set_s(C21[1]);
                
                PV2 = [d[j].p(),d[j].q()];
                C12 = [d[j].r(),d[j].s()];
                #Rotate C12 wrt PV2 (clockwise)
                C12=self.rotate(C12, PV2, mode[0]);
                d[j].set_r(C12[0]);d[j].set_s(C12[1]);
                
                d[j].set_fixed(1);
                
                return d[j];
            else:
                PV1 = [d[i].p(),d[i].q()];
                C11 = [d[j].p(),d[j].q()];
                #Rotate C11 wrt PV1 (clockwise)
                
                C11=self.rotate(C11, PV1, 180-mode[1]);
                C21 = [d[j].r(),d[j].s()];
                #Rotate C21 wrt PV1 (clockwise)
                C21=self.rotate(C21, PV1, 180-mode[1]);
                d[j].set_p(C11[0]);d[j].set_q(C11[1]);d[j].set_r(C21[0]);d[j].set_s(C21[1]);
                
                PV2 = [d[j].p(),d[j].q()];
                C12 = [d[j].r(),d[j].s()];
                #Rotate C12 wrt PV2 (anti-clockwise)
                C12=self.rotate(C12, PV2, 360-(180-mode[0]));
                d[j].set_r(C12[0]);d[j].set_s(C12[1]);
    
                d[j].set_fixed(1);
                
                return d[j];
        
                
    
    
    '''
     * This method draws the mode by calling create mode and assigning 
     * disc colour and calculating direction cosines
     * @param g Graphics object
     * @param d discstructure
     * @param j index of the former disc
     * @param i index of the later disc
     * @param x x position of the disc
     * @param y y position of the disc
     * @param mode relative mode between the disc 
     * @param drad disc radius
     * @param dbwd distance between the disc
     '''
    def drawmode(self,d, j,i, x,  y, mode,drad,dbwd):
        if d[i].fixed()==0:
            R=mode[2];
            d[i].set_theta1(mode[0]);
            d[i].set_theta2(mode[1]);
            
            #If mode created is anti parallel
            if (R==0):
                
                
                if(d[j].dvec()==1):
                    d[i].set_aphase(d[j].aphase()-mode[0]+mode[1]);
                    d[i].initnxtdisc(d[j],drad,dbwd,x,y,0);
                    d[i].getdc();
                    
                    
                    d[i].set_shear(d[j].shear()-mode[3]);
                
                else:
                    d[i].set_aphase(d[j].aphase()+mode[0]-mode[1]);        
                    d[i].initnxtdisc(d[j],drad,dbwd,x,y,1);
                    d[i].getdc();
                    
                    
                    d[i].set_shear(d[j].shear()+mode[3]);
                    
                
            #If mode created is parallel
            else:
                
                if(d[j].dvec()==1):
                    d[i].set_aphase(d[j].aphase()-mode[0]+mode[1]);
                    
                    d[i].set_shear(d[j].shear()-mode[3]);
                else:
                    d[i].set_aphase(d[j].aphase()+mode[0]-mode[1]);
                    
                    d[i].set_shear(d[j].shear()+mode[3]);
                
                
                
                d[i].initnxtdisc(d[j],drad,dbwd,x,y,d[j].dvec());
                d[i].getdc();
                
            T= transformation();
            d[i]=T.createmode(d,j,i,mode);
            
            d[i].getdc();
            d[j].getdc();
            
            #Make the angle positive by adding 360 degree to negative angle
            if(d[i].aphase()<0):
                d[i].set_aphase(360+d[i].aphase());
        
        else:
            R=mode[2];
            d[j].set_theta1(mode[0]);
            d[j].set_theta2(mode[1]);
            
            #If mode created is anti parallel
            if (R==0):
                
                
                if(d[i].dvec()==1):
                    d[j].set_aphase(d[i].aphase()-mode[0]+mode[1]);
                    d[j].initnxtdisc(d[i],drad,dbwd,x,y,0);
                    d[j].getdc();
                    
                    
                    d[j].set_shear(d[i].shear()-mode[3]);
                
                else:
                    d[j].set_aphase(d[i].aphase()+mode[0]-mode[1]);        
                    d[j].initnxtdisc(d[i],drad,dbwd,x,y,1);
                    d[j].getdc();
                    
                    
                    d[j].set_shear(d[i].shear()+mode[3]);
                    
                
            #If mode created is parallel
            else:
                
                if(d[i].dvec()==1):
                    d[j].set_aphase(d[i].aphase()-mode[0]+mode[1]);
                    
                    d[j].set_shear(d[i].shear()-mode[3]);
                else:
                    d[j].set_aphase(d[i].aphase()+mode[0]-mode[1]);
                    
                    d[j].set_shear(d[i].shear()+mode[3]);
                
                
                
                d[j].initnxtdisc(d[i],drad,dbwd,x,y,d[i].dvec());
                d[j].getdc();
                

            T= transformation();
            d[j]=T.createmode(d,j,i,mode);
            
            d[i].getdc();
            d[j].getdc();
            
            #Make the angle positive by adding 360 degree to negative angle
            if(d[j].aphase()<0):
                d[j].set_aphase(360+d[j].aphase());
            
                    
        
        
        
    


