def seizoen(maandnummer):
    if maandnummer >= 2 and  maandnummer<= 5:
        return 'Lente'
    elif maandnummer >= 9 and maandnummer<=11:
        return 'herfst'
    elif maandnummer ==12 or maandnummer <=2:
        return 'winter'
    elif maandnummer >= 6 and maandnummer <= 8:
        return 'zomer'

print('Dit is ' + seizoen(8))





