""""""
################################################################################
#   Copyright (C) 2016 Neelesh Soni <neeleshsoni03@gmail.com>, 
#   <neelesh.soni@alumni.iiserpune.ac.in>
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
################################################################################

 
#import Tkinter as Tk
#from tkinter import Tk
import tkinter as Tk
#import Image, ImageDraw
#import ImageTk
import random
from PIL import Image

class Print_Disc_Model:

	"""Summary
	"""
	
	def __init__(self,d,bdm):
		"""Summary
		
		Args:
		    d (TYPE): Description
		    bdm (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		#self.__CANVAS_WIDTH = 740;
		#self.__CANVAS_HEIGHT = 780;
		self.__TITLE = "  Disc Transformation";
		self.__discs=d;
		
		self.__nod=bdm.get_nod();
		self.__drad=bdm.get_drad();
		self.__dbwd=bdm.get_dbwd();

		self.__modes=bdm.get_arguments()['@ARG5']
		self.__labelarg = bdm.get_arguments()['@ARG4']

		self.__CANVAS_WIDTH = 2*self.__nod*(self.__drad*2);
		self.__CANVAS_HEIGHT = 2*self.__nod*(self.__drad*2);
		

		return
	
		
	'''
	 * This method generates the graphical output and prints out
	 * the cutoff and other values to the standard input output.
	 * @param g2d1 Graphics object
	 * @param d discstructure object
	 '''
	def printdata(self,d,fname,score_obj):
		"""Summary
		
		Args:
		    d (TYPE): Description
		    fname (TYPE): Description
		    score_obj (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		self.Drawfinal_structure(d,0,int(self.__nod),fname,score_obj);
		
		return
	
	
	def _create_circle(self, x, y, r, **kwargs):
		"""Summary
		
		Args:
		    x (TYPE): Description
		    y (TYPE): Description
		    r (TYPE): Description
		    **kwargs: Description
		
		Returns:
		    TYPE: Description
		"""
		return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
	Tk.Canvas.create_circle = _create_circle

	def _create_circle_arc(self, x, y, r, **kwargs):
		"""Summary
		
		Args:
		    x (TYPE): Description
		    y (TYPE): Description
		    r (TYPE): Description
		    **kwargs: Description
		
		Returns:
		    TYPE: Description
		"""
		if "start" in kwargs and "end" in kwargs:
			kwargs["extent"] = kwargs["end"] - kwargs["start"]
			del kwargs["end"]
		return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
	Tk.Canvas.create_circle_arc = _create_circle_arc
	
	def write_label(self,canvas,x,y,string):
		"""Summary
		
		Args:
		    canvas (TYPE): Description
		    x (TYPE): Description
		    y (TYPE): Description
		    string (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		canvas.create_text(x,y,font="calibri 12 bold underline",text=string)
		return canvas

	def save_as_pdf(self,canvas,fname):
		"""Summary
		
		Args:
		    canvas (TYPE): Description
		    fname (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		# save postscipt image
		canvas.postscript(file=fname, height=self.__CANVAS_HEIGHT, width=self.__CANVAS_WIDTH, colormode="color")
		
		return

	def save_as_png(self,canvas,fname):
		"""Summary
		
		Args:
		    canvas (TYPE): Description
		    fname (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		#canvas.scale("all",0,0,2,2)
		# save postscipt image
		#canvas.postscript(file=fname, height=400, width=400, colormode="color")
		
		#from pdf2image import convert_from_path

		#pages = convert_from_path(fname+'.eps')

		#img = Image.open(fname+'.eps')
		#img.save(fname+'.png','png')

		#pages[0].save(fname+'.png')

		return

	def DrawInteractingSites(self,canvas,discx):
		"""Summary
		
		Args:
		    canvas (TYPE): Description
		    discx (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		if len(discx.Get_InteractingSites()[0])==0:
			return

		
		#print("Inside Draw",np.mean(discx.Get_InteractingSites()[1]))
		canvas.create_circle(discx.Get_InteractingSites()[3][0],discx.Get_InteractingSites()[3][1], self.__drad*0.1,fill="white", outline="black", width=0.01*self.__drad)

		XCoord,YCoord = discx.Get_InteractingSites()[0],discx.Get_InteractingSites()[1]
		
		for x,y in zip(XCoord[1:],YCoord[1:]):
			canvas.create_circle(x,y,self.__drad*0.05,fill="gray", outline="", width=0.01*self.__drad)

		canvas.create_circle(XCoord[0],YCoord[0],self.__drad*0.05,fill="blue", outline="", width=0.01*self.__drad)
		canvas.create_circle(XCoord[-1],YCoord[-1],self.__drad*0.05,fill="red", outline="", width=0.01*self.__drad)

		return
	
	def Drawfinal_structure(self,d,str1,end,fname,score_obj):
		"""Summary
		
		Args:
		    d (TYPE): Description
		    str1 (TYPE): Description
		    end (TYPE): Description
		    fname (TYPE): Description
		    score_obj (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		from numpy import cross, dot, arctan2, array
		
		#print fname
		
		root = Tk.Tk()
		canvas = Tk.Canvas(root, width=self.__CANVAS_WIDTH, height=self.__CANVAS_HEIGHT, borderwidth=0, highlightthickness=0, bg="white")
		canvas.grid()

		#Print all mode positions
		#for c in score_obj.get_mode_positions():
		#	canvas.create_circle(c[0],c[1], score_obj.get_probe(),fill="blue",  outline="black", width=0.5)

		#Print all accessible regions
		for c in score_obj.get_accessibility():
			canvas.create_circle(c[0],c[1], score_obj.get_probe(),fill="pink",  outline="black", width=0.5)
		
		#Get default contrasting colors unles number of colors required is more than 4
		colors = ['yellow','blue','cyan','white']
		number_of_colors = len(self.__modes.keys());
		if number_of_colors>4:
			colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(number_of_colors)]
		


		for i in range(str1,end):

			#print("disc idx:",i)

			xcord1=d[i].p();
			ycord1=d[i].q();
			xcord2=d[i].r();
			ycord2=d[i].s(); 
			
			x1=float(d[i].p() - (self.__drad/3)*d[i].l());
			y1=float(d[i].q() - (self.__drad/3)*d[i].m());
			
			a= array([d[0].r()-d[0].p() , d[0].s()-d[0].q()])
			b= array([d[i].r()-d[i].p() , d[i].s()-d[i].q()])
			angle=arctan2( cross(a,b) , dot(a,b))  * 180 / 3.14159 
			#offset=90;
			
			if(d[i].dvec()==1):
				
				canvas.create_circle(xcord1,ycord1, self.__drad,fill="green",  outline="black", width=0.09*self.__drad)
				canvas.create_line(xcord1,ycord1,xcord2,ycord2,width=0.09*self.__drad)
				
				
				self.DrawInteractingSites(canvas,d[i])
					
				for cidx,mvalues in enumerate(self.__modes.values()):

					M1 = float(mvalues[0]);M2 = float(mvalues[1])
					#Print regular mode value arc
					canvas.create_circle_arc(xcord1,ycord1, self.__drad-self.__drad*((1+cidx)*0.1),style="arc",fill="",  outline=colors[cidx], width=0.09*self.__drad, start=90-M1-angle-5, end=90-M1-angle+5)
					#Print reverse mode value arc
					#canvas.create_circle_arc(xcord1,ycord1, self.__drad-5,style="arc",fill="blue",  outline=colors[cidx], width=3, start=90-(180-M2)-angle-5, end=90-(180-M2)-angle+5)
				

				"""
				M1 = float(self.__modes['A'][0]); M2 = float(self.__modes['A'][1])
				canvas.create_circle_arc(xcord1,ycord1, self.__drad-5,style="arc",fill="blue",  outline="blue", width=3, start=90-M1-angle-5, end=90-M1-angle+5)
				canvas.create_circle_arc(xcord1,ycord1, self.__drad-5,style="arc",fill="blue",  outline="blue", width=3, start=90-(180-M2)-angle-5, end=90-(180-M2)-angle+5)
				
				#from numpy import cos, sin
				#pif=-3.1416/180.0
				#canvas.create_circle(xcord1+self.__drad*cos((90-M1-angle)*pif),ycord1+self.__drad*sin((90-M1-angle)*pif), 5,fill="blue",  outline="yellow", width=1)
				#canvas.create_circle(xcord1+self.__drad*cos((90-(180-M2)-angle)*pif),ycord1+self.__drad*sin((90-(180-M2)-angle)*pif), 5,fill="blue",  outline="yellow", width=1)


				M1 = float(self.__modes['B'][0]); M2 = float(self.__modes['B'][1])
				canvas.create_circle_arc(xcord1,ycord1, self.__drad-5.5,style="arc",fill="blue",  outline="yellow", width=3, start=90-M1-angle-5, end=90-M1-angle+5)
				canvas.create_circle_arc(xcord1,ycord1, self.__drad-5.5,style="arc",fill="blue",  outline="yellow", width=3, start=90-(180-M2)-angle-5, end=90-(180-M2)-angle+5)
				
				#M1 = float(self.__modes['C'][0]); M2 = float(self.__modes['C'][1])
				#canvas.create_circle_arc(xcord1,ycord1, self.__drad-6,style="arc",fill="blue",  outline="purple", width=3, start=90-M1-angle-5, end=90-M1-angle+5)
				#canvas.create_circle_arc(xcord1,ycord1, self.__drad-6,style="arc",fill="blue",  outline="purple", width=3, start=180+90-M2-angle-5, end=180+90-M2-angle+5)
				"""

			else:
				canvas.create_circle(xcord1,ycord1, self.__drad,fill="red",  outline="black", width=0.09*self.__drad)
				canvas.create_line(xcord1,ycord1,xcord2,ycord2,width=0.09*self.__drad)
				
				self.DrawInteractingSites(canvas,d[i])

				for mvalues in self.__modes.values():
					M1 = float(mvalues[0]);M2 = float(mvalues[1])
					#Print regular mode value arc
					canvas.create_circle_arc(xcord1,ycord1, self.__drad-self.__drad*((1+cidx)*0.1),style="arc",fill="",  outline=colors[cidx], width=0.09*self.__drad, start=90+(M1-angle)-5, end=90+(M1-angle)+5)
					#Print reverse mode value arc
					#canvas.create_circle_arc(xcord1,ycord1, self.__drad-5,style="arc",fill="blue",  outline="blue", width=3, start=90+(180-M2)-angle-5, end=90+(180-M2)-angle+5)
				
				"""
				#angle2=360-angle 
				M1 = float(self.__modes['A'][0]); M2 = float(self.__modes['A'][1])
				canvas.create_circle_arc(xcord1,ycord1, self.__drad-5,style="arc",fill="blue",  outline="blue", width=3, start=90+(M1-angle)-5, end=90+(M1-angle)+5)
				canvas.create_circle_arc(xcord1,ycord1, self.__drad-5,style="arc",fill="blue",  outline="blue", width=3, start=90+(180-M2)-angle-5, end=90+(180-M2)-angle+5)

				#from numpy import cos, sin
				#pif=-3.1416/180.0
				#canvas.create_circle(xcord1+self.__drad*cos((90+(M1-angle))*pif),ycord1+self.__drad*sin((90+(M1-angle))*pif), 5,fill="blue",  outline="yellow", width=1)
				#canvas.create_circle(xcord1+self.__drad*cos((90+(180-M2)-angle)*pif),ycord1+self.__drad*sin((90+(180-M2)-angle)*pif), 5,fill="blue",  outline="yellow", width=1)
				

				M1 = float(self.__modes['B'][0]); M2 = float(self.__modes['B'][1])
				canvas.create_circle_arc(xcord1,ycord1, self.__drad-5.5,style="arc",fill="blue",  outline="yellow", width=3, start=90+(M1-angle)-5, end=90+(M1-angle)+5)
				canvas.create_circle_arc(xcord1,ycord1, self.__drad-5.5,style="arc",fill="blue",  outline="yellow", width=3, start=90+(180-M2)-angle-5, end=90+(180-M2)-angle+5)

				#M1 = float(self.__modes['C'][0]); M2 = float(self.__modes['C'][1])
				#canvas.create_circle_arc(xcord1,ycord1, self.__drad-6,style="arc",fill="blue",  outline="purple", width=3, start=90+(M1-angle)-5, end=90+(M1-angle)+5)
				#canvas.create_circle_arc(xcord1,ycord1, self.__drad-6,style="arc",fill="blue",  outline="purple", width=3, start=180+90+M2-angle-5, end=180+90+M2-angle+5)
				"""
				
				
			if self.__labelarg=='yes':
				canvas=self.write_label(canvas,x1,y1,str(i));
		
		#canvas.postscript(file=fname, height=self.__CANVAS_HEIGHT, width=self.__CANVAS_WIDTH, colormode="color")
		self.save_as_pdf(canvas,fname);
		print("Sample Representation saved in;",fname)
		#Use external script to convert into image
		#self.save_as_png(canvas,fname)
		
		
		#COMMENT THIS IF U DONT WANT TO DISPLAY CANVAS
		#root.wm_title("Disctransformation")
		#root.mainloop()
		return