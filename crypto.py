#!/usr/bin/python
f = open("./crypto0.txt",'r')
g = open("./crypto1.txt",'r')
h = open("./crypto2.txt",'r')
line = f.read()
lin0 = g.read()
lin1 = h.read()
line0 = line.replace(",","\n")
line1 = lin0.replace(",","\n")
line2 = lin1.replace(",","\n")

f.close()
g.close()
h.close()

f = open("./crypto0.txt",'w')
g = open("./crypto1.txt",'w')
h = open("./crypto2.txt",'w')

for i in line0:
	f.write("%s" % i)
for i in line1:
	g.write("%s" % i)
for i in line2:
	h.write("%s" % i)

f.close()
g.close()
h.close()
