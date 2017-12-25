import sys
import xml.etree.ElementTree
if len(sys.argv)!=2:
	print 'Errore nei parametri: manca il nome file'
	sys.exit()
e = xml.etree.ElementTree.parse(sys.argv[1]).getroot()
for atype in e.findall('item'):
	print(atype.find('name').text)


