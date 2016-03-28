'''
Copyright (C) 2012 Neelesh Soni <neelesh.soni@alumni.iiserpune.ac.in>
This file is part of DiscTransformation.

DiscTransformation is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

DiscTransformation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with DiscTransformation.  If not, see <http:#www.gnu.org/licenses/>.
'''

'''
 * @author Neelesh Soni
 * This is the main class for DISC TRANSFORMATION.
 * 
 '''
class DiscTransformation:
        
    def __init__(self):
        self.__clash_score=0;
        self.__model_score=0;
        self.__model_mean=[]
        self.__radial_density=[]
        self.__max_dist=0
        return
    
    def main(self,args):
        
        #Setup Disc model environment variables through constructor
        bdm=Build_Disc_Model(args);
        
        
        #Build disc models
        discs=bdm.build_disc();
        
        #Get the disc state object
        ds=disc_state(bdm,discs);
        
        #Score the models
        score_obj=Score_Model(bdm.argsg(),ds,discs);
        
        
        
        #Write the text output file of the model  
        bdm.write_output_file(discs,score_obj);
        
        #Setup environment variables for graphics frame through constructor
        pdm=Print_Disc_Model(discs,bdm.argsg());
        
        #Write ps output
        pdm.printdata(discs,bdm.argsg()[len(bdm.argsg())-3]);
        
        return discs,bdm

    def print_model(self,discs,bdm):
        #Setup environment variables for graphics frame through constructor
        pdm=Print_Disc_Model(discs,bdm.argsg());
        
        #Write ps output
        pdm.printdata(discs,bdm.argsg()[len(bdm.argsg())-3]);
        return

    def clash_score(self):
        return self.__clash_score;

    def model_score(self):
        return self.__model_score;

    def model_mean(self):
        return self.__model_mean

    def radial_density(self):
        return self.__radial_density

    def max_dist(self):
        return self.__max_dist


from Build_Disc_Model import Build_Disc_Model
from disc_state import disc_state
from Score_Model import Score_Model
from Print_Disc_Model import Print_Disc_Model
import sys


mdl=DiscTransformation()

mdl.main(sys.argv)
#OR
#mdl.main(['','./input/sample_input_2.txt'])



