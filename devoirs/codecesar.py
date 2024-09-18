def Decrypter():
    code=input("Entrez le message à déchifrer: ")
    decalage=int(input("Entrez le décalage entre 1 et 26: "))
    if decalage>26:
        print("Entrez un nombre en 1 et 26 ! ")
        while int(decalage)>26:
            decalage=input("Entrez le décalage entre 1 et 26: ")
    
    codenb = []
    for i in code:
        codenb.append(ord(i.upper())) #ça met aussi les espaces
    
    codemodif=[]

    for i in codenb:
        if i == 32:
            codemodif.append(i)
        else:
            i = i - decalage
            if i<65:
                i = i+26
                codemodif.append(i)
            else:
                codemodif.append(i)
    
    final = []

    for i in codemodif:
        final.append(chr(i))
    print(''.join(final))


Decrypter()
