import subprocess
Process=subprocess.Popen(["iwlist","wlan0","scan"],stdout=subprocess.PIPE,universal_newlines=True)
out,err=Process.communicate()
new_l=out.split('\n')
#print new_l

x1,y1=0.7,0
x2,y2=8,0
x3,y3=4,10
import math

def Distance(RSSI,A,n):
	aux=RSSI-A	
	aux=(-1)*aux
	aux=float(aux)/(10*n)
	x=math.pow(10,aux)
	return x



cells=[]
dict_wifi={}

for i in range(0,20):
	dict_wifi[i]=[]
	#three_wifi[i]=[]

for line in new_l:
	line=line.lstrip()
	line=line.rstrip()
	"""if line.startswith("ESSID"):
		line2=line.split(":")
	 	if line2[1]=="shape of you"||line2[1]=="RealSteel"||line2[1]=="IIITS_ProjectLab":
			cells.append(line2[1])"""
	if line.startswith("Cell"):
		line1=line.split()
	#	print line1[4]
		cells.append(line1[4])		
	if line.startswith("ESSID"):
		line2=line.split(":")
	#	print line2[1]
		cells.append(line2[1])
	if line.startswith("Channel"):
		line3=line.split(":")
	#	print line3[1]
		cells.append(line3[1])	
	if line.startswith("Frequency"):
		line4=line.split(":")
		k=line4[1].split('(')
#		print k[0]
		cells.append(k[0])
	if line.startswith("Quality"):
		line5=line.split()
		#line6=line.split(' ')
		#line5=line.split("=")
		line6=line5[2].split("=")
	#	print line6[1]
		cells.append(line6[1])
#print cells
cells.reverse()
print cells

c=0
k=1
for i in range(0,len(cells)):
	if i%5==0:
		#print cells[i][0:len(cells[i])+1]
		if cells[i][0:len(cells[i])+1]=='"RealSteel"' or cells[i][0:len(cells[i])+1]=='"shape of you"' or cells[i][0:len(cells[i])+1]=='"IIITS_ProjectLab"':		
			print cells[i]+" ***"
			dict_wifi[c].append(cells[i])
			dict_wifi[c].append(cells[i+1])
			dict_wifi[c].append(cells[i+2])
			dict_wifi[c].append(cells[i+3])
			dict_wifi[c].append(cells[i+4])
			dict_wifi[c].append(str(Distance(int(cells[i+1]),-39,4)))
			c=c+1
			k=k+1			
						

print "S.No",'       ',"SSID",'      ',"RSSI(dBm)",'      ',"Freq",'      ',"Channel",'     ',"MAC",'         ',"Distance(mts)"


for i in dict_wifi.keys():
	if dict_wifi[i]!=[]:
		print i,'   ',
		print dict_wifi[i][0]
		for j in dict_wifi[i]: 
			
			print j,'    ',
		print '\n'


ln=[]
for h in dict_wifi.values():
	if h!=[]:
		print h,type(h)
		ln.append(float(h[5]))
print ln 


ind=[]
i=0
while(i<3):
	ind.append(ln.index(min(ln)))
	ln[ln.index(min(ln))]=max(ln)+1
	i+=1
print ind


#dist=[]
#for j in ind:
	#dist.append(float(dict_wifi[j][5])
	#print dict_wifi[j][0],float(dict_wifi[j][5])

three_wifi={}
for i in range(0,3):
	three_wifi[i]=[]


for i in dict_wifi.keys():
	if dict_wifi[i]!=[]:
		if dict_wifi[i][0]=='"RealSteel"':
			three_wifi[0].append(dict_wifi[i][0])
			three_wifi[0].append(dict_wifi[i][1])
			three_wifi[0].append(dict_wifi[i][2])
			three_wifi[0].append(dict_wifi[i][3])
			three_wifi[0].append(dict_wifi[i][4])
			three_wifi[0].append(dict_wifi[i][5])
for i in dict_wifi.keys():
	if dict_wifi[i]!=[]:
		if dict_wifi[i][0]=='"IIITS_ProjectLab"':
			three_wifi[1].append(dict_wifi[i][0])
			three_wifi[1].append(dict_wifi[i][1])
			three_wifi[1].append(dict_wifi[i][2])
			three_wifi[1].append(dict_wifi[i][3])
			three_wifi[1].append(dict_wifi[i][4])
			three_wifi[1].append(dict_wifi[i][5])
for i in dict_wifi.keys():
	if dict_wifi[i]!=[]:
		if dict_wifi[i][0]=='"shape of you"':
			three_wifi[2].append(dict_wifi[i][0])
			three_wifi[2].append(dict_wifi[i][1])
			three_wifi[2].append(dict_wifi[i][2])
			three_wifi[2].append(dict_wifi[i][3])
			three_wifi[2].append(dict_wifi[i][4])
			three_wifi[2].append(dict_wifi[i][5])
	
	
	







print three_wifi[0][0],three_wifi[1][0],three_wifi[2][0]

for i in three_wifi.keys():
	if three_wifi[i]!=[]:
		print i,'   ',
		#print three_wifi[i][0]
		for j in three_wifi[i]: 
			
			print j,'    ',
		print '\n'





d1=(x1**2)+(y1**2)-(float(three_wifi[ind[0]][5])**2)
d2=(x2**2)+(y2**2)-(float(three_wifi[ind[1]][5])**2)
d3=(x3**2)+(y3**2)-(float(three_wifi[ind[2]][5])**2)

import matplotlib.pyplot as pt
from sympy import *

pt.axis([-20,20,-20,20])
pt.plot(0.7,0,'bo')
pt.annotate(three_wifi[ind[0]][0]+'\n'+str(round(float(three_wifi[ind[0]][5]),2))+'mts',xy=(0.7,0),xycoords='data',xytext=(-30,+40),textcoords='offset points',fontsize=10,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))

pt.plot(8,0,'ro')
pt.annotate(three_wifi[ind[1]][0]+'\n'+str(round(float(three_wifi[ind[1]][5]),2))+'mts',xy=(8,0),xycoords='data',xytext=(+30,+40),textcoords='offset points',fontsize=10,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
pt.plot(4,10,'go') 
pt.annotate(three_wifi[ind[2]][0]+'\n'+str(round(float(three_wifi[ind[2]][5]),2))+'mts',xy=(4,10),xycoords='data',xytext=(+30,-40),textcoords='offset points',fontsize=10,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))

x,y=symbols('x,y',real=True)
print x,y
system=[(2*x*(x2-x1))+(2*y*(y2-y1))+d1-d2,(2*x*(x3-x1))+(2*y*(y3-y1))+d1-d3]

q={}
q=solve(system,x,y)
x=q[x]
y=q[y]
print x,y
pt.plot(x,y,'yo')
pt.annotate(r'You'+'\n'+'['+str(round(x,2))+','+str(round(y,2))+']',xy=(x,y),xycoords='data',xytext=(+0,-30),textcoords='offset points',fontsize=10,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))

pt.show()






