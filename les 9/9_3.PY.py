#bestand moet geopent worden en gesloten.
#hij moet weten welke wat de hoogste score is en deze printen. Hetzelfde geld voor de speeldatum en de naam.
import gamers.csv
with open('gamers.txt', 'r') as gamersfile:
    reader=csv.reader(gamersfile, delimiter=';')
highscore=0

for row in reader:
    print(''"hoogste score" {}, "datum" {}, "naam" {}''.format(hoogstescore, datum, naam)







