Das Programm

Bei diesem Beispiel weiß man, wie oft die gleiche Aktion (Würfeln) ausgeführt werden soll. Deshalb wird im Programm
eine for-Schleife verwendet. Vergiss nicht den Doppelpunkt! Er zeigt an, dass nun ein neuer Bock beginnt.

    from random import randint
    for nr in range(51):
        zahl = randint(1, 5)
