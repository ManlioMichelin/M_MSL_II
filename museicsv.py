f=open('musei.csv','r')
line=f.readline()
while line:
	# Separo la linea in campi
	v=line.split(';')
	# Stampo il secondo campo (indice 1)senza ""
	print v[1].replace('"','')
	line=f.readline()
