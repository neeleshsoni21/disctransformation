'''
Copyright (C) 2012 Neelesh Soni <neelesh.soni@alumni.iiserpune.ac.in>
This file is part of DiscTransformation.

DiscTransformation is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

DiscTransformation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with DiscTransformation.  If not, see <http:#www.gnu.org/licenses/>.
'''

from discstructure import discstructure
from transformation import transformation
import sys,math
class Build_Disc_Model:
    
    def __init__(self,args):
        
        self.__argsg = ""
        
        #Initial position of the first disc
        self.__x = 250.0
        self.__y = 250.0
        #Disc radius (Default 20)
        self.__drad = 0
        #Distance between the succeeding disc (distance between the circumference) (Default 2)
        self.__dbwd=0;
        
        #Number of Discs (Default 10)
        self.__nod=0;
        
        self.__mindist=0;
        self.__maxdist=0;
        
        self.__argsg=self.read_arguments(args)
        
        self.__drad=float(self.__argsg[1]);
        self.__dbwd=float(self.__argsg[2]);
        self.__nod=int(self.__argsg[0]);
                
        
        return
    def read_arguments(self,args):
        #Create an array list for storing input arguments.
        argt = []
        argsArray = [];
        tokens = [];
        try:
            #print args[0]
            br=open(args[1],'r');
            #Read File Line By Line
            for strLine in br.readlines():
                n_strLine=strLine.strip();
                #Skip if line is empty
                if len(n_strLine)!=0:
                    #Skip if line starts with '#'
                    if n_strLine[0]!='#':
                        #Parse the line with space OR multiple spaces as delimiter
                        tokens = strLine.split(' ');
                        for tk in tokens:
                            argt.append(tk.strip());
        
            br.close();
        
        except IOError:#Catch exception if any
            print("Error: ");
        
        #Return parameter passed through input file
        return argt
        
    def build_disc(self):
        #Initialize discs
        d=[]
        for i in range(0,self.__nod):
            d.append(discstructure());
        
        
        T= transformation();
        #Create starting disc at the position given by x,y
        d[0].init_new_starting_disc(d[0],self.__x,self.__y,self.__drad);
        
        #Create succeeding discs
        
        for i in range(4,len(self.__argsg)-4,6):
            a1=int(self.__argsg[i]);
            a2=int(self.__argsg[i+1]);
            a3=float(self.__argsg[i+2]);
            a4=float(self.__argsg[i+3]);
            a5=float(self.__argsg[i+4]);
            a6=float(self.__argsg[i+5]);
            M1 = [a3,a4,a5,a6];
            #If input disc number is less than total number of disc then generate the mode else exit
            
            if((a1<self.__nod) & (a2<self.__nod)):
                T.drawmode(d,a1,a2,self.__x,self.__y,M1,self.__drad,self.__dbwd);
            else:
                print "Error: Total number Discs in argument 1 is less than the numbers provided in input file!!!";
                sys.exit(0);
        
        return d
    def write_output_file(self,d, score_obj):
        line="#Disc Model representation using coordinates. \n"+"#This file gives discs coordinates in tab separated format.\n"+"#First column is the disc number. Second column gives the coordinates " +"#of the center of the disc. Third column gives the coordinates of the other point on \n" +"#the disc circumference. \n\n";
        for i in range(0,int(self.__argsg[0])):
            vec_c="("+str(round((d[i].p()-self.__x),1))+","+str(round((d[i].q()-self.__y),1))+")";
            vec_r="("+str(round((d[i].r()-self.__x),1))+","+str(round((d[i].s()-self.__y),1))+")"; 
            vec_n=str(i);
            rad_vec=vec_n+"\t"+vec_c+"\t"+vec_r+"\t"+str(d[i].dvec());
            line+=rad_vec+'\n';
        
        try:
            out=open('./output/Disc_Structure_Coordinates.txt','w');
            out.writelines(line);
            #Get score values
            out.writelines("\nModel Score is: ");
            model_score=score_obj.model_score()
            out.writelines(str(model_score))

            out.writelines("\nModel Clash Score is: ");
            clash_score=score_obj.clash_score()
            out.writelines(str(clash_score))
            
            out.writelines("\nModel radial density: ");
            radial_density=score_obj.radial_density()
            out.writelines(str(" ".join(radial_density)))
            
            out.writelines("\nModel Mean is: ");
            model_mean=score_obj.model_mean()
            out.writelines(str(" ".join(map(str,model_mean))))
            
            out.writelines("\nModel Max Distance is: ");
            max_dist=score_obj.max_dist()
            out.writelines(str(max_dist))
            #Close the output stream
            out.close();
        except IOError:#Catch exception if any
            print "Error: ";
        return
    def argsg(self):
        return self.__argsg
