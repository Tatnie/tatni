# 6_3.py
invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst_2=sorted(str(invoer))

print('Gesorteerde list van ints: '+ str(lijst_2))

print('grootste getal:', +max(lijst_2),'en kleinste getal is:' + min(lijst_2))

print('Aantal getallen', + len(invoer), 'en som van de getallen' + sum(invoer))

print('Het gemiddelde:', +sum(invoer)/len(invoer))

#hoe krijg ik die '-' weg in lijst_2?. Ik heb geprobeerd om lijst_3=lijst_2.remove('-') te maken. Maar als ik het dan print staat er none.


#6_5.py
def tafels(uitkomst):
    res=0
    for i in range(1,10):
        res=+i*i
        return res

#ik heb nu zo gedaan en heb geen idee of dit goed is. Ik weet ook niet hoe ik dit moet printen.

