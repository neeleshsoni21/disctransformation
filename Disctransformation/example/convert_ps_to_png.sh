
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


outdir=output_gpcr
#outdir="output_gpcr"
start=0
end=179

mkdir ./$outdir/pngs/

for (( i=$start; i<=$end; i++ ))
do  
	#echo ./"$outdir"/Disc_Mdl_"$i".ps ./"$outdir"/pngs/Disc_Mdl_"$i".png
	convert -density 500 ./"$outdir"/Disc_Mdl_"$i".ps ./"$outdir"/pngs/Disc_Mdl_"$i".png
done
