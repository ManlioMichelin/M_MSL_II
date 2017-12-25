# open e' funzione predefinita
f=open('musei.xml','r')
# su f richiamo il metodo readline senza parametri
line=f.readline()
print line # print e' speciale e non richiede ()
print line
# In line e' compreso l'a-capo finale
