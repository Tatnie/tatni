def registreertijd(hardloper):
    vandaag=datetime.datetime.totday()
    s=vandaag.strftime("a d v y," H:M:S)
    s+=','+hardloper
    outfile=open('hardlopers.txt')
    outfile.write('s+\n')
    print(s)

    def registreerHardloper():
        while True:
            Hardlopernaam=input('Hoe heet deze hardloper?)\n
                                if hardlopernaam=="":
                                    break
            registeertijd(hardlopersnaam)

            registeerhardloper
