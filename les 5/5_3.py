def analyseertKaartnummers():
    infile = open('kaartnummers.txt')
    regels = infile.readlines()
    infile.close()
    print('Deze file telt {} regels').format(len(regels))
    nummers = ()
    for regel in regels :
        nummers.append(int(regel.strip().split(',')[0]))

