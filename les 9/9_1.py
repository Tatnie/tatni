try:
 aantal_mensen=input('Typ hier het aantal personen')
 intpersonen=4356/int(aantal_mensen)
 print('Je moet {} zoveel per persoon betalen'.format(intpersonen))


except ZeroDivisionError:
 print('delen door nu kan niet')

if aantal_mensen <0



