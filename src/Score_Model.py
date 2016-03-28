'''
Copyright (C) 2012 Neelesh Soni <neelesh.soni@alumni.iiserpune.ac.in>
This file is part of DiscTransformation.

DiscTransformation is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

DiscTransformation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with DiscTransformation.  If not, see <http:#www.gnu.org/licenses/>.
'''

import math
from numpy import pi
class Score_Model:
    
    def __init__(self,argsg,ds,d):
        
        self.__discs = d;
        self.__ds=ds;
        self.__argsg=argsg;
        self.__shear_steps=5;
        self.__theta1_steps=10;
        self.__theta2_steps=10;
        
        self.__clash_score=0;
        self.__model_score=0;
        
        self.__model_mean=[-100000,-100000];
        
        self.__radial_density=[];
        self.__max_dist=0;

        self.__relax_min_dist=0;
        self.__Modes = []

        #THIS will be helpful if you have a constrained moves between the discs
        #self.read_allowed_states(self.__argsg[len(self.__argsg)-3]);
                
        #Use below if you need to find the clash between last disc added with all remaining self.__discs
        #self.__status=self.clash_finding_function_last_vs_all();
        
        #Following gives the compactness and clash scores
        #self.__status=self.compactness_finding_function_first_last_disc();
        #self.__status=self.clash_and_compactness_finding_function_for_last_disc();
        #self.__status=self.compactness_finding_function();

        self.scoring_function(ds)

        #Use below if find you need to find the clash between all self.__discs
        self.__clash_score=self.clash_finding_function_all_vs_all();
        if self.__clash_score ==  1:
            self.radial_dist_function();
        
    #Calculate the distance of all discs from the model mean. This is used for getting the compactness in the structure
    def radial_dist_function(self):
        
        for i in range(0,len(self.__discs)):
            distance=math.sqrt((self.__model_mean[1]-self.__discs[i].q())*(self.__model_mean[1]-self.__discs[i].q()) + (self.__model_mean[0]-self.__discs[i].p())*(self.__model_mean[0]-self.__discs[i].p()));
            self.__radial_density.append(str(int(distance*10)/10.0));
            if distance > self.__max_dist:
                self.__max_dist=distance;
                
        self.__max_dist=(int(self.__max_dist*10)/10.0)

        return;


    #This module calculates the clashes between all discs and determines the model mean
    def clash_finding_function_all_vs_all(self):
        
        tot_disc=len(self.__discs);

        relax_min_dist=float(self.__argsg[len(self.__argsg)-1]);
        sum_x=0;
        sum_y=0;
        for i in range(0,tot_disc):
            sum_x+=self.__discs[i].p();
            sum_y+=self.__discs[i].q();
            for j in range(0,tot_disc):
                if(i!=j):
                    distance=math.sqrt((self.__discs[j].q()-self.__discs[i].q())*(self.__discs[j].q()-self.__discs[i].q()) + (self.__discs[j].p()-self.__discs[i].p())*(self.__discs[j].p()-self.__discs[i].p()));
                    if(distance <relax_min_dist):
                        return 0;
        avg_x=sum_x/tot_disc;
        avg_y=sum_y/tot_disc;
        avg_x=(int(avg_x*10)/10.0)
        avg_y=(int(avg_y*10)/10.0)
        self.__model_mean=[avg_x,avg_y]

        return 1;



    #This model determines the clashes and compactness for the last discs only
    def clash_and_compactness_finding_function_for_last_disc(self):
        
        relax_min_dist=float(self.__argsg[len(self.__argsg)-1]);
        radius=float(self.__argsg[1]);
        gap=float(self.__argsg[2]);
        
        #j is the last disx index
        j=len(self.__discs)-1;
        #dist between first and last disk
        dfl=0;
        Total_dimers=16;
        #Tolerance for compactness which is equal to 1 disc + 1 gap
        tolerance=1*(2*radius+gap);
        for i in range (len(self.__discs)-3,0,-1):
            distance=math.sqrt((self.__discs[j].q()-self.__discs[i].q())*(self.__discs[j].q()-self.__discs[i].q()) + (self.__discs[j].p()-self.__discs[i].p())*(self.__discs[j].p()-self.__discs[i].p()));
            dfl=distance;
            if(distance <relax_min_dist):
                #Model has clash return zero
                return 0;
        IMD=(Total_dimers-j)*(2*radius+gap);
        if (IMD +tolerance < dfl):
            return 0;
                
        return 1;
    
    #This module determnine the camnpactness for the first and the lasdt discs
    def compactness_finding_function_first_last_disc(self):
        
        relaxed_max_distance=float(self.__argsg[len(self.__argsg)-2])+20;
        i=0;
        j=len(self.__discs)-1;
        distance=math.sqrt((self.__discs[j].q()-self.__discs[i].q())*(self.__discs[j].q()-self.__discs[i].q()) + (self.__discs[j].p()-self.__discs[i].p())*(self.__discs[j].p()-self.__discs[i].p()));
        
        if(distance >relaxed_max_distance):
            #Model not compact
            return 0;
           
        return 1;
    
    #Determine the clash of the last dics vs the all
    def clash_finding_function_last_vs_all(self):
        
        relax_min_dist=float(self.__argsg[len(self.__argsg)-1]);
        for i in range(0,len(self.__discs)-1):
            j=len(self.__discs)-1;
            distance=math.sqrt((self.__discs[j].q()-self.__discs[i].q())*(self.__discs[j].q()-self.__discs[i].q()) + (self.__discs[j].p()-self.__discs[i].p())*(self.__discs[j].p()-self.__discs[i].p()));
            if(distance <relax_min_dist):
                return 0;
                   
                
        return 1;
    
        
    #This the scoring fucntion which takes care of the allowed states and then score the model
    def scoring_function(self,ds):
        relax_max_dist=float(self.__argsg[len(self.__argsg)-2]);
        relax_min_dist=float(self.__argsg[len(self.__argsg)-1]);

        for i in range(0,len(self.__discs)):
            for j in range(0,len(self.__discs)):
                if(i!=j):
                    score1,score2=0,0

                    distance=math.sqrt((self.__discs[j].q()-self.__discs[i].q())*(self.__discs[j].q()-self.__discs[i].q()) + (self.__discs[j].p()-self.__discs[i].p())*(self.__discs[j].p()-self.__discs[i].p()));
                    if(distance >=relax_min_dist):
                        if(distance <= relax_max_dist):
                            disc_state=ds.calculate_state(self.__discs[i],self.__discs[j]);
                            
                            #flag=search_allowed_state(disc_state);
                            #if (flag==true):
                            #    print "satisfy modes\n",i,j,disc_state[0];
                        else:
                            score1=self.gaussian_distance(self.__discs[i],self.__discs[j],relax_max_dist,3)[1];
                                
                    else:
                        score2=self.gaussian_distance(self.__discs[i],self.__discs[j],relax_min_dist,3)[1];
                        status=0;
                        print "Clashed Structure";
                        exit(status);
                        
                
        #Score
        #abs_phase=gaussian_phase(self.__discs[0],self.__discs[3],200,3)[1];
        
        self.__model_score=score1+score2

        
        return 0;
    
        
    def roundupto_x(num,x):
        return math.floor((num + x/2.0) / x) * x;
        
    def search_allowed_state(disc_state):
        
        for value in Modes:
            nshear=roundupto_x(disc_state[0],shear_steps);
            ntheta1=roundupto_x(disc_state[1],theta1_steps);
            ntheta2=roundupto_x(disc_state[2],theta2_steps);
            if (nshear==value[0]):
                if (ntheta1==value[1]):
                    if (ntheta2==value[2]):
                        return true;
        return false;
        
        
    def harmonic_distance(d1,d2,k,mean):
        x=distance(d1, d2);
        score=0.5*k*(x-mean)*(x-mean);
        values=[x,score];
        return values;
        
    def harmonic_phase(d1,d2,k,mean):
        d1_p=d1.aphase;
        d2_p=d2.aphase;
        rel_p=math.abs(d1_p-d2_p);
        #Normalize the phase with 360 degrees so that score will not be increased to high values.
        #Mean and relative phase values after normalize will be in range (0,1)
        score=0.5*k*((rel_p-mean)/360)*((rel_p-mean)/360);
        values=[rel_p,score];
        return values;
        
    def gaussian_phase(self,d1,d2,mu,sigma):
        d1_p=d1.aphase;
        d2_p=d2.aphase;
        rel_p=math.abs(d1_p-d2_p);
        #Normalize the phase with 360 degrees so that score will not be increased to high values.
        #Mean and relative phase values after normalize will be in range (0,1)
        #score=0.5*k*((rel_p-mean)/360)*((rel_p-mean)/360);
        rel_p_s=(rel_p-mu)/sigma;
        mag=1/(sigma*math.sqrt(2 * math.PI));
        score_g=math.exp(-rel_p_s*rel_p_s / 2)*mag;
        #Inverting the gaussian curve so as to make score at mean minimum and adding magnitude to make it zero
        score=-1*score_g+mag;
        values=[rel_p,score];
        return values;
        
    def gaussian_distance(self,d1,d2,mu,sigma):
        x=self.distance(d1, d2);
        x_s=(x-mu)/sigma;
        mag=1/(sigma*math.sqrt(2 * pi));
        score_g=math.exp(-x_s*x_s / 2)*mag;
        #Inverting the gaussian curve so as to make score at mean minimum and adding magnitude to make it zero
        score=-1*score_g+mag;
        values=[x,score];
        return values;
        
    
    def distance(self,d1,d2):
        #calculate the euclidian distance between two self.__discs
        dis=math.sqrt((d2.q()-d1.q())*(d2.q()-d1.q()) + (d2.p()-d1.p())*(d2.p()-d1.p()));
        return dis;
        
    
    
    def read_allowed_states(self,filename):
        tokens = [];print filename
        try:
            
            line_count=0;
            br=open(filename,'r')
            #Read File Line By Line
            for strLine in br.readlines():
            
                #Skip if line is empty
                if (len(strLine.strip()) != 0):
                    #Skip if line starts with '#'
                    if (strLine[0]!='#'):
                        line_count+=1;
                        temp=[]
                        #Parse the line with space OR multiple spaces as delimiter
                        tokens = strLine.split("\t");
                        for i in range(0,len(tokens)):
                            #System.out.println(tokens[i]);
                            temp.append(float(tokens[i]));
                        self.__Modes.append(temp);
                                                            
            #Close the input stream
            br.close();
            
        except IOError:
            print "Error: ";
        return
        
    def clash_score(self):
        return self.__clash_score

    def model_score(self):
        return self.__model_score

    def model_mean(self):
        return self.__model_mean

    def radial_density(self):
        return self.__radial_density

    def max_dist(self):
        return self.__max_dist

        