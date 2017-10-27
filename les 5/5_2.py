def toonkaartnummers():
    'print naam geeft kaartnummer'
infile=open("kaartnummers.txt")
for regel in infile.readlines():
    nummer, naam =regel.split(',')
    print('{} heeft kaartnummer: : {}'.format(naam, nummer))







