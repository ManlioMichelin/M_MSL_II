import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('musei.xml').getroot()
for atype in e.findall('item'):
	print(atype.find('name').text)
