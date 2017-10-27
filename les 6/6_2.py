#maak een lijst, om de waarden in op te slaan
lijst_van_inputs = eval(input('geef een woord:'))
lijst_van_uitvoer = []
#herhaal de volgende handeling 10 keer
for gegeven_woord in lijst_van_inputs:
    #controleer of het woord vier letters lang is
    if len(gegeven_woord) == 4:
        #als het woord vier letters lang is,
        # voeg het toe aan de lijst
        lijst_van_uitvoer.append(gegeven_woord)

#toon de lijst
print(lijst_van_uitvoer)
















