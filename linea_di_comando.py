
import sys
print 'Numero parametri: %d' % (len(sys.argv)-1)
print 'Parametri:'
for i in range(len(sys.argv)):
	print i,sys.argv[i]

