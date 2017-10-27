def gemiddelde():
    willeukeurigezin=input('doe maar een zin')
    Allewoorden=willeukeurigezin.strip.()split()
    aantalwoorden=len(allewoorden)
    accumulator=0
    for woord in allewoorden:
        accumulator += len(woord)

    print('De gemiddelde lengte van het aantal woorden in deze zin: {}'.format(gem))

