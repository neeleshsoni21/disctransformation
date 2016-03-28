'''
Copyright (C) 2012 Neelesh Soni <neelesh.soni@alumni.iiserpune.ac.in>
This file is part of DiscTransformation.

DiscTransformation is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

DiscTransformation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with DiscTransformation.  If not, see <http:#www.gnu.org/licenses/>.
'''
 
import Tkinter as tk
#import Image, ImageDraw
#import ImageTk

class Print_Disc_Model:
    
    def __init__(self,d,args_bdm):
        self.__CANVAS_WIDTH = 740;
        self.__CANVAS_HEIGHT = 780;
        self.__TITLE = "  Disc Transformation";
        self.__discs=d;
        self.__argsg=args_bdm;
        self.__nod=int(args_bdm[0]);
        self.__drad=int(args_bdm[1]);
        self.__dbwd=int(args_bdm[2]);
        
        return
    
        
    '''
     * This method generates the graphical output and prints out
     * the cutoff and other values to the standard input output.
     * @param g2d1 Graphics object
     * @param d discstructure object
     '''
    def printdata(self,d,fname):
        
        self.Drawfinal_structure(d,0,int(self.__nod),fname);
        
        return
    
    
    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    tk.Canvas.create_circle = _create_circle

    def _create_circle_arc(self, x, y, r, **kwargs):
        if "start" in kwargs and "end" in kwargs:
            kwargs["extent"] = kwargs["end"] - kwargs["start"]
            del kwargs["end"]
        return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
    tk.Canvas.create_circle_arc = _create_circle_arc
    
    def write_label(self,canvas,x,y,string):
        canvas.create_text(x,y,font="calibri 12 bold underline",text=string)
        return canvas
        
        
    
    def Drawfinal_structure(self,d,str1,end,fname):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=self.__CANVAS_WIDTH, height=self.__CANVAS_HEIGHT, borderwidth=0, highlightthickness=0, bg="white")
        canvas.grid()
        for i in range(str1,end):
            xcord1=d[i].p();
            ycord1=d[i].q();
            xcord2=d[i].r();
            ycord2=d[i].s(); 
            
            x1=float(d[i].p() - (self.__drad/3)*d[i].l());
            y1=float(d[i].q() - (self.__drad/3)*d[i].m());
            
            
            if(d[i].dvec()==1):
                
                canvas.create_circle(xcord1,ycord1, self.__drad,fill="green",  outline="black", width=2)
                canvas.create_line(xcord1,ycord1,xcord2,ycord2,width=2)
            else:
                canvas.create_circle(xcord1,ycord1, self.__drad,fill="red",  outline="black", width=2)
                canvas.create_line(xcord1,ycord1,xcord2,ycord2,width=2)
            canvas=self.write_label(canvas,x1,y1,str(i));
        
        canvas.postscript(file=fname, height=self.__CANVAS_HEIGHT, width=self.__CANVAS_WIDTH, colormode="color")
        
        
        #COMMENT THIS IF U DONT WANT TO DISPLAY CANVAS
        root.wm_title("Disctransformation")
        root.mainloop()
        return